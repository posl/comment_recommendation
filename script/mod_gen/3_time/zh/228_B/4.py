def main():
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    a[x - 1] = 0
    for i in range(n):
        if a[i] == x:
            a[i] = 0
    print(len(set(a)))

if __name__ == '__main__':
    main()