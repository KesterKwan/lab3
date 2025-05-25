import employee_info as employee

def test_get_employee_by_age_range():
    data=[   
        {"name":"Ruici","age":17,"department":"Sales","salary":50000}
        ]
    result=employee.get_employee_by_age_range(15,20)
    assert(result == data)

def test_calculate_average_salary():
    average=employee.calculate_average_salary()
    result=59500
    assert(result==average) 

def test_get_employee_by_dept():
    data=[   
        {"name":"Ruici","age":17,"department":"Sales","salary":50000},
        {"name": "John", "age": 30, "department":"Sales", "salary": 50000}
        ]
    result=employee.get_employee_in_dept('Sales')
    assert(result==data)
