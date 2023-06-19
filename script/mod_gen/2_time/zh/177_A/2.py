def problem177_a():
    D, T, S = map(int, input().split())
    if D / S <= T:
        print("Yes")
    else:
        print("No")
problem177_a()
