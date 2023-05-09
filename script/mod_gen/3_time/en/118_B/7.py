def main():
    n, m = map(int, input().split())
    ans = 0
    for _ in range(n):
        k, *a = map(int, input().split())
        ans |= 1 << (k - 1)
    print(bin(ans).count("1"))

if __name__ == '__main__':
    main()