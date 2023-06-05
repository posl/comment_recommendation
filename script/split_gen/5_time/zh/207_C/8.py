def solve():
    n = int(input())
    tlr = []
    for i in range(n):
        t, l, r = map(int, input().split())
        tlr.append((t, l, r))
    ans = 0
    for i in range(n):
        for j in range(i+1, n):
            t1, l1, r1 = tlr[i]
            t2, l2, r2 = tlr[j]
            if t1 == 1:
                if t2 == 1 or t2 == 2:
                    if l1 <= l2 <= r1:
                        ans += 1
                if t2 == 3:
                    if l1 <= l2 < r1:
                        ans += 1
            if t1 == 2:
                if t2 == 1:
                    if l2 <= l1 <= r2:
                        ans += 1
                if t2 == 2:
                    if l1 <= l2 <= r1 or l2 <= l1 <= r2:
                        ans += 1
                if t2 == 3:
                    if l2 <= l1 < r2:
                        ans += 1
            if t1 == 3:
                if t2 == 1:
                    if l2 <= l1 < r2:
                        ans += 1
                if t2 == 2:
                    if l2 <= l1 <= r2:
                        ans += 1
                if t2 == 3:
                    if l1 <= l2 <= r1 or l2 <= l1 <= r2:
                        ans += 1
    print(ans)
