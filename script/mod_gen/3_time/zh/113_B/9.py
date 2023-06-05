def main():
    N = int(input())
    T, A = map(int, input().split())
    H = list(map(int, input().split()))
    min_diff = 1000000
    min_diff_idx = 0
    for i in range(N):
        diff = abs(T - H[i] * 0.006 - A)
        if diff < min_diff:
            min_diff = diff
            min_diff_idx = i + 1
    print(min_diff_idx)

if __name__ == '__main__':
    main()