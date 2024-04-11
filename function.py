#more readable code

#print
# def find_grade(marks):
#   if marks >= 80:
#      print("A+")
#   elif marks >= 70:
#      print("A")
#   elif marks >= 60:
#      print("B+")
#   else:
#      print("F")

# marks = input()
# marks = int(marks)
# find_grade(marks)

#return
def find_grade(marks):
  if marks >= 80:
     return("A+")
  elif marks >= 70:
     return("A")
  elif marks >= 60:
     return("B+")
  else:
     return("F")

mark= input()
mark = int(mark)
grade = find_grade(mark)
print("Your grade is", grade)

