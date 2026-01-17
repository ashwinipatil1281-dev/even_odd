from number_check import check_number

def test_number_case1():
    expected_output = ("Prime", "Odd")
    assert check_number(7) == expected_output
