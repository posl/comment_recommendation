def main():
    import bisect
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    x = [int(input()) for _ in range(Q)]
    A.sort()
    for i in x:
        print(bisect.bisect_left(A, i))

if __name__ == '__main__':
    main()