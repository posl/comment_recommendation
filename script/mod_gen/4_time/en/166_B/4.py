def main():
    n, k = map(int, input().split())
    d = [0] * n
    for _ in range(k):
        for a in map(int, input().split()):
            d[a - 1] += 1
    print(sum(1 for i in range(n) if d[i] == 0))

if __name__ == '__main__':
    main()