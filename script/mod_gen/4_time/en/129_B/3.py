def main():
    n = int(input())
    w = list(map(int, input().split()))
    min_diff = 1000
    for i in range(n):
        diff = abs(sum(w[:i+1]) - sum(w[i+1:]))
        if diff < min_diff:
            min_diff = diff
    print(min_diff)

if __name__ == '__main__':
    main()