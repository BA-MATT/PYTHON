student_hght = [150,155,160,165,170,172,190,174,175,176,177,178,179,180]

count_student = len(student_hght)

sum_hght=0
# Sum of students heights
for student_hghts in student_hght:
    sum_hght+=student_hghts

max_hght=0
# Find tallest of students heights
for student_hghts in student_hght:
    if student_hghts>max_hght:
        max_hght=student_hghts

print (f"Number of Students: {count_student}")
print(f" Average height of Students {sum_hght/count_student}") 
print(f" Tallest Student height {max_hght}") 