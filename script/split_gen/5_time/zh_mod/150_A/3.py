def problem150_a():
    k, x = map(int, input().split())
    print("Yes" if k * 500 >= x else "No")
