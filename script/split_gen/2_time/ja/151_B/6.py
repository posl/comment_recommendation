def main():
    N, K, M = map(int, input().split())
    A = list(map(int, input().split()))
    total = sum(A)
    target = N * M
    if total >= target:
        print(0)
    elif total + K < target:
        print(-1)
    else:
        print(target - total)
