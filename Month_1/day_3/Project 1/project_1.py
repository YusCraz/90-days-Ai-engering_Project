##Goal
##Build a small program that reads a text file and gives basic information about it.


#logic = stores data, python reads it , python process it , useful result






from pathlib import Path
current_dir = Path(__file__)
file_path = current_dir.parent / "notes.txt"
def load_notes():
    
    write = file_path.write_text("I am YUS \n MY anme is AAYUSH \n HEllow word \n Python is here")
    
    read = file_path.read_text()
    items = read.splitlines()
    return items 


def show_notes(notes):
    for note in notes:
        print (note)
        
def count_notes(notes):
    count = len(notes)
    return count


def main():
    load_notes()
    notes = load_notes()
    
    show_notes(notes)
    print(f"Total notes: {count_notes(notes)}")
   
    
    
if __name__ =="__main__":
    main()
    






















