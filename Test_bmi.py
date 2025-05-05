import Lab2.bmi as bmi

print("Test_bmi")

def test_bmi_normal_weight():
    assert bmi.check_bmi(bmi.calculate_bmi(1.64,42.5)) == -1

    
    

def test_bmi_over_weight():
    assert bmi.check_bmi(bmi.calculate_bmi(1.7,60.5)) == 0



def test_bmi_under_weight():
    assert bmi.check_bmi(bmi.calculate_bmi(1.74,100.5)) == 1


    


