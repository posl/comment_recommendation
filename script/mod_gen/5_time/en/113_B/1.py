def main():
    N = int(input())
    T, A = map(int, input().split())
    H = list(map(int, input().split()))
    min_diff = 100000000
    min_diff_index = 0
    for i in range(N):
        diff = abs(A - (T - H[i] * 0.006))
        if diff < min_diff:
            min_diff = diff
            min_diff_index = i + 1
    print(min_diff_index)

if __name__ == '__main__':
    main()