def main():
    import sys
    input = sys.stdin.readline
    N, K = map(int, input().split())
    H = list(map(int, input().split()))
    H.sort()
    if N <= K:
        print(0)
    else:
        print(sum(H[:N-K]))
