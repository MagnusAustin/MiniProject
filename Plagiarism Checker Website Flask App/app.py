# import os
# import textract
# from flask import Flask, request, redirect
# from werkzeug.utils import secure_filename

# # Define supported file extensions
# SUPPORTED_EXTENSIONS = [".pdf", ".docx", ".jpg", ".jpeg", ".png", ".gif", ".txt"]

# # Define input and output folder paths
# input_folder = "input"
# output_folder = "output"

# app = Flask(__name__)
# app.config['UPLOAD_FOLDER'] = input_folder

# # Create the output folder if it doesn't exist
# os.makedirs(output_folder, exist_ok=True)

# @app.route('/')
# def index():
#     return '''<!DOCTYPE html>
# <html>
# <head>
#     <title>Plagiarism Checker</title>
# </head>
# <body>
#     <h1>Plagiarism Checker</h1>
#     <form action="/upload" method="post" enctype="multipart/form-data">
#         <input type="file" name="file" multiple>
#         <input type="submit" value="Check Plagiarism">
#     </form>
# </body>
# </html>'''

# @app.route('/upload', methods=['POST'])
# def upload_file():
#     # Save the uploaded file
#     file = request.files['file']
#     filename = secure_filename(file.filename)
#     file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    
#     # Check if the file is a supported format
#     _, file_extension = os.path.splitext(filename)
#     if file_extension not in SUPPORTED_EXTENSIONS:
#         print(f"'{filename}' is not a supported file format.")
#         return redirect('/')
    
#     # Build the input and output file paths
#     input_file = os.path.join(input_folder, filename)
#     output_file = os.path.join(output_folder, os.path.splitext(filename)[0] + ".txt")

#     # Extract text from the input file
#     text = textract.process(input_file).decode("utf-8")

#     # Write the extracted text to the output file
#     with open(output_file, "w") as f:
#         f.write(text)

#     print(f"Text has been extracted from '{filename}' and saved to '{output_file}'.")
    
#     return redirect('/')

# if __name__ == '__main__':
#     app.run(debug=True)

import os
import textract
from flask import Flask, request, redirect

from werkzeug.utils import secure_filename

# Define supported file extensions
SUPPORTED_EXTENSIONS = [".pdf", ".docx", ".jpg", ".jpeg", ".png", ".gif", ".txt"]

# Define input and output folder paths
input_folder = "input"
output_folder = "output"

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = input_folder

# Create the output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

@app.route('/')
def index():
    return '''<!DOCTYPE html>
<html>
<head>
    <title>Plagiarism Checker</title>
</head>
<body>
    <h1>Plagiarism Checker</h1>
    <form action="/upload" method="post" enctype="multipart/form-data">
        <input type="file" name="file" multiple>
        <input type="submit" value="Check Plagiarism">
    </form>
</body>
</html>'''

@app.route('/upload', methods=['POST'])
def upload_file():
    # Save the uploaded file
    file = request.files['file']
    filename = secure_filename(file.filename)
    file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

    # Check if the file is a supported format
    _, file_extension = os.path.splitext(filename)
    if file_extension not in SUPPORTED_EXTENSIONS:
        print(f"'{filename}' is not a supported file format.")
        return redirect('/')

    # Build the input and output file paths
    input_file = os.path.join(input_folder, filename)
    output_file = os.path.join(output_folder, 'check' + ".txt")

    # Extract text from the input file
    text = textract.process(input_file).decode("utf-8")

    # Write the extracted text to the output file
    with open(output_file, "w") as f:
        f.write(text)

    print(f"Text has been extracted from '{filename}' and saved to '{output_file}'.")
    
    # Return a success message
    return '''<!DOCTYPE html>
<html>
<head>
    <title>Plagiarism Checker</title>
</head>
<body>
    <h1>Plagiarism Checker</h1>
    <p>File uploaded successfully!</p>
    <form action="/upload" method="post" enctype="multipart/form-data">
        <input type="file" name="file" multiple>
        <input type="submit" value="Check Plagiarism">
    </form>
</body>
</html>'''

if __name__ == '__main__':
    app.run(debug=True)
