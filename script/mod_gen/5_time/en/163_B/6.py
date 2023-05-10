def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort(reverse=True)
    print(n - sum(a) if n >= sum(a) else -1)

if __name__ == '__main__':
    main()