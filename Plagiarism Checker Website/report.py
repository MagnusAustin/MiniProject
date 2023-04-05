# import pymongo
# client = pymongo.MongoClient("mongodb://localhost:27017/")
# db = client["Plagiarism_Checker"]
# collection = db["quotes"]
# for document in collection.find():
#     print(document)
import pymongo
import os
import re
from pdfkit import from_file

# Connect to the MongoDB database
client = pymongo.MongoClient('mongodb://localhost:27017/')
db = client['Plagiarism_Checker']
collection = db['quotes']

# Define the paths of the input and output files
input_file_path = './output/check.txt'
output_file_path = './report/report.pdf'

# Open and read the input file
with open(input_file_path, 'r') as input_file:
    input_text = input_file.read()

# Clean the input text by removing all non-alphanumeric characters and converting it to lowercase
clean_input_text = re.sub(r'\W+', ' ', input_text).lower()

# Retrieve all the documents from the MongoDB collection
documents = collection.find()

# Iterate through each document and compare it with the input text
plagiarism_count = 0
plagiarism_records = []
for document in documents:
    clean_document_text = re.sub(r'\W+', ' ', document['quote']).lower()
    if clean_document_text in clean_input_text:
        plagiarism_count += 1
        plagiarism_records.append({
            'document_id': document['_id'],
            'plagiarized_text': document['quote'],
            'matching_text': clean_document_text
        })

# Calculate the percentage of plagiarism
plagiarism_percentage = round(plagiarism_count / collection.count_documents({}) * 100, 2)

# Generate the plagiarism report
report = f'Plagiarism Percentage: {plagiarism_percentage}%\n\n'
for record in plagiarism_records:
    report += f'Document ID: {record["document_id"]}\n'
    report += f'Plagiarized Text: {record["plagiarized_text"]}\n'
    report += f'Matching Text: {record["matching_text"]}\n\n'

# Write the plagiarism report to a text file
with open('./report/report.txt', 'w') as report_file:
    report_file.write(report)

# Convert the plagiarism report to a PDF file
from_file('./report/report.txt', output_file_path)
