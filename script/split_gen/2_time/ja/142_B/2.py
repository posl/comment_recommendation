def main():
    N, K = map(int, input().split())
    H = list(map(int, input().split()))
    count = 0
    for i in range(N):
        if H[i] >= K:
            count += 1
    print(count)
