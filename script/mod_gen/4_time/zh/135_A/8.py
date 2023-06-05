def problems135_a():
    a,b = map(int,input().split())
    if a >= b:
        if (a-b)%2 == 0:
            print((a-b)//2 + b)
        else:
            print("IMPOSSIBLE")
    else:
        if (b-a)%2 == 0:
            print((b-a)//2 + a)
        else:
            print("IMPOSSIBLE")

if __name__ == '__main__':
    problems135_a()