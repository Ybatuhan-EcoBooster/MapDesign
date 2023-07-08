# Libraries
import glob
import os

def FileName():
    # Directory path where the PNG files are located
    directory = "D:\dosyalar\Github\MapDesign\Images"

    # Search for PNG files in the directory
    png_files = glob.glob(os.path.join(directory, "*.png"))

    # Iterate over each PNG file
    for file_path in png_files:
        # Extract the file name from the file path
        file_name = os.path.basename(file_path)

        # Remove the file extension from the file name
        file_name_without_extension = os.path.splitext(file_name)[0]

        # Print the extracted file name
    return file_name_without_extension

