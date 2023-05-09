def main():
    N, K = map(int, input().split())
    win = 0
    for i in range(1, N+1):
        count = 0
        while i < K:
            i *= 2
            count += 1
        win += 1/N * (1/2)**count
    print(win)
