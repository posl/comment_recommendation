def main():
    n, k = map(int, input().split())
    d = [0] * n
    for i in range(k):
        for j in map(int, input().split()[1:]):
            d[j - 1] += 1
    print(d.count(0))

if __name__ == '__main__':
    main()