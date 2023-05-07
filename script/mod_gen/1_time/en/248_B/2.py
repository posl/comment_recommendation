def main():
    a, b, k = map(int, input().split())
    n = 0
    while a < b:
        a *= k
        n += 1
    print(n)

if __name__ == '__main__':
    main()