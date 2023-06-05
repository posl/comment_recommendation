def problem265_a():
    x,y,n = map(int,input().split())
    if n%3 == 0:
        print(n//3*y)
    elif n%3 == 1:
        print((n//3)*y+x)
    else:
        print((n//3)*y+y)

if __name__ == '__main__':
    problem265_a()