def main():
    N = int(input())
    a = list(map(int, input().split()))
    if N == 1:
        if a[0] == 0:
            print(1)
            print(1)
        else:
            print(-1)
    elif N == 2:
        if a[0] == 0 and a[1] == 0:
            print(2)
            print(1, 2)
        elif a[0] == 1 and a[1] == 0:
            print(1)
            print(2)
        elif a[0] == 0 and a[1] == 1:
            print(1)
            print(1)
        else:
            print(-1)
    else:
        if a[0] == 1 and a[1] == 1 and a[2] == 1:
            print(-1)
        elif a[0] == 0 and a[1] == 1 and a[2] == 1:
            print(1)
            print(1)
        elif a[0] == 1 and a[1] == 0 and a[2] == 1:
            print(1)
            print(2)
        elif a[0] == 1 and a[1] == 1 and a[2] == 0:
            print(1)
            print(3)
        elif a[0] == 0 and a[1] == 0 and a[2] == 1:
            print(2)
            print(1, 2)
        elif a[0] == 0 and a[1] == 1 and a[2] == 0:
            print(2)
            print(1, 3)
        elif a[0] == 1 and a[1] == 0 and a[2] == 0:
            print(2)
            print(2, 3)
        elif a[0] == 0 and a[1] == 0 and a[2] == 0:
            print(3)
            print(1, 2, 3)
        else:
            print(-1)
