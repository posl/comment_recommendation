def main():
    a, b, q = map(int, input().split())
    s = [-10**15] + [int(input()) for _ in range(a)] + [10**15]
    t = [-10**15] + [int(input()) for _ in range(b)] + [10**15]
    x = [int(input()) for _ in range(q)]
    for i in range(q):
        ans = 10**15
        for j in range(a + 2):
            if s[j] >= x[i]:
                break
        for k in range(b + 2):
            if t[k] >= x[i]:
                break
        for l in range(j - 1, j + 1):
            for m in range(k - 1, k + 1):
                ans = min(ans, max(s[l] - x[i], x[i] - t[m]))
                ans = min(ans, max(t[m] - x[i], x[i] - s[l]))
        print(ans)
main()

if __name__ == '__main__':
    main()