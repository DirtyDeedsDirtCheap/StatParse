import argparse
import sys
import csv
import time
from datetime import datetime, timezone

def read_file(infile):
    with open(infile, 'r', encoding='utf-8') as file:
        return [line.rstrip() for line in file.readlines()]


def parse_metadata(lines):
    fileName, size, inode, permission, owner, group, atime, mtime, ctime, btime = [], [], [], [], [], [], [], [], [], []
    utc = lines[4].split()[-1]
    if 'Birth' in lines[7]:
        jmp_idx = 8
        btime_check = True
    else:
        jmp_idx = 7
        btime_check = False

    for i in range(0, len(lines), jmp_idx):
        data_block = lines[i:i + jmp_idx]
        cleaning(data_block, fileName, size, inode, permission, owner, group, atime, mtime, ctime, btime, btime_check)

    return (fileName, size, inode, permission, owner, group, atime, mtime, ctime, btime)


def cleaning(data_block, fileName, size, inode, permission, owner, group, atime, mtime, ctime, btime, btime_check):
    data = [line.split() for line in data_block]
    fileName.append(get_filename(data))
    size.append(get_size(data))
    inode.append(get_inode(data))
    permission.append(get_permission(data))
    uid, gid = get_owner(data)
    owner.append(uid)
    group.append(gid)
    atime.append(get_timestamp(data, 4))
    mtime.append(get_timestamp(data, 5))
    ctime.append(get_timestamp(data, 6))
    if btime_check:
        btime.append(get_timestamp(data, 7))
    else:
        btime.append("-")

def convert_to_utc(date_str):
    # Define the date format
    date_format = '%Y-%m-%d %H:%M:%S %z'

    # Parse the date string into a datetime object
    local_dt = datetime.strptime(date_str, date_format)

    # Convert to UTC by using the timezone offset
    utc_dt = local_dt.astimezone(timezone.utc)

    # Return in ISO 8601 format
    return utc_dt.isoformat()
def get_filename(data):
    return data[0][1].replace('‘', '').replace('’', '')


def get_size(data):
    return data[1][1]


def get_inode(data):
    return data[2][3]


def get_permission(data):
    return data[3][1].split('/')[0].strip('()')


def get_owner(data):
    if len(data[3]) < 10:
        uid = data[3][4] + data[3][5]
        gid = data[3][4]
        uid = uid.replace("Gid:", "")
    else:
        uid = data[3][4] + data[3][5]
        gid = data[3][8] + data[3][9]
    return uid.strip('()'), gid.strip('()')


def get_timestamp(data, idx):
    date = convert_to_utc(f"{data[idx][1]} {data[idx][2].split('.')[0]} {data[idx][3]}")
    return date


def write_to_csv(output_file, metadata):
    with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:

        writer = csv.writer(csvfile)
        # Write header
        writer.writerow(
            ["File Name",  "Access Time", "Modify Time", "Change Time", "Birth Time", "User", "Group", "Permission", "inode", "Size"])
        # Write data rows
        for i in range(len(metadata[0])):
            writer.writerow([metadata[0][i], metadata[6][i], metadata[7][i], metadata[8][i],
                             metadata[9][i], metadata[4][i], metadata[5][i],
                             metadata[3][i], metadata[2][i], metadata[1][i]])


def main():
    parser = argparse.ArgumentParser(sys.argv[1:])
    parser.add_argument('-f', '--file', help="Result file of stat command", dest='stat_file')
    parser.add_argument('-o', '--out', help="Specify output file name", dest='output_file')
    args = parser.parse_args()

    # Input file verification
    if not args.stat_file:
        print("Please provide the path to the stat command result file!")
        print("Use the '-f' or '--file' option.")
        exit(0)

    stat_file = args.stat_file
    output_file = args.output_file if args.output_file else "stat_parse_result.csv"

    # Start time counter
    start_time = time.time()

    # Parse metadata
    lines = read_file(stat_file)
    metadata = parse_metadata(lines)

    # Write to CSV
    write_to_csv(output_file, metadata)

    # Calculate and print execution time
    end_time = time.time()
    print(f"CSV file '{output_file}' generated successfully.")
    print(f"Execution Time: {end_time - start_time:.2f} seconds")


if __name__ == "__main__":
    main()
