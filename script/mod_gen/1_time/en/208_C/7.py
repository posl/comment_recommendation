def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    k = k % n
    for i in range(n):
        if i < k:
            print(n)
        else:
            print(n-1)

if __name__ == '__main__':
    main()