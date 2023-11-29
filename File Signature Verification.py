import os # imports the 'os' module

def get_file_signature(file_path):

    # Reads the first few bytes of a file and returns the file signature.

    with open(file_path, 'rb') as file: # The file_path is being read in binary ('rb')
        return file.read(10) # Reading the first '10' bytes of the file signature

def check_file_signature(file_path):

    # Checks the file signature against its extension and returns the file path if they don't match.
    # Down below is the types of file extensions. More can be added.
    # Utilize https://en.wikipedia.org/wiki/List_of_file_signatures for more file signatures.
    
    file_signatures = {
    '.jpg': [b'\xFF\xD8\xFF'],
    '.jpeg': [b'\xFF\xD8\xFF'],
    '.png': [b'\x89\x50\x4E\x47\x0D\x0A\x1A\x0A'],
    '.gif': [b'GIF87a', b'GIF89a'],
    '.pdf': [b'%PDF-'],
    '.zip': [b'PK\x03\x04', b'PK\x05\x06', b'PK\x07\x08'],
    '.rar': [b'Rar!\x1A\x07\x00'],
    '.7z': [b'7z\xBC\xAF\x27\x1C'],
    '.mp3': [b'ID3'],
    '.wav': [b'RIFF'],
    '.avi': [b'RIFF'],
    '.mp4': [b'\x00\x00\x00\x18ftypmp42'],
    '.mov': [b'\x00\x00\x00\x14ftyp'],
    '.doc': [b'\xD0\xCF\x11\xE0\xA1\xB1\x1A\xE1'],
    '.docx': [b'PK\x03\x04'],
    '.xls': [b'\xD0\xCF\x11\xE0\xA1\xB1\x1A\xE1'],
    '.xlsx': [b'PK\x03\x04'],
    '.ppt': [b'\xD0\xCF\x11\xE0\xA1\xB1\x1A\xE1'],
    '.pptx': [b'PK\x03\x04'],
    '.bmp': [b'BM'],
    '.html': [b'<!DOCTYPE HTML>', b'<HTML>', b'<html>'],
    '.xml': [b'<?xml version="1.0"?>', b'<?xml version="1.1"?>'],
    '.psd': [b'8BPS'],
    '.ogg': [b'OggS']  
    }

    file_signature = get_file_signature(file_path)
    extension = os.path.splitext(file_path)[1].lower()

    if extension in file_signatures:
        if not any(file_signature.startswith(sig) for sig in file_signatures[extension]): # Checks any if any of the signatures matches the extension
            return file_path
    return None

def check_directory(directory_path):

    # Iterates over files in a directory and checks each file.

    mismatched_files = []
    for root, dirs, files in os.walk(directory_path):
        for file in files:
            file_path = os.path.join(root, file)
            mismatch_result = check_file_signature(file_path)
            if mismatch_result:
                mismatched_files.append(mismatch_result)
    return mismatched_files  # Returns any mismatched files

# Usage
directory_to_check = '/path/to/your/directory' # <-- Add your path to directory here.
print(check_directory(directory_to_check))
