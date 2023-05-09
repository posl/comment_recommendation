def main():
    n, m = map(int, input().split())
    a = [0] * m
    for _ in range(n):
        for i in map(int, input().split()[1:]):
            a[i - 1] += 1
    print(sum(1 for i in a if i == n))

if __name__ == '__main__':
    main()