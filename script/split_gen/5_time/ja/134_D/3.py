def main():
    N = int(input())
    a = list(map(int, input().split()))
    if N == 1:
        if a[0] == 0:
            print(1)
            print(1)
        else:
            print(-1)
        return
    if N == 2:
        if a[0] == 0 and a[1] == 0:
            print(2)
            print("1 2")
        elif a[0] == 1 and a[1] == 1:
            print(2)
            print("1 2")
        elif a[0] == 0 and a[1] == 1:
            print(2)
            print("1 2")
        elif a[0] == 1 and a[1] == 0:
            print(2)
            print("1 2")
        else:
            print(-1)
        return
    if a[0] == 1:
        print(-1)
        return
    if a[1] == 1:
        print(-1)
        return
    if a[0] == 0 and a[1] == 0:
        print(2)
        print("1 2")
        return
    if a[0] == 0 and a[1] == 1:
        print(-1)
        return
    if a[0] == 1 and a[1] == 0:
        print(-1)
        return
    if a[0] == 1 and a[1] == 1:
        print(-1)
        return
    print(N)
    for i in range(1, N+1):
        print(i)
