tasks = [
    {
        "name": "Networking Assignment",
        "course": "CS 3700",
        "hours": 3.0,
        "priority": 4
    },
    {
        "name": "Music Quiz",
        "course": "MUS 1000",
        "hours": 1.0,
        "priority": 2
    },
    {
        "name": "Linear Algebra Homework",
        "course": "MTH 3130",
        "hours": 2.5,
        "priority": 5
    },
    {
        "name": "Anthropology Discussion",
        "course": "ANT 2330",
        "hours": 1.5,
        "priority": 3
    }
]



def total_hour(tasks):
    
    total = sum(task['hours'] for task in tasks)
    return total

def avg_time(tasks):
    total_sum = total_hour(tasks)
    avg = total_sum / len (tasks)
    return avg
    
def higest_priority(tasks):
        higest = tasks[0]
        for task in tasks[1:]:
            if task['priority'] > higest ['priority']:
                higest = task
        return higest 
    
if __name__ == "__main__":
    print(f"Total workload: {total_hour(tasks):.2f}")
    print(f"Average task length: {avg_time(tasks):.2f} hr")
    
    higest = higest_priority(tasks)
    print(f"Highest priority:  {higest['name']} ({ higest ["course"]})")