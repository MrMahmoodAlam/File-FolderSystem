import os

# File Making Function
def create_files(directory, name, file_type, file_number_list):
    for file in range(file_number_list):
        with open(os.path.join(directory, f'{name}{file+1}.{file_type}'), 'w') as fp:
            pass
    print("Successfully completed")


def make_folder(directory):
    while True:
        folder_type = int(input("Folder Name: 1. Custom Folder Name, 2. Number of Folders, 0. Go Back: "))
        
        if folder_type == 0:
            break

        # Single Folder Making
        elif folder_type == 1:
            folder_name = str(input("Enter your folder name: ")).strip()
            os.mkdir(os.path.join(directory, folder_name))
            print("Successfully completed")

            print("Your Files and Folder on that directory")
            folder_list = os.listdir(directory)
            for folder in folder_list:
                print(folder)

        # Multiple Folder Making
        elif folder_type == 2:
            folder_name = str(input("Enter folder name: ")).strip()
            folder_number = int(input("How many folders do you want to make: "))
            for folder in range(folder_number):
                os.mkdir(os.path.join(directory, f'{folder_name}{folder+1}'))
            print("Successfully completed")

            print("Your Files and Folder on that directory")
            folder_list = os.listdir(directory)
            for items in folder_list:
                print(items)
        else:
            print("Please enter a correct option")

def make_file(directory):
    while True:
        file_name_list = int(input("File Name: 1. Custom File Name, 2. Number of Files, 0. Go Back: "))
        
        if file_name_list == 0:
            break

        # Single File Making
        elif file_name_list == 1:
            print("You selected to make a single file")
            file_name = str(input("Enter file name: ")).strip()
            file_extension = input('Enter file type: 1. Text file, 2. Word file, 3. Excel file, 4. Other type: ')

            if file_extension == "1":
                with open(os.path.join(directory, f'{file_name}.txt'), 'w') as text_filewriting:
                    pass
                
                print("Congratulations, you made a text file")
                print("Your Files and Folder on that directory")
                file_list = os.listdir(directory)
                for files in file_list:
                    print(files)
            
            elif file_extension == "2":
                with open(os.path.join(directory, f'{file_name}.docx'), 'w') as word_filewriting:
                    pass
                print("Congratulations, you made a Word file")
                print("Your Files and Folder on that directory")
                file_list = os.listdir(directory)
                for files in file_list:
                    print(files)

            elif file_extension == "3":
                with open(os.path.join(directory, f'{file_name}.xlsx'), 'w') as excel_filewriting:
                    pass
                print("Congratulations, you made an Excel file")
                print("Your Files and Folder on that directory")
                file_list = os.listdir(directory)
                for files in file_list:
                    print(files)

            elif file_extension == "4":
                custom_file_extension = input("Enter your file extension name: ").strip()
                with open(os.path.join(directory, f'{file_name}.{custom_file_extension}'), 'w') as custom_filewriting:
                    pass
                print(f'Congratulations, you made a {custom_file_extension} file')
                print("Your Files and Folder on that directory")
                file_list = os.listdir(directory)
                for files in file_list:
                    print(files)

            else:
                print("Please select the correct option")

        # Multiple File Making
        elif file_name_list == 2:
            multiple_file_name = input("Enter file name: ").strip()
            file_number = int(input("How many files do you want to make: "))
            selecting_file_type = input('Enter file type: 1. Text file, 2. Word file, 3. Excel file, 4. Other type: ')

            if selecting_file_type == "1":
                create_files(directory, multiple_file_name, "txt", file_number)
                print("Your Files and Folder on that directory")
                file_list = os.listdir(directory)
                for files in file_list:
                    print(files)

            elif selecting_file_type == "2":
                create_files(directory, multiple_file_name, "docx", file_number)
                print("Your Files and Folder on that directory")
                file_list = os.listdir(directory)
                for files in file_list:
                    print(files)

            elif selecting_file_type == "3":
                create_files(directory, multiple_file_name, "xlsx", file_number)
                print("Your Files and Folder on that directory")
                file_list = os.listdir(directory)
                for files in file_list:
                    print(files)

            elif selecting_file_type == "4":
                custom_file_extension = input("Enter your file extension name: ").strip()
                create_files(directory, multiple_file_name, custom_file_extension, file_number)
                print("Your Files and Folder on that directory")
                file_list = os.listdir(directory)
                for files in file_list:
                    print(files)

            else:
                print("Please select the correct option")
        else:
            print("Please select the correct option")

def list_files_and_folders(path):
    """
    Recursively list all files and folders in the given directory path.
    """
    for root, dirs, files in os.walk(path):
        level = root.replace(path, '').count(os.sep)
        indent = ' ' * 4 * (level)
        print(f'{indent}{os.path.basename(root)}/')
        subindent = ' ' * 4 * (level + 1)
        for f in files:
            print(f'{subindent}{f}')

def search_files_and_folders(path, search_name):
    """
    Search for a specific file or folder name in the given directory path.
    """
    matches = []
    for root, dirs, files in os.walk(path):
        for name in dirs + files:
            if search_name.lower() in name.lower():
                matches.append(os.path.join(root, name))
    return matches

def search_and_list_files(directory):
    # List files and folders
    print(f"\nListing files and folders in: {directory}\n")
    list_files_and_folders(directory)

    # Search for a specific file or folder
    search_name = input("\nEnter the file or folder name to search: ")
    matches = search_files_and_folders(directory, search_name)

    if matches:
        print(f"\nFound the following matches for '{search_name}':")
        for match in matches:
            print(match)
    else:
        print(f"\nNo matches found for '{search_name}'.")

while True:
    print("Please select an option:")
    print("1. Make Folder")
    print("2. Make File")
    print("3. List and Search Files/Folders")
    print("0. Exit")

    option = int(input("Enter your number: "))
    if option == 0:
        break
    elif option == 1:
        file_directory = input("Enter your path: ").strip()
        make_folder(file_directory)
    elif option == 2:
        file_directory = input("Enter your path: ").strip()
        make_file(file_directory)
    elif option == 3:
        file_directory = input("Enter your path: ").strip()
        search_and_list_files(file_directory)
    else:
        print("You selected the wrong option, please select the correct option")