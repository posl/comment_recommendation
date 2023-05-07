def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    if K >= N:
        print(0)
        return
    print(sum(A[:N-K]))
