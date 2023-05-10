def main():
    N = int(input())
    T, A = map(int, input().split())
    H = list(map(int, input().split()))
    ans = 0
    min_diff = 100000000
    for i in range(N):
        tmp = T - H[i] * 0.006
        diff = abs(A - tmp)
        if diff < min_diff:
            min_diff = diff
            ans = i + 1
    print(ans)

if __name__ == '__main__':
    main()