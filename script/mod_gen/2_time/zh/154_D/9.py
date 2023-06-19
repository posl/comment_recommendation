def main():
    n, k = map(int, input().split())
    p = list(map(int, input().split()))
    p.sort()
    print(sum(p[-k:]) / 2 ** k)

if __name__ == '__main__':
    main()