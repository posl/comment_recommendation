def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    k = k % n
    i = 0
    while i < k:
        i += 1
        a = [a[a[j]-1] for j in range(n)]
    print(a[0])

if __name__ == '__main__':
    main()