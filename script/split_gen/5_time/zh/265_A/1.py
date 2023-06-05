def main():
    x, y, n = map(int, input().split())
    cnt = 0
    for i in range(1, n+1):
        if i % 3 == 0:
            cnt += y
        else:
            cnt += x
    print(cnt)
