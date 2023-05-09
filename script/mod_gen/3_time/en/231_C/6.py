def main():
    import sys
    from bisect import bisect_right
    input = sys.stdin.readline
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    X = [int(input()) for _ in range(Q)]
    A.sort()
    for x in X:
        print(bisect_right(A, x))

if __name__ == '__main__':
    main()