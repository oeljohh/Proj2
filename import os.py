import os
import pathlib

os.system('cls')
os.system('ls -l')

def GetState():
        state1 = input("Pick a state  ") 
        return state1;

def FormatState(sName):
        if len(sName) < 8:
            seName = sName.ljust( 8, '*')
            return seName;
        else:
            return sName;

print("1 Get informa3tion and display to screen  ")
print("2 Get Call user created functions  ")
print("3 Write a List of files to file  ")
print("4 Read the specified file  ")
choice = input("Enter number of task to do:  ")

if choice == "1":

    companyName = "Dunwoody College"
    programName = "Computer Net"
    uName = os.environ['UserName']
    classFirst =input("What was the name of your first class ")
    classSecond =input("What is the name of your second class ")
    message = "John First class is  " +  classFirst  + " Then he goes to  " + classSecond + " Then he goes home"
    message2 = uName +  "works at"  + companyName + "And is also studying  " + programName + "while still working"
    print(message)
    print(message2)


elif choice == "2":

    state = GetState()
    newState = FormatState(state)
    print(" state is " + state + " new state is " + newState )

elif choice == "3":
    fileOfFiles = input(" whats the name of the file  ")
    fList = []
    for p in pathlib.Path('.').iterdir():
        if p.is_file():
            fList.append(p)
    with open(fileOfFiles, "w") as myFile:
        myFile.write("my list of file: \n ")
        for f in fList:
            myFile.write(f.name)
            myFile.write("\n")

elif choice == "4":
    file =input("what file would you like to see  ")
    with open(file, "r+") as myFileread:
        print(myFileread.read())