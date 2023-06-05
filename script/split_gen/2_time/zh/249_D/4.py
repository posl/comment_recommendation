def get_ans(n, k, s):
    ans = 0
    for i in range(1<<n):
        if bin(i).count('1') != k:
            continue
        tmp = set()
        for j in range(n):
            if i & (1<<j):
                for c in s[j]:
                    tmp.add(c)
        if len(tmp) == k:
            ans = max(ans, bin(i).count('1'))
    return ans
