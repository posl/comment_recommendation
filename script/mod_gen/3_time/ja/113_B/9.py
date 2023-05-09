def main():
    n = int(input())
    T, A = map(int, input().split())
    H = list(map(int, input().split()))
    ans = 0
    min_diff = 1000000000
    for i in range(n):
        diff = abs(A-(T-H[i]*0.006))
        if diff < min_diff:
            ans = i + 1
            min_diff = diff
    print(ans)

if __name__ == '__main__':
    main()