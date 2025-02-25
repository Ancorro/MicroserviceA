import json
import time
import os
from PyPDF2 import PdfReader

"""
Looks for a json file titled in the same directory titled "a.json"
that has the format:
    {
        "cmd":"request",
        "pdf_path":"./pdf_folder/pdf_name.pdf"
    }

It renames the input JSON to "processed{x}" where x is incremented
Then it will print the pdf metadata to json file titled "metadata.json"
"""


def main_program():
    count = 0
    while True:
        pdf_path = get_pdf_path("./a.json", count)
        count += 1
        if pdf_path:
            scrape_pdf(pdf_path)

        time.sleep(.5)


def get_pdf_path(file_path, idx):
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            
        if 'cmd' in data and data['cmd'] == 'request' and 'pdf_path' in data:
            data['cmd'] = 'request'  # Modify "cmd" field

            # Overwrite the JSON file with the updated data
            with open(file_path, 'w') as file:
                json.dump(data, file, indent=4)

            new_file_name = f"processed{idx}"
            new_file_path = os.path.join(new_file_name)

            # Rename the file
            os.rename(file_path, new_file_path)

            return data['pdf_path']
        else:
            return False
    except (FileNotFoundError, json.JSONDecodeError):
        #print(f"Error reading JSON file: {e}")
        return False
    except OSError as e:
        print(f"Error renaming file: {e}")
        return False


def scrape_pdf(pdf_path):
    try:
        reader = PdfReader(pdf_path)
        info = reader.metadata  # Correct attribute access

        meta = {
            "title": info.title if info.title else None,
            "creation_date": info.creation_date.isoformat() if info.creation_date else None,
            "modification_date": info.modification_date.isoformat() if info.modification_date else None,
            "author": info.author if info.author else None,
            "subject": info.subject if info.subject else None,
            "producer": info.producer if info.producer else None
        }

        # Save metadata to a JSON file
        with open('metadata.json', 'w') as json_file:
            json.dump(meta, json_file, indent=4)

        print("Metadata saved to metadata.json")
    except Exception as e:
        print(f"Error reading PDF file: {e}")


# Run
main_program()
