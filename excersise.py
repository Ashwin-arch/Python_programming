student_pet_count_list=[0,1,2,3,4,5,7,6,3,2,12]
student_pet_count_list[2]=4
student_pet_count_list[3]=student_pet_count_list[3]+1
student_pet_count_list[-1]=student_pet_count_list[-1]+2
student_pet_count_list.append(4)
NUM_OF_STUDENTS=len(student_pet_count_list)
print(NUM_OF_STUDENTS)
SUM=0
for INDIVIDUAL_PET_COUNT in student_pet_count_list:
    SUM=SUM+INDIVIDUAL_PET_COUNT
print(SUM)
AVERAGE=SUM/NUM_OF_STUDENTS
print(AVERAGE)