# create_employees_file.py

def write_employees_to_file(file_name):
    employees = [
        {"name": "John Doe", "age": 30, "salary": 50000},
        {"name": "Jane Smith", "age": 25, "salary": 60000},
        {"name": "Bob Johnson", "age": 35, "salary": 55000},
    ]
    
    with open(file_name, 'w') as file:
        for employee in employees:
            file.write(f"{employee['name']}, {employee['age']}, {employee['salary']}\n")

write_employees_to_file('employee.txt')
