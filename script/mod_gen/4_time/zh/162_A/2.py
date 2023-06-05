def is_7(n):
    if n % 10 == 7:
        return True
    elif n // 10 == 0:
        return False
    else:
        return is_7(n // 10)
n = int(input())

if __name__ == '__main__':
    is_7()