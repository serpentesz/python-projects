def Process(written):
  amount_of_grades = input("input your grades, seperated by commas:\n")
  list_of_grades = amount_of_grades.split(',')
  all_exam_grades = [float(x.strip()) for x in list_of_grades]
  print(all_exam_grades)
#--// calculating
  if written == False:
      oral_grade = int(input("input your oral grade: "))
      all_grades = sum(all_exam_grades) / int(len(all_exam_grades))
      all_together_mark = all_grades * .5 + oral_grade * .5
  elif written == True:
      all_grades = sum(all_exam_grades) / int(len(all_exam_grades))
      all_together_mark = all_grades

#--// end
  print(all_together_mark)
  exit("done")

#--// vars
while True:
  type_of_grade = input("do you want to calculate your written or total grade (written / total):\n")
  if type_of_grade in ('written', 'total'):
    if type_of_grade == "total":
      Process(False)
    elif type_of_grade == "written":
      Process(True)