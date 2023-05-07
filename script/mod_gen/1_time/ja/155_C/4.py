def main():
    N = int(input())
    S = [input() for _ in range(N)]
    d = {}
    for s in S:
        if s in d:
            d[s] += 1
        else:
            d[s] = 1
    ans = []
    max_cnt = max(d.values())
    for k, v in d.items():
        if v == max_cnt:
            ans.append(k)
    ans.sort()
    for a in ans:
        print(a)

if __name__ == '__main__':
    main()