def main():
    N, K = map(int, input().split())
    H = list(map(int, input().split()))
    H.sort()
    if N <= K:
        print(0)
    else:
        print(sum(H[:N-K]))
