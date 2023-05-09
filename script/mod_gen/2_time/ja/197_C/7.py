def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    b = 0
    for i in range(n):
        b |= a[i]
    print(b ^ a[0])

if __name__ == '__main__':
    main()