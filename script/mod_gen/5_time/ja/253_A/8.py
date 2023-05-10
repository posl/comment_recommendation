def problem253_a():
    a,b,c = map(int,input().split())
    if a <= b <= c or c <= b <= a:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    problem253_a()