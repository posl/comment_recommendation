def main():
    n, a, b = map(int, input().split())
    if a+b == 0:
        print(0)
    else:
        print(a*(n//(a+b))+min(a, n%(a+b)))

if __name__ == '__main__':
    main()