def main():
    N = int(input())
    T, A = map(int, input().split())
    H = list(map(int, input().split()))
    ans = 0
    min_diff = abs(A - (T - H[0] * 0.006))
    for i in range(1, N):
        diff = abs(A - (T - H[i] * 0.006))
        if diff < min_diff:
            min_diff = diff
            ans = i
    print(ans + 1)

if __name__ == '__main__':
    main()