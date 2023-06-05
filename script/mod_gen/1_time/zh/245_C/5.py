def check(a,b,k):
    for i in range(len(a)):
        if abs(a[i]-b[i])>k:
            return False
    return True

if __name__ == '__main__':
    check()