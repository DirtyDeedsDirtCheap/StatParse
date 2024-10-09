
# Stat Parse

A Python script that processes the output of the `stat` command and converts it into a CSV file, summarizing file metatata such as access time, modification time, permissions, and more. This project is a rebuild of the original [linux-metadata-parser](https://github.com/genes1sx/linux-metadata-parser).

## Table of Contents
- [Prerequisites](#prerequisites)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Arguments](#arguments)
- [Example](#example)
- [Acknowledgements](#acknowledgements)
- [License](#license)

## Prerequisites

Before using this script, you need to generate a file containing the output of the `stat` command. You can do this but running the following command in your terminan:


```bash
find ./ -exec stat '{}' \; > stat.meta
```

This command will create a file named `stat.meta` with the metadata of all files in the root directory. Make sure to run itwith the approirate permissions.

## Features 
- Reads the output of the `stat` command from a specified file.
- Parses the metadata, including:
  - File name
  - Size
  - Inode
  - Permissions
  - Owner and group
  - Access, modification, change, and birth times
- Converts timestamps to UTC format.
- Exports the parsed data to a CSV file, where the fields are organized in a clear and user-friendly manner for easy analysis.

## Installation

1. Make sure you have Python 3 installed on your machine.
2. Clone this repository:
   ```bash
   git clone https://github.com/DirtyDeedsDirtCheap/StatParse.git
   ```
3. Navigate to the project directory:
   ```bash
   cd StatParse
   ```

## Usage

Run the script from the command line, providing the path to the `stat` command output file and (optionally) specifying the output CSV file name.

```bash
python script_name.py -f path_to_stat_file -o output_file_name.csv
```

## Arguments

- `-f`, `--file`: Specify the path to the result file of the `stat` command (required).
- `-o`, `--out`: Specify the name of the output CSV file (optional; defaults to `stat_parse_result`).

## Example

Assuming you have a file named `stat_output.txt` containing the output of the `stat` command:

```bash
python script-name.py -f stat_output.txt -o output_metadata.csv
```

This will generate a file named `output_metadata.csv` in the same directory.

## Acknowledgements

This project is a rebuild of the original [linux-metadata-parser](https://github.com/genes1sx/linux-metadata-parser)

MIT License

Copyright (c) 2022 j4hmilli

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
