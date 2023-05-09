def main():
    n = int(input())
    w = list(map(int, input().split()))
    s1 = 0
    s2 = sum(w)
    min_diff = 1000000000
    for i in range(1, n):
        s1 += w[i - 1]
        s2 -= w[i - 1]
        diff = abs(s1 - s2)
        if diff < min_diff:
            min_diff = diff
    print(min_diff)

if __name__ == '__main__':
    main()