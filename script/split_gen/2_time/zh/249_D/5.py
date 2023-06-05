def compute():
    n, k = map(int, input().split())
    s = [input() for _ in range(n)]
    ans = 0
    for i in range(1 << n):
        if bin(i).count("1") != k:
            continue
        st = set()
        for j in range(n):
            if i >> j & 1:
                for c in s[j]:
                    st.add(c)
        if len(st) == k:
            ans = max(ans, bin(i).count("1"))
    print(ans)
compute()
