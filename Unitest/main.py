

if __name__ == '__main__':
    try:
        assert 8 == 10, 'Error 8 is not equal 10'
        print(">>> it's equal")
    except AssertionError as error:
        print(error)
        