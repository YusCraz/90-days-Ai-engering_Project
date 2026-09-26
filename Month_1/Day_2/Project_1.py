## PRoject Student grade Tracker
## class will be class Student:
# student attribute in __INIT__ are name course grades
# methods are add_grade()
#calculate_average()
#get_highest_grade()


class Student:
    def __init__(self, name, course, grade):
        self.name = name
        self.course = course
        self.grade = grade
        
    def add_grade(self):
        grade = int((input(f"Enter your Grade you want to input: ")))
        self.grade.append(grade)
        return self.grade
    
    def avg_grade(self):
        avg = sum(self.grade) / len(self.grade)
        return avg
    
    def highest_grade(self):
        highest = self.grade[0] #setting the counter as 1st indext then we compare in for loop
        for grade in self.grade[1:]:
            if grade > highest:
                highest = grade
        return highest
    
    
    
    
    
def main():
        student = Student("Aayush", "CS 3700", [85, 92, 78])
        print(f"Your total grade are {student.add_grade()}")
        print(f"Your Average grade is: {student.avg_grade():.2f}")
        print(f"Your higest grade is: {student.highest_grade()}")
if __name__== "__main__":
    main()