def main():
    n = int(input())
    a = list(map(int, input().split()))
    d = [0] * n
    for i in range(n):
        d[(i-1) % n] += a[i]
        d[(i+1) % n] += a[i]
    print(*d)

if __name__ == '__main__':
    main()