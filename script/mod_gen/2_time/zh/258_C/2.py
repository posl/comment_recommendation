def problem258_c():
    n,q=map(int,input().split())
    s=input()
    for i in range(q):
        t,x=map(int,input().split())
        if t==1:
            s=s[-x:]+s[:-x]
        else:
            print(s[x-1])

if __name__ == '__main__':
    problem258_c()