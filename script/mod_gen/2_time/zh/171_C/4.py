def main():
    n, k = map(int, input().split())
    p = sorted(map(int, input().split()))
    print(sum(p[:k]))

if __name__ == '__main__':
    main()