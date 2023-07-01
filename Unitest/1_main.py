

# if __name__ == '__main__':
#     try:
#         assert 8 == 10, 'Error 8 is not equal 10'
#         print(">>> it's equal")
#     except AssertionError as error:
#         print(error)
        
# if __name__ == '__main__':
#     try:
#         assert 8 == 10, 'Error 8 is not equal 10'
#         print(">>> it's equal")


def sum(a: int, b: int) -> int:
    """sum two numbers

    args:
        a (int): first number
        b (int): second number

    Raises:
        AssertionError: if a and b are not equal

    Returns:
        int: sum of two numbers
    """

    assert a > 0 and b > 0, 'a and b must be positive'
    
    return a + b

if __name__ == '__main__':
    result = sum(-8, 10)
    print(result)
