#from pathlib import Path

#script = Path(__file__)

#folder = script.parent/"shopping_list.txt"
#content = folder.read_text()
#print(content)



#also a example 
"""  
from pathlib import Path 

script = Path(__file__)## tells you where the python script is located


folder = script.parent## help you locate the folder where you .py file is 

file_path = folder / "shopping_list.txt" #now you have used that folder and looking for "shopping_list.txt" like you look soeming inside the dict 


content = file_path.read_text() ## using .read_text() to read waht i sinside the our final path .txt file 


print(content)  #will print that file after we read  it

"""

#you can also write the file liek you read it 
#important----> read_text() only read the file but write_terxt() erase all data with new data so i treplace it


"""  chainging file into list too

for example
content = file_path.read_text()

items= content.splitlines() ##now the file has converted to list and item is the list veriable 

and to check for length we can do either/
for intem in items:
    print(item)

or print(len(items))

"""


""" important syntax

Path
→ represents a filesystem path

Path.cwd()
→ current working directory

__file__
→ location of currently running Python script

Path(__file__)
→ turn script location into a Path object

.parent
→ containing folder

/
→ combine Path pieces

.read_text()
→ file → string

.write_text()
→ string → file

.splitlines()
→ multiline string → list of lines


"""

""" Logic:
import the path from path lib
then find the current runnogni script location
and relocate the script folder 
then use "/" to combine with our text 
read it 
convert it using splitlines




"""
"""
USed to read the file 

from pathlib import Path
file = Path(__file__)
folder = file.parent
content = folder/"practice.txt"
read = content.read_text()
print(read)
item = read.splitlines()
print(item)"""


"""
To write the file 


"""

from pathlib import Path 
file = Path(__file__)
folder = file.parent
text = file.parent/"goals.txt"
write = text.write_text("Learn Python \n Learn Machine Learnign \n Build AI system")
read = text.read_text()
iteams = read.splitlines()
print (iteams)
print(read)
print(write)
