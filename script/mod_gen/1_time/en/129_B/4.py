def main():
    n = int(input())
    w = list(map(int, input().split()))
    min_diff = 100 * 100
    for t in range(1, n):
        s1 = sum(w[:t])
        s2 = sum(w[t:])
        diff = abs(s1 - s2)
        if diff < min_diff:
            min_diff = diff
    print(min_diff)

if __name__ == '__main__':
    main()