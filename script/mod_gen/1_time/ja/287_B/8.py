def main():
    n, m = map(int, input().split())
    s = [input() for _ in range(n)]
    t = [input() for _ in range(m)]
    print(sum(s.count(t[-3:]) for t in t))

if __name__ == '__main__':
    main()