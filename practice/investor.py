student_name = input("Enter your Name: ")
Age = input("Enter your Age: ")
Gender = input("Enter your Gender: ")
Phone_number = input("Enter your Phone_number: ")
Email_address = input("Enter your Email_address: ")


print(f'Student_name: {student_name}, Age: {Age}, Gender: {Gender}, Phone_number: {Phone_number}, Email_address: {Email_address}')



def student_info():
    student_name = input("Enter your Name: ")
    Age = int(input("Enter your Age: "))
    Gender = input("Enter your Gender: ")
    Phone_number = input("Enter your Phone_number: ")
    Email_address = input("Enter your Email_address: ")

    student_file = {
        'name': student_name,
        'age': Age,
        'gender': Gender,
        'Phone_number': Phone_number,
        'Email_address': Email_address,
    }

    return student_name, Age, Gender, Phone_number, Email_address