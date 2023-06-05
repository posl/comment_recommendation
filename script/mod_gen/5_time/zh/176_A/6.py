def problem176_a():
    n,x,t = map(int,input().split())
    print(((n-1)//x+1)*t)

if __name__ == '__main__':
    problem176_a()