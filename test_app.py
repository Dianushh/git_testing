from app import sum_numbers

def test_sum():
    assert sum_numbers(2, 3) == 5
    assert sum_numbers(-1, 1) == 0