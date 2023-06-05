def problem120_a():
    a,b,c = map(int,input().split())
    if a*c <= b:
        print(c)
    else:
        print(b//a)

if __name__ == '__main__':
    problem120_a()