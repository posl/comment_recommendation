def main():
    N, K = map(int, input().split())
    X = list(map(int, input().split()))
    # 1本のろうそくに火を付けるのに必要な最小の時間
    min_time = 10**9
    for i in range(N-K+1):
        left = X[i]
        right = X[i+K-1]
        time = min(abs(left), abs(right)) + abs(right-left)
        if time < min_time:
            min_time = time
    print(min_time)
