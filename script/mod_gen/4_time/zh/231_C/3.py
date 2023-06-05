def main():
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    x = [int(input()) for _ in range(q)]
    a.sort()
    for i in range(q):
        j = 0
        while a[j] < x[i]:
            j += 1
        print(n - j)

if __name__ == '__main__':
    main()