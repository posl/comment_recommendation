def main():
    n = int(input())
    a = 0
    b = 0
    for _ in range(n):
        a1, b1 = map(int, input().split())
        a += a1
        b += b1
    print((a + b - 1) // b - 1)

if __name__ == '__main__':
    main()