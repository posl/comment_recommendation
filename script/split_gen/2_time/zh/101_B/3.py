def problem101_b():
    n = int(input())
    s = sum([int(i) for i in str(n)])
    if n%s == 0:
        print("Yes")
    else:
        print("No")
