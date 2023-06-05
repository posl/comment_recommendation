def problem176_a():
    n,x,t = map(int, input().split())
    print((n+x-1)//x*t)

if __name__ == '__main__':
    problem176_a()