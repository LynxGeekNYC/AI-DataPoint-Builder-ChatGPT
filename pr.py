import pdfplumber
import pytesseract
from PIL import Image
import re
import json

# Function to extract text from PDF
def extract_text_from_pdf(pdf_path):
    text = ""
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text += page.extract_text()
    return text

# Function to extract text from Image using OCR
def extract_text_from_image(image_path):
    image = Image.open(image_path)
    text = pytesseract.image_to_string(image)
    return text

# Function to extract key data points from report text
def extract_data_from_report(report_text):
    # Define regular expressions to extract relevant information
    case_pattern = r'NYPD Case No: ([\d-]+)'
    date_pattern = r'Date: ([\w\s,]+)'
    location_pattern = r'Location: ([\w\s,]+)'
    officer_pattern = r'Officer: ([\w\s]+), Badge No\. ([\d]+)'
    incident_pattern = r'Type of Incident: ([\w\s]+)'
    injuries_pattern = r'Injuries: ([\w\s,]+)'
    narrative_pattern = r'Narrative: (.+)'

    # Use regex to find the corresponding data
    case_no = re.search(case_pattern, report_text)
    date = re.search(date_pattern, report_text)
    location = re.search(location_pattern, report_text)
    officer = re.search(officer_pattern, report_text)
    incident_type = re.search(incident_pattern, report_text)
    injuries = re.search(injuries_pattern, report_text)
    narrative = re.search(narrative_pattern, report_text)

    # Organize the data into a dictionary
    report_data = {
        'case_no': case_no.group(1) if case_no else 'N/A',
        'date': date.group(1) if date else 'N/A',
        'location': location.group(1) if location else 'N/A',
        'officer': {
            'name': officer.group(1) if officer else 'N/A',
            'badge_no': officer.group(2) if officer else 'N/A'
        },
        'incident_type': incident_type.group(1) if incident_type else 'N/A',
        'injuries': injuries.group(1) if injuries else 'N/A',
        'narrative': narrative.group(1) if narrative else 'N/A'
    }

    return report_data

# Function to export data points to JSON format
def export_to_json(report_data, output_file):
    with open(output_file, 'w') as f:
        json.dump(report_data, f, indent=4)

# Example usage
if __name__ == '__main__':
    # Extract text from a PDF file or an Image file
    pdf_path = 'police_report.pdf'
    image_path = 'police_report_image.png'

    # Uncomment based on what you're using
    report_text_pdf = extract_text_from_pdf(pdf_path)  # For PDF
    report_text_image = extract_text_from_image(image_path)  # For Image

    # Choose which text to process (based on whether you're using PDF or Image)
    report_text = report_text_pdf  # or report_text_image

    # Extract structured data points from the report
    report_data = extract_data_from_report(report_text)

    # Export the extracted data to JSON format for future processing
    export_to_json(report_data, 'exported_report_data.json')

    print("Data extracted and exported to 'exported_report_data.json'")
