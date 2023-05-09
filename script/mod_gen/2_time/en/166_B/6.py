def main():
    n, k = map(int, input().split())
    s = set()
    for i in range(k):
        d = int(input())
        for j in input().split():
            s.add(j)
    print(n - len(s))

if __name__ == '__main__':
    main()