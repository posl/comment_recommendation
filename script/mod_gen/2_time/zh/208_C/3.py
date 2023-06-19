def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    d = k // n
    r = k % n
    for i in range(n):
        print(d + (1 if i < r else 0))

if __name__ == '__main__':
    main()