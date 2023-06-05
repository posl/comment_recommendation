def solve():
    n = int(input())
    agree = 0
    for i in range(n):
        s = input()
        if s == "For":
            agree += 1
    if agree > n // 2:
        print("Yes")
    else:
        print("No")
