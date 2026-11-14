# Python program to demonstrate file manipulation

# 1. WRITE DATA INTO A FILE
file = open("student.txt", "w")
file.write("Student Name: Tanmay Yelwande\n")
file.write("Roll No: 34\n")
file.write("Course: AI and ML\n")
file.close()
print("Data Written successfully.\n")

# 2. READ DATA FROM THE FILE
file = open("student.txt", "r")
data = file.read()
print("Contents of student.txt")
print(data)
file.close()

# 3. Append data to the file
file = open("student.txt", "a")
file.write("semester: Third\n")
file.write("subject: Python\n")
file.close()
print("Data append successfully.\n")

# read updated contents
file = open("student.txt", "r")
data = file.read()
print("updated contents of student.txt:")
print(data)
file.close()

# 4. Copy contents from one file to another
source = open("student.txt", "r")
destination = open("student_copy.txt", "w")
data = source.read()
destination.write(data)
source.close()
destination.close()
print("File copied successfully.\n")

file = open("student_copy.txt", "r")
data = file.read()
print("Contents of student_copy.txt:")
print(data)
file.close()

print("All file operations completed successfully.")
