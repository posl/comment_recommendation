def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    total = sum(A)
    if total > N:
        print(-1)
    else:
        print(N - total)
