def main():
    N = int(input())
    S = []
    for i in range(N):
        S.append(input())
    print(S)
    from collections import Counter
    c = Counter(S)
    print(c)
    m = max(c.values())
    print(m)
    for k in sorted(k for k, v in c.items() if v == m):
        print(k)

if __name__ == '__main__':
    main()