def check(a,b):
    for i in range(len(a)):
        if a[i] != b[i]:
            return False
    return True

if __name__ == '__main__':
    check()