def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    if n < sum(a):
        print(-1)
    else:
        print(n - sum(a))

if __name__ == '__main__':
    main()