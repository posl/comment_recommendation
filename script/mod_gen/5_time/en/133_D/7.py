def main():
    n = int(input())
    a = list(map(int, input().split()))
    k = 0
    for i in range(n):
        k ^= a[i]
    for i in range(n):
        print(a[i] ^ k, end=' ')

if __name__ == '__main__':
    main()