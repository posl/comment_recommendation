def main():
    n, m = map(int, input().split())
    x = list(map(int, input().split()))
    x.sort()
    diff = [0] * (m - 1)
    for i in range(m - 1):
        diff[i] = x[i + 1] - x[i]
    diff.sort()
    print(sum(diff[:max(0, m - n)]))

if __name__ == '__main__':
    main()