def main():
    n, m = map(int, input().split())
    s = [input() for _ in range(n)]
    t = [input() for _ in range(m)]
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            for k in range(n):
                if k == i or k == j:
                    continue
                for l in range(n):
                    if l == i or l == j or l == k:
                        continue
                    x = s[i] + '_' + s[j] + '_' + s[k] + '_' + s[l]
                    if 3 <= len(x) <= 16 and x not in t:
                        print(x)
                        return
    print(-1)

if __name__ == '__main__':
    main()