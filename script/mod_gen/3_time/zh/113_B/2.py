def main():
    N = int(input())
    T, A = map(int, input().split())
    H = list(map(int, input().split()))
    min_diff = 1000
    index = 0
    for i in range(N):
        diff = abs(A - (T - H[i] * 0.006))
        if diff < min_diff:
            min_diff = diff
            index = i + 1
    print(index)

if __name__ == '__main__':
    main()