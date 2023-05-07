def main():
    import sys
    from bisect import bisect_left
    input = sys.stdin.readline
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A.sort()
    for b in B:
        if bisect_left(A, b) == N or A[bisect_left(A, b)] != b:
            print("No")
            return
    print("Yes")

if __name__ == '__main__':
    main()