def main():
    L, Q = map(int, input().split())
    query = []
    for _ in range(Q):
        c, x = map(int, input().split())
        query.append((c, x))
    query.reverse()
    ans = []
    ans.append(L)
    for c, x in query:
        if c == 1:
            ans.append(min(x, ans[-1] - x))
        else:
            ans.append(min(x, ans[-1]))
    ans.reverse()
    for i in range(1, Q + 1):
        print(ans[i])

if __name__ == '__main__':
    main()