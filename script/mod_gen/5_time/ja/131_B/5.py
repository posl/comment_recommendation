def main():
    N, L = map(int, input().split())
    total = 0
    min_diff = 10**10
    for i in range(N):
        total += L + i
        if abs(L + i) < abs(min_diff):
            min_diff = L + i
    print(total - min_diff)

if __name__ == '__main__':
    main()