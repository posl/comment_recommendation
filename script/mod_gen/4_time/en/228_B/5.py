def main():
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    a = [i - 1 for i in a]
    b = [False] * n
    b[x - 1] = True
    for i in range(n):
        if b[i]:
            b[a[i]] = True
    print(sum(b))

if __name__ == '__main__':
    main()