import lab2 as test

print("Test_Lab2")

def test_find_min_max():
    inp_list = [10, 12.5, 20.3, 15.8, 18.2]

    result = test.find_min_max(inp_list)

    assert (result == 10, 20.3)

def test_calc_average():
    inp_list = [10, 12.5, 20.3, 15.8, 18.2]

    result = test.calc_average(inp_list)

    assert (result == 15.36)

def test_calc_median_temperature():
    inp_list = [10, 12.5, 20.3, 15.8, 18.2]

    result = test.calc_median_temperature(inp_list)

    assert (result == 15.8 )