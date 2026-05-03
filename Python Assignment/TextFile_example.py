
#Assignment question 3
"""
This code opens a file named myfile.txt in write mode using the open() function.
If there is no existing file with that name, it creates a new one. I
f there is an existing file, it overwrites the content of the file.
Then, it writes two lines of text to the file using the write() method. 
Finally, it closes the file using the close() method to ensure that all data is saved properly.
"""
with open("myfile.txt", "w") as f: 

    f.write("Hello, this is a text file.\n")
    f.write("We can write multiple lines to the file.\n")
    f.close()

#Assignment question 4
"""
This code opens myfile.txt in reaad mode with open() function and 
reads content of the file using read() method and prints it to the console. 
Finally, it closes the file using close() method.

"""
f=open("myfile.txt", "r")
content = f.read()
print(content)
f.close()