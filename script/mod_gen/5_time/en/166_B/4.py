def main():
    n, k = map(int, input().split())
    s = set()
    for _ in range(k):
        d = int(input())
        a = set(map(int, input().split()))
        s |= a
    print(n - len(s))

if __name__ == '__main__':
    main()