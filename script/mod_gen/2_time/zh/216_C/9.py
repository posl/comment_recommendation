def getA(n):
    if n==0:
        return ""
    elif n==1:
        return "A"
    elif n%2==0:
        return getA(n//2)+"B"
    else:
        return getA(n-1)+"A"

if __name__ == '__main__':
    getA()