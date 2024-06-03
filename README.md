# XML to CSV Converter

This application converts XML files containing test case information into a CSV format.

## Usage

1. Place your XML files containing test case information in a folder.
2. Ensure you have Python installed on your system.
3. Clone this repository to your local machine.
4. Update the `data_folder` variable in `export_file.py` to point to the folder containing your XML files.
5. Run the following command to generate the CSV file:
    ```bash
    python export_file.py
    ```
6. The CSV file named `output_file.csv` will be created in the same directory.

## Important Note

To generate the CSV file, you need to use the `get_parsed_files` function provided in the `get_parsed_files` module.

Example:

```python
import get_parsed_files
import export_file

# Specify the folder containing XML files
data_folder = '/path/to/your/xml/files'

# Parse XML files to get class items
class_items = get_parsed_files.parse_xml_files(data_folder)

# Convert class items to CSV
export_file.groups_to_csv(class_items)

Replace /path/to/your/xml/files with the actual path to your XML files folder.
```

## License
This project is licensed under the MIT License.
