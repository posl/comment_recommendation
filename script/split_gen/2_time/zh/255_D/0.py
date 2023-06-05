def main():
    x, a, d, n = map(int, input().split())
    cnt = 0
    while x != a:
        if x > a:
            x -= 1
        else:
            x += 1
        cnt += 1
    print(cnt)
