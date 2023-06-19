def problem124_a():
    a,b = map(int,input().split())
    if a == b:
        print(a+a)
    elif a > b:
        print(a+a-1)
    else:
        print(b+b-1)

if __name__ == '__main__':
    problem124_a()