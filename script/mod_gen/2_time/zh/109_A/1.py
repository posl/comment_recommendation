def check_odd(A, B):
    for i in range(1,4):
        if (A*B*i)%2 != 0:
            return True
    return False

if __name__ == '__main__':
    check_odd()