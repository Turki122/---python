#----------------------
#---------File Handling write and Append in file------
#---------------------------------------------


myFile = open("C:\python\Turki.txt", "w")
myFile.write("Hello\n")
myFile.write("Third Line")

myFile = open(r"C:\python\fun.txt", "w")
myFile.write("Elzero Web School\n" * 1000)

myList = ["Oasma\n", "Ahmed\n", "Sayed\n"]

myFile = open(r"C:\python\osama.txt", "w")
myFile.writelines(myList)

myFile = open(r"C:\python\osama.txt", "a")
myFile.write("Elzero")

