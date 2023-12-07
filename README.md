# File Signature Verification
This repository was created as a requirement of CIS 442 (Digital Forensics Project) at UMass Dartmouth.

## Introduction
This Python script provides a solution for verifying the integrity and authenticity of files in a directory. It reads the file signatures (mime files) and compares them with expected values based on the file's extension. This tool is particularly useful in scenarios involving security checks, data validation, or forensic analysis.

## Features
- **Signature Extraction**: Efficiently reads the first few bytes of files to extract their signatures.
- **Comprehensive File Type Support**: Includes a wide range of file types, from images and documents to audio and video formats.
- **Recursive Directory Scanning**: Scans all files within a specified directory and its subdirectories.
- **Mismatch Identification**: Clearly identifies files whose content does not match their extension.

## Getting Started

### Prerequisites
Ensure you have Python 3.x installed. You can download this from [Python's official website](https://www.python.org/downloads/).

### Installation
To get started with this script, clone the repository to your local machine:

```sh
git clone [repository URL]
```

### Usage
1. Edit the script to specify the directory you wish to scan. For example:

   ```python
   directory_to_check = '/path/to/your/directory'
   ```

2. Run the script using Python:

   ```sh
   python file_signature_verification.py
   ```

   This will print out a list of files with mismatched signatures.

## Documentation

### How It Works
- **File Signature Reading**: The script opens each file in binary mode and reads the first 10 (`file.read(10)`) bytes to determine the file's signature.
- **Signature Verification**: It compares this signature against a predefined list of signatures for various file types. If you choose to add more file sigatures for verification, refer to [Wiki Files Signatures](https://en.wikipedia.org/wiki/List_of_file_signatures)
- **Directory Scanning**: The script uses [`os.walk`](https://docs.python.org/3/library/os.html) to look through the given directory and checks each file it encounters.
- **Results**: Files with mismatched signatures are reported, providing insights into potentially changed or mislabeled files.

### Code Structure
- `import: os`: Imports the os module from the standard Python library.
- `get_file_signature(file_path)`: Function to extract the signature of a file.
- `check_file_signature(file_path)`: Function to verify the file's signature against expected values.
- `check_directory(directory_path)`: Function to scan a directory and identify files with mismatched signatures.
