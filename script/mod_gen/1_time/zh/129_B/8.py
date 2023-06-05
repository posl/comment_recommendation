def main():
    n = int(input())
    W = list(map(int, input().split()))
    min_diff = 1000
    for t in range(1, n):
        s1 = sum(W[0:t])
        s2 = sum(W[t:])
        diff = abs(s1 - s2)
        if diff < min_diff:
            min_diff = diff
    print(min_diff)

if __name__ == '__main__':
    main()