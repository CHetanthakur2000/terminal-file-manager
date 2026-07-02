import os


menu = """

======== terminal file manager =========
1. Show Current Directory
2. Change Directory
3. List Files & Folders
4. Search Files
5. Create File
6. Create Folder
7. Rename File/Folder
8. Delete File
9. Delete Folder
10. File Information
11. Exit
"""
while True:
	print(menu)
	user = input("Enter your choice: ")
	
	if user == "1":
		print("current directory: ",os.getcwd())
		
	elif user == "2":
		Directory = input("Enter your directory name: ")
		try:
			os.chdir(Directory)
			print("current directory: ",os.getcwd())
		except:
			
			print("directory not found")
	elif user == "3":
		for entry in os.scandir():
			if entry.is_dir():
				print("📁",entry.name)
			else:
				print("📝",entry.name)
	elif user == "4":
		name=input("enter your file name: ")
		found = False
		for root, dirs, files in os.walk(os.getcwd()):
			for file in files:
			 if file == name:
			 	print(os.path.join(root,file))
			 	found = True
		if not found:
			 print("no file found")
			 
			 
	elif user == "5":
			 file2 = input("enter file name: ")
			 if os.path.isfile(file2):
			 	print("file already exists")
			 else:
			 		
			 		
			 		with open (file2,"w")as file:
			 			text = input("give some text: ")
			 			file.write(text)
			 			print("file created successfully")
			 print("location: ",os.path.abspath(file2))
	
	elif user == "6":
			 new_folder = input("enter your folder name: ")
			 if os.path.isdir(new_folder):
			 	print("file already exists pls give another name")
			 else:
			 	os.mkdir(new_folder)
			 	print("directory created successfully ")
			 	print("current location: ",os.path.abspath(new_folder))
			 	
	elif user == "7":
		current_file = input("current file or folder name: ")
		rename_file = input("enter your rename file or folder name: ")
		try:
			os.rename(current_file,rename_file)
			print("file name changed")
		except:
			print("this name is not vaible or file not found")
			print("location",os.path.abspath(rename_file))
	
	
	elif user == "8":
		del_file_name = input("Enter file name for delete: ")
		try:
			os.remove(del_file_name)
			print("file deleted successfully")
		except FileNotFoundError:
			print("file not found: ",del_file_name)
		except IsADirectoryError:
			print("this is a directory")
			print("location:",os.path.abspath(del_file_name))
	
	
	elif user == "9":
		del_folder_name = input("Enter your folder name for delete ensure fisrt delete folder files: ")
		try:
			os.rmdir(del_folder_name)
			print("folder deleted")
		except FileNotFoundError:
			print("Folder not found or this is file")
			
		except OSError:
		  print("Folder is not empty")
		
		
		
	elif user == "10":
		detail_file_folder = input("enter your file or folder name details: ")
		try:
				
				info = os.stat(detail_file_folder)
				print("="*8,"File Detail","="*8)
				print("FILE NAME: ",detail_file_folder)
				print("FILE AVAIBLE: ",os.path.isfile(detail_file_folder))
				print("FILE PATH: ",os.path.abspath(detail_file_folder))
				print("file Size: ",info.st_size / 1024,"KB")
				print("Last Modified: ",info.st_mtime)
				print("Access time: ", info.st_atime )
				print("="*35)
		except FileNotFoundError:
				
				print("file not found")
			
	elif user == "11":
	 	print("thankyou for using our terminal file manager💗")
	 	break
	 	
	 
	else:
	 	
	 	print("invalid choice")
			
		
		
		
