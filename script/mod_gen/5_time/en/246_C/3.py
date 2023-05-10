def main():
    n, k, x = map(int, input().split())
    a = list(map(int, input().split()))
    print(sum([min(x, a[i]) for i in range(n)]))

if __name__ == '__main__':
    main()