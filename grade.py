# Creates a text file containing the final average of all the grading 

a = "a students name, grade level and will calculate the average grade of the student"
creator = "Amazing Grace Cabiles\n"

print("\nThis program will store:", (a))
print("!!!! Always Follow the prompt of the program !!!!")
print("\nThis program was made by:", (creator))

def grade_program():
  print("\nEnter Full Name: \n")
  name = str(input())

  print("\nEnter Grade Level: \n")
  grade_level = int(input())

  print("\nEnter First Grading Average: \n")
  average_1 = int(input())

  print("\nEnter Second Grading Average: \n")
  average_2 = int(input())

  print("\nEnter Third Grading Average: \n")
  average_3 = int(input())

  print("\nEnter Fourth Grading Average: \n")
  average_4 = int(input())

  add_average = (average_1 + average_2 + average_3 + average_4)
  final_grade = ((add_average) // 4)
  print("\nAverage Grade = \n" , str(final_grade))
  print("\n Done!\n")

  write_grade = open(r"C:\Users\Amazing\Documents\Notepad files\Average Grade.txt", "a")

  write_grade.write("\nName: ")
  write_grade.write(str(name))
  write_grade.write("\nGrade Level: ")
  write_grade.write(str(grade_level))
  write_grade.write("\nAverage Grade: ")
  write_grade.write(str(final_grade))
  write_grade.write("\n")

  write_grade.close()

grade_program()