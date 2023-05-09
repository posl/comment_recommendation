def problem():
    x,y = map(int, input().split())
    if y % 2 == 0 and 2 * x <= y and y <= 4 * x:
        print("Yes")
    else:
        print("No")
problem()

if __name__ == '__main__':
    problem()