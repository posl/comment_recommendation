def main():
    x, a, d, n = map(int, input().split())
    cnt = 0
    if d == 0:
        if x != a:
            cnt = 2
        else:
            cnt = 0
    elif n == 1:
        if x != a:
            cnt = 2
        else:
            cnt = 0
    else:
        if (x - a) % d == 0:
            cnt = 0
        else:
            cnt = 2
    print(cnt)
