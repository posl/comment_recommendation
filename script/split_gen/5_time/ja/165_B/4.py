def solve():
    x = int(input())
    y = 100
    cnt = 0
    while y < x:
        y = int(y * 1.01)
        cnt += 1
    print(cnt)
