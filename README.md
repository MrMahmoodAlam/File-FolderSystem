# File and Folder Management Script

This Python script provides a simple command-line interface for creating and managing files and folders in a specified directory. It includes functionalities to create single or multiple files and folders, list all files and folders, and search for specific files or folders within a directory.

## Features

1. **Create Folders**:
   - Create a custom-named folder.
   - Create multiple folders with a common base name and sequential numbering.

2. **Create Files**:
   - Create a single file with a custom name and specified extension (e.g., .txt, .docx, .xlsx).
   - Create multiple files with a common base name and specified extension.

3. **List and Search**:
   - Recursively list all files and folders in a given directory.
   - Search for specific files or folders by name within a directory and its subdirectories.

## How to Use

1. Clone the repository to your local machine.
2. Run the script using a Python interpreter.
3. Follow the on-screen prompts to perform the desired file and folder management operations.

### Sample Execution

```bash
Please select an option:
1. Make Folder
2. Make File
3. List and Search Files/Folders
0. Exit

Enter your number: 1
Enter your path: /path/to/directory

Folder Name: 
1. Custom Folder Name
2. Number of Folders
0. Go Back

Enter your folder name: MyFolder
Successfully completed
```

### Functions

- `create_files(directory, name, file_type, file_number_list)`: Create multiple files with a specified base name and file type.
- `make_folder(directory)`: Create a single or multiple folders based on user input.
- `make_file(directory)`: Create a single or multiple files based on user input.
- `list_files_and_folders(path)`: Recursively list all files and folders in the given directory path.
- `search_files_and_folders(path, search_name)`: Search for specific file or folder names in the given directory path.
- `search_and_list_files(directory)`: List files and folders in a directory and search for a specific file or folder.

### Prerequisites

- Python 3.x
- OS module (part of the standard Python library)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

Feel free to customize this description as per your needs before uploading it to GitHub.
