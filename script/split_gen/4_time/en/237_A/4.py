def problems237_a():
    n = int(input())
    if -2**31 <= n and n <= 2**31-1:
        print("Yes")
    else:
        print("No")
