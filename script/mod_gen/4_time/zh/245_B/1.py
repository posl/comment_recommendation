def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    m = 1
    for i in range(n):
        if a[i] == m:
            m += 1
    print(m)

if __name__ == '__main__':
    main()