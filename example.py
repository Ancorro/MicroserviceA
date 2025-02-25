import json
import time


def create_json():
    example_data = {
        "cmd": "request",
        "pdf_path":"./pdf_folder/pdf3.pdf"
    }
    with open('a.json', 'w') as json_file:
        json.dump(example_data, json_file, indent=4)
    print("Example JSON file created.")


def print_json_data():
    with open('metadata.json', 'r') as json_file:
        data = json.load(json_file)
        print(json.dumps(data, indent=4))


# Run
create_json()
print_json_data()

