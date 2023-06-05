def problem222_b():
    n, p = map(int, input().split())
    a = list(map(int, input().split()))
    fail = 0
    for i in range(n):
        if a[i] < p:
            fail += 1
    print(fail)
