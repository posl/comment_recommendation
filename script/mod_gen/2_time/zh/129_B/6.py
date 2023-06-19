def main():
    n = int(input())
    w = list(map(int, input().split()))
    diff = 100 * n
    for i in range(1, n):
        diff = min(diff, abs(sum(w[:i]) - sum(w[i:])))
    print(diff)

if __name__ == '__main__':
    main()