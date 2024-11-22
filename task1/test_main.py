import pytest
from main import sum_two, strict


# correct
def test_sum_two_correct_arguments():
    assert sum_two(1, 2) == 3


# incorrect 1
def test_sum_two_incorrect_first_argument():
    with pytest.raises(TypeError, match="Argument a expected <class 'int'>, got <class 'str'> instead."):
        sum_two("1", 2)


# incorrect 2
def test_sum_two_incorrect_second_argument():
    with pytest.raises(TypeError, match="Argument b expected <class 'int'>, got <class 'float'> instead."):
        sum_two(1, 2.5)


# correct with keyword
def test_sum_two_mixed_args_and_kwargs():
    assert sum_two(1, b=2) == 3


# iccorrect with keyword
def test_sum_two_incorrect_kwargs():
    with pytest.raises(TypeError, match="Argument b expected <class 'int'>, got <class 'str'> instead."):
        sum_two(1, b="2")
