def solve():
    # +++ input +++
    n = int(input())
    s = [input() for _ in range(n)]
    # +++ solve +++
    # 1. dict
    d = {}
    for i in range(n):
        if s[i] in d:
            d[s[i]] += 1
        else:
            d[s[i]] = 1
    # 2. list
    # d = []
    # for i in range(n):
    #     d.append(s[i])
    # 3. Counter
    # d = Counter(s)
    # 4. defaultdict
    # d = defaultdict(int)
    # for i in range(n):
    #     d[s[i]] += 1
    # 5. Counter + max
    # d = Counter(s)
    # d = max(d, key=d.get)
    # 6. Counter + most_common
    # d = Counter(s)
    # d = d.most_common(1)[0][0]
    # +++ output +++
    print(max(d, key=d.get))

if __name__ == '__main__':
    solve()