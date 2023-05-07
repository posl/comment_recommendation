def poor(num1, num2, num3):
    if num1 == num2 and num1 != num3:
        return True
    elif num1 == num3 and num1 != num2:
        return True
    elif num2 == num3 and num2 != num1:
        return True
    else:
        return False

if __name__ == '__main__':
    poor()