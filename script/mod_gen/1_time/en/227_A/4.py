def main():
    n, k, a = map(int, input().split())
    a -= 1
    print((a + k) % n + 1)

if __name__ == '__main__':
    main()