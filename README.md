# Overview: MicroserviceA - PDF Metadata Scraper
Microservice 'A' for Kelly's project, this program will take a given pdf and scrape the metadata using the PyPDF2 library. 
It searches for a request json file every .5 seconds, when it finds one, it processes the request and gets the metadata for the pdf.
Then it outputs the metadata to a json file titled "metadata.json" and renames the request json to "processed{x}" where x is an incrementing integer. 

# How to Programmatically REQUEST Data
The user needs to save a JSON file to the same directory as microservice A with the title "a.json", they dont need to call the program.
The JSON file needs two data fields, a "cmd" field with "request, and a "pdf_path" field with a path string

Example of a valid request JSON: 
```
{
    "cmd": "request",
    "pdf_path": "./pdf_folder/pdf3.pdf"
}
```

# How to Programmatically RECEIVE Data
The metadata will be saved to a JSON file titled "metadata.json"

Here is an example of the data:
```
{
    "title": "An Introduction to Formal Languages and Automata",
    "creation_date": "2022-01-13T19:31:21+00:00",
    "modification_date": "2022-01-13T19:31:23+00:00",
    "author": "Peter Linz",
    "subject": null,
    "producer": "calibre (3.10.0) [https://calibre-ebook.com]"
}
```
if any field is not found by the metadata scraper, it will have a null value. 

**When another request is processed, the last one is overwritten, so the caller must assure the metadata is saved before creating another request json**

# ULM Sequence Diagram
![image](https://github.com/user-attachments/assets/56b7b7ea-4fad-46e3-8061-2ba4485f1acf)

