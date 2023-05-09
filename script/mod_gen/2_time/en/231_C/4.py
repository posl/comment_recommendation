def main():
    import sys
    input = sys.stdin.readline
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    X = [int(input()) for _ in range(Q)]
    A.sort()
    for x in X:
        print(len(A) - A.index(x) if x in A else len(A) - A.index(x) + 1)

if __name__ == '__main__':
    main()