def floor(a,b):
    if a%b==0:
        return a//b
    else:
        return (a-a%b)//b
a,b,n=map(int,input().split())

if __name__ == '__main__':
    floor()