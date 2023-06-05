def isMultipleOf9(n):
    if (n == 0 or n == 9):
        return True
    if (n < 9):
        return False
    return isMultipleOf9(int(n/9) - int(n%9))
n = input()

if __name__ == '__main__':
    isMultipleOf9()