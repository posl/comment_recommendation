def main():
    n=int(input())
    a=0
    b=0
    x=0
    while True:
        if n>=x:
            a+=1
            x=a**3+a**2*b+a*b**2+b**3
            if n<=x:
                break
        else:
            b+=1
            x=a**3+a**2*b+a*b**2+b**3
            if n<=x:
                break
    print(x)
