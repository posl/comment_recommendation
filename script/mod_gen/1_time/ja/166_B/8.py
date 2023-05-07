def main():
    n, k = map(int, input().split())
    a = [0 for _ in range(n + 1)]
    for _ in range(k):
        d = int(input())
        for i in map(int, input().split()):
            a[i] += 1
    print(a.count(0) - 1)

if __name__ == '__main__':
    main()