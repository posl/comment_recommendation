def judge():
    a,b = map(int,input().split())
    if (a>=1 and a<=10) and (b>=1 and b<=10) and a<b:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    judge()