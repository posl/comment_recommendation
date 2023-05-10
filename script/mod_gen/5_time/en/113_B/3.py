def main():
    N = int(input())
    T, A = [int(i) for i in input().split()]
    H = [int(i) for i in input().split()]
    min_diff = 1000000000
    min_index = -1
    for i in range(N):
        diff = abs(A - (T - H[i] * 0.006))
        if diff < min_diff:
            min_diff = diff
            min_index = i + 1
    print(min_index)

if __name__ == '__main__':
    main()