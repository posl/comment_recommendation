def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    left = 0
    right = 10**12 + 1
    while right - left > 1:
        mid = (left + right) // 2
        if sum((a - 1) // mid for a in A) <= K:
            right = mid
        else:
            left = mid
    print(right)

if __name__ == '__main__':
    main()