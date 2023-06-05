def main():
    n, d = map(int, input().split())
    cnt = 0
    for i in range(n):
        x, y = map(int, input().split())
        if x*x + y*y <= d*d:
            cnt += 1
    print(cnt)
