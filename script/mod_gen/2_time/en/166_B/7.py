def main():
    n, k = map(int, input().split())
    snacks = set()
    for i in range(k):
        d = int(input())
        snacks.update(map(int, input().split()))
    print(n - len(snacks))

if __name__ == '__main__':
    main()