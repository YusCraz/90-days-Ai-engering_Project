#import json
#text = '{"name":"YUS", "age":22}'
#student = json.loads(text)
#print(student["age"])


#import json

##def get_username(text):
 ##  username = converted["username"]
  #  return username    




#data = '{"username": "YUS", "level": 5}'

#print(get_username(data))



#import json
#def convert_to_json(student):
#    converted = json.dumps(student)
#    return converted
    
    
#student = {"name":"YUS", "level": 6 }

#print(convert_to_json(student))


#import json
#from pathlib import Path

#def save_student(student):
#    file_path = Path(__file__).parent / "student.json"
#    text = json.dumps(student, indent=4)
#    file_path.write_text(text)
    
  


#student = {
#    "name": "YUS",
##    "level": 6,
 #   "skills": ["Python", "JSON"]
#}

#save_student(student)

import json
from pathlib import Path

#def load_student():
#    file_path = Path(__file__).parent / "student.json"
#    read = file_path.read_text()
#    convert = json.loads(read)
#    return convert
    
#student = load_student()
#print(student["name"])
#print(student["skills"])


#============
## Project 2 
#============
import json
from pathlib import Path
file_path = Path(__file__).parent / "hunter.json"

def complete_quest(hunter, quest_name, reward):
    ## we need to add the quest 
    #so we gona ask the user waht he did 
    
    
    if quest_name not in hunter["completed_quests"]:
        hunter["completed_quests"].append(quest_name)
        hunter["xp"] += reward
    else:
        
        print("You hav alredy done that quest")
    
    return hunter 
    
def save_hunter(hunter):
    convert = json.dumps(hunter)
    saving = file_path.write_text(convert)
    return saving
    
def load_hunter():
    read = file_path.read_text()
    converted_dict = json.loads(read)
    return converted_dict

def main():
    hunter = {
        "name": "YUS",
        "xp": 0,
        "completed_quests": []
    }
    
    complete_quest(hunter , "Learn JSON", 50)
    complete_quest(hunter, "Learn Python", 100)
    save_hunter(hunter)
    print(load_hunter())
    

if __name__ == "__main__":
    main()