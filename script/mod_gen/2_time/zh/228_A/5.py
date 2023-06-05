def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    print(a)
    print(n, k)

if __name__ == '__main__':
    main()