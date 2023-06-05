def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    print(n - sum(a) if n >= sum(a) else -1)

if __name__ == '__main__':
    main()