import os
import textract

# Define supported file extensions
SUPPORTED_EXTENSIONS = [".pdf", ".docx", ".jpg", ".jpeg", ".png", ".gif", ".txt"]

# Define input and output folder paths
input_folder = "input"
output_folder = "output"

# Create the output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

# Loop through all the files in the input folder
for filename in os.listdir(input_folder):
    # Check if the file is a supported format
    _, file_extension = os.path.splitext(filename)
    if file_extension not in SUPPORTED_EXTENSIONS:
        print(f"'{filename}' is not a supported file format.")
        continue

    # Build the input and output file paths
    input_file = os.path.join(input_folder, filename)
    output_file = os.path.join(output_folder, 'check' + ".txt")

    # Extract text from the input file
    text = textract.process(input_file).decode("utf-8")

    # Write the extracted text to the output file
    with open(output_file, "w") as f:
        f.write(text)

    print(f"Text has been extracted from '{filename}' and saved to '{output_file}'.")
