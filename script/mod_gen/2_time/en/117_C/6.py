def main():
    from bisect import bisect_left
    N, M = map(int, input().split())
    X = sorted(map(int, input().split()))
    if N >= M:
        print(0)
        return
    diff = [X[i + 1] - X[i] for i in range(M - 1)]
    diff.sort()
    print(sum(diff[:M - N]))
main()

if __name__ == '__main__':
    main()