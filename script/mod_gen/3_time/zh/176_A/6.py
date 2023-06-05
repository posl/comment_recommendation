def problem176_a():
    n,x,t = map(int,input().split())
    if n%x == 0:
        print((n//x)*t)
    else:
        print(((n//x)+1)*t)

if __name__ == '__main__':
    problem176_a()