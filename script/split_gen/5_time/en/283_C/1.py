def solve():
    s = int(input())
    count = 0
    while s > 0:
        if s % 100 == 0:
            s = s // 100
        elif s % 10 == 0:
            s = s // 10
        else:
            s -= 1
        count += 1
    print(count)
