def problems144_a():
    a,b = map(int,input().split())
    if a > 9 or b > 9:
        print(-1)
    else:
        print(a*b)

if __name__ == '__main__':
    problems144_a()