def check(a,b,c,d):
    if a>b or b>c or c>d:
        return False
    if sum(A[a:b])!=P:
        return False
    if sum(A[b:c])!=Q:
        return False
    if sum(A[c:d])!=R:
        return False
    return True

if __name__ == '__main__':
    check()