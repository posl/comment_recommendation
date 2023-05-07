def main():
    a, b, c, d = map(int, input().split())
    if a > b * d:
        print(-1)
        return
    cnt = 0
    while a > b * d:
        a += b
        a -= c * d
        cnt += 1
    print(cnt)
