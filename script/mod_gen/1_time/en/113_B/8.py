def main():
    # read data
    N = int(input())
    T, A = map(int, input().split())
    H = list(map(int, input().split()))
    # solve
    ans = 1
    min_diff = abs(T - H[0] * 0.006 - A)
    for i in range(1, N):
        diff = abs(T - H[i] * 0.006 - A)
        if diff < min_diff:
            ans = i + 1
            min_diff = diff
    # output
    print(ans)

if __name__ == '__main__':
    main()