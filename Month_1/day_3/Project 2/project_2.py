#logic will be 
"""   
make a file names text.txt 
use read_text.txt to read the made wile 
convert the file into list
add a new task and update the list using WRITE
show the new file task.txt

 


"""
from pathlib import Path
file_path = Path(__file__)
folder = file_path.parent/"tasks.txt"

def load_task():
   
    read_file = folder.read_text()
    iteams = read_file.splitlines()
    return iteams

def add_task(tasks):
    new_task = input(f"Enter the Task you want to do:  ")
    if new_task in tasks:
        print("You already have this task scheduled")
    else:
        tasks.append(new_task)
   
            
    return tasks 
def update_list(tasks):
   in_string_task = "\n".join(tasks)
   new_file = folder.write_text(in_string_task)
   new_read_file = folder.read_text()
   return new_read_file


def main():
    print(load_task())
    tasks = load_task()
    print (add_task(tasks))
    print (update_list(tasks))
    
if __name__ == "__main__":
    main()