# python-openpyxl
Finding car brands in xlsx using python openpyxl library
![Ekran görüntüsü 2024-09-29 220736](https://github.com/user-attachments/assets/722a8c52-ab28-48e9-b65e-4b96901d1fcd)
# Let's create the README.md file for the user

readme_content = """
# Car Brand and Model Query Script - README

## Overview
This Python script allows users to search for car brands and their respective models from an Excel file (`car_brands_and_models.xlsx`). The script uses the `openpyxl` library to read data from the Excel file, and it provides an interactive prompt for users to search for specific car brands or display all car entries in the file. Additionally, the script makes use of the `colorama` library to color the terminal output, providing a more user-friendly experience.

## Features
- **Load Excel File**: The script loads an Excel file containing car brands and models.
- **Search Functionality**: Users can search for specific car brands, and the script will return the corresponding models.
- **Display All Cars**: Users can type a special command (`all_car`) to display all car brands and models from the Excel file.
- **Exit**: The user can exit the script by typing `Exit`.
- **Color-Coded Output**: Output is color-coded to enhance the user experience:
  - Green text for the introductory banner.
  - Yellow text for car details.
  - Red text when a car brand is not found.
  
## Requirements

To run this script, you need to have the following Python libraries installed:

- `openpyxl`: For reading Excel files.
- `colorama`: For coloring terminal text.

You can install the necessary libraries using `pip`:

```bash
pip install openpyxl colorama
