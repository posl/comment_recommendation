def judge7(n):
    if n%7==0:
        return True
    while n>0:
        if n%10==7:
            return True
        n=n//10
    return False

if __name__ == '__main__':
    judge7()