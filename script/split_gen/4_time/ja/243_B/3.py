def solve(n, a, b):
    cnt1 = 0
    cnt2 = 0
    for i in range(n):
        if a[i] == b[i]:
            cnt1 += 1
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            if a[i] == b[j]:
                cnt2 += 1
    return (cnt1, cnt2//2)
