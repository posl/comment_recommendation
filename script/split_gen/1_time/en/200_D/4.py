def  main():
    n = int(input())
    a = list(map(int, input().split()))
    b = {}
    for i in range(n):
        b[a[i] % 200] = i + 1
    for i in range(n):
        if b[(a[i] % 200)] != i + 1:
            print("Yes")
            print("1", i + 1)
            print("1", b[(a[i] % 200)])
            return
    print("No")
