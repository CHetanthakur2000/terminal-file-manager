import os
import time

menu = """
======== TERMINAL FILE MANAGER ========

1. Show Current Directory
2. Change Directory
3. List Files & Folders
4. Search File
5. Create File
6. Create Folder
7. Rename File/Folder
8. Delete File
9. Delete Folder
10. File Information
11. Exit

=======================================
"""


#function

def show_directory():
	print("current directory",os.getcwd())
	
def change_directory():
	directory = input("Enter your directory name or back for 1 step back: ")
	try:
		if directory.lower() == "back":
			directory = ".."
		os.chdir(directory)
		print("directory changed successfully")
		print(os.getcwd())
	except FileNotFoundError:
		print("directory not found")
		
		
def list_files():
    for entry in os.scandir():
        if entry.is_dir():
            print("📁", entry.name)
        else:
            print("📝", entry.name)
            
def  search_file():
				name = input("enter file name:")
				found = False
				for root, dirs, files in os.walk(os.getcwd()):
					for file in files:
						if file == name:
							print("searching...")
							time.sleep(1)
							print("File Found: ",os.path.join(root, file))
							found = True
				if not found:
							print("file not found")
							
							
def create_file():
	file_name = input("Enter Your File Name: ")
	try:
					
							with open(file_name, "x")as file:
								file.write("")
								print("file created successfully")
			
	except FileExistsError:
							print("file already exists")
							
def create_folder():
							folder_name = input("enter your new folder name: ")
							try:
								os.mkdir(folder_name)
								print("directory created successfully")
								time.sleep(1)
								print("location: ",os.path.abspath(folder_name))
							except FileExistsError:
								print("pls change name your directory")
								
										
def rename_file():
							orginal_name = input("Enter your orginal file name: ")
							rename_name = input("Enter your rename file name: ")
							
							try:
								os.rename(orginal_name, rename_name)
								print("File rename successfully")
								print("location of rename file: ",os.path.abspath(rename_name))
							except FileNotFoundError:
								print("Original file not found")
							except FileExistsError:
							                     	print("File name already exists")
								
def delete_file():
							delete_file_name = input("Enter File name for delete: ")
							if os.path.isfile(delete_file_name):
								print("File current location: ",os.path.abspath(delete_file_name))
							else:
								print("this name file not found")
							try:
								os.remove(delete_file_name)
								print("File deleted")
								
							except:
								print("No match found for this file")
								
def delete_folder():
								delete_folder_name = input("Enter Folder name: ")
								if os.path.isdir(delete_folder_name):
									print("Folder current location: ",os.path.abspath(delete_folder_name))
									print("WARNING:-FIRST DELETE INSIDE FILES OF FOLDER")
								else:
									print("Directory not found")
								try:
									os.rmdir(delete_folder_name)
									print("Folder deleted")
								except OSError:
									print("Folder is not empty")
								except FileNotFoundError:
									print("File not found")
								
def file_info():
    name = input("Enter File or Folder name: ")

    try:
        info = os.stat(name)

        print("=" * 8, "File Info", "=" * 8)
        print("File Name:", name)
        print("Is File:", os.path.isfile(name))
        print("Path:", os.path.abspath(name))
        print("File Size:", info.st_size / 1024, "KB")
        print("Access Time:", info.st_atime)
        print("Modified Time:", info.st_mtime)
        print("=" * 32)

    except FileNotFoundError:
        print("There is no file or folder for information")
    
def exit_program():
											print("Thankyou for using Terminal File Manager ")
											
											
												
while True:
	print(menu)
	user = input("Enter your choice: ")
	if user == "1":
	    	show_directory()
	
	    	
	elif user == "2":
	 	change_directory()
	 	
	elif user == "3":
		list_files()
		
		
	elif user == "4":
		search_file()
		
		
	elif user == "5":
		create_file()
		
		
	elif user == "6":
		create_folder()
		
	elif user == "7":
		rename_file()	
		
	elif user == "8":
		delete_file()
		
	elif user == "9":
		delete_folder()
		
	elif user == "10":
		file_info()
		
	elif user == "11":
		
		exit_program()
		break
		
	else:
		print("invalid input")
		
	
		
		
		
	
