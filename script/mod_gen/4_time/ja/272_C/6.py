def check_even(a):
    for i in range(len(a)):
        for j in range(i+1, len(a)):
            if (a[i] + a[j]) % 2 == 0:
                return True
    return False

if __name__ == '__main__':
    check_even()