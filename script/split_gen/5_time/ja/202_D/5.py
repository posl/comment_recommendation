def main():
    a,b,k = map(int,input().split())
    #print(a,b,k)
    ret = ""
    for i in range(a+b):
        if a == 0:
            ret += "b"
            b -= 1
        elif b == 0:
            ret += "a"
            a -= 1
        elif k <= 2**(a+b-1):
            ret += "a"
            a -= 1
        else:
            ret += "b"
            k -= 2**(a+b-1)
            b -= 1
    print(ret)
