def check(a,b,x,k):
    for i in range(len(a)):
        if x[i] != a[i] and x[i] != b[i]:
            return False
        if i > 0 and abs(x[i] - x[i-1]) > k:
            return False
    return True

if __name__ == '__main__':
    check()