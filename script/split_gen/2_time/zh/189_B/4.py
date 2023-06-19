def main():
    n, x = map(int, input().split())
    x *= 100
    cnt = 0
    for i in range(n):
        v, p = map(int, input().split())
        cnt += v * p
        if cnt > x:
            print(i + 1)
            return
    print(-1)
