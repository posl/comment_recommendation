def main():
    n, k = map(int, input().split())
    p = list(map(int, input().split()))
    print(sum(sorted(p)[:k]))

if __name__ == '__main__':
    main()