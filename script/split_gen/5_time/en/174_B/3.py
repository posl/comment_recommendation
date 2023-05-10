def main():
    N, D = map(int, input().split())
    cnt = 0
    for i in range(N):
        x, y = map(int, input().split())
        if x * x + y * y <= D * D:
            cnt += 1
    print(cnt)
