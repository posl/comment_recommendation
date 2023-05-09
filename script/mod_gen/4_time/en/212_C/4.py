def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A.sort()
    B.sort()
    min_diff = 10**9
    for a in A:
        i = bisect.bisect_left(B, a)
        if i < M:
            min_diff = min(min_diff, abs(a - B[i]))
        if i > 0:
            min_diff = min(min_diff, abs(a - B[i-1]))
    print(min_diff)

if __name__ == '__main__':
    main()