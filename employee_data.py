employee_data = [
    {"name":"Ruici","age":17,"department":"Sales","salary":50000},
    {"name": "Greg", "age": 25, "department": "Marketing", "salary": 60000},
    {"name": "Mary", "age": 23, "department": "Marketing", "salary": 56000},
    {"name": "Chloe",  "age": 35, "department": "Engineering", "salary": 70000},
    {"name": "Alex", "age": 32, "department": "Engineering", "salary": 65000},
    {"name": "Lucas", "age": 40, "department": "Sales", "salary": 60000}
    ]

def diplay_all_records():
    print(("Name"+"\t"+"Age"+"\t"+"Department"+"\t"+"salary").expandtabs(15))
    for i in employee_data:
        print((i["name"]+"\t"+str(i["age"])+"\t"+i["department"]+"\t"+str(i["salary"])).expandtabs(15))

def calculate_average_salary():
    total = 0
    average = 0
    for i in employee_data:
        total+=i["salary"]
    average = total / len(employee_data)

    return round(average,2)

def get_employee_by_age_range(age_upper_limit,age_lower_limit):
    result=[]
    for i in employee_data:
        if int(i["age"])>int(age_lower_limit) and int(i["age"])<int(age_upper_limit):
            result.append(i)
    return result

def display_records(employee_info):
    print(("Name"+"\t"+"Age"+"\t"+"Department"+"\t"+"Salary").expandtabs(15))
    for i in employee_info:
            
        print((i["name"]+"\t"+str(i["age"])+"\t"+i["department"]+"\t"+str(i["salary"])).expandtabs(15))
        
def get_employee_in_dept(department):
    result=[]
    for i in employee_data:
        if i["department"] ==department:
            result.append(i)
    return department






def display_main_menu():
    print("\nEmployee information Tracker")

    print("Select option\n")

    print("1. Display record")
    print("2. Display average salary")
    print("3. Display employee within certain age")
    print("4. Display employee in a department")

    print("N - exit")

    option = input("Enter selection: ")

    if option == '1':
        diplay_all_records()
    elif option == '2':
        average_salary = calculate_average_salary()
        print("Average salary = "+str(average_salary))

    elif option == '3':
        age_upper_limit=input("Enter age upper range: ")
        age_lower_limit=input("Enter age lower range: ")
        employee_info=get_employee_by_age_range(age_upper_limit,age_lower_limit)
        display_records(employee_info)


    elif option == '4':
        department=input("Enter Department: ")
        employee_info = get_employee_in_dept(department)
        display_records(employee_info)



    elif option == 'N':
        quit()




def main():
    while(True):
        display_main_menu()


if __name__ == "__main__":
    main()