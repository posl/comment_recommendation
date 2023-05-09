def main():
    n = int(input())
    t = []
    l = []
    r = []
    for i in range(n):
        t_, l_, r_ = map(int, input().split())
        t.append(t_)
        l.append(l_)
        r.append(r_)
    ans = 0
    for i in range(n):
        for j in range(i+1, n):
            if t[i] == 1:
                if t[j] == 1:
                    if l[i] <= l[j] <= r[i] or l[i] <= r[j] <= r[i] or l[j] <= l[i] <= r[j] or l[j] <= r[i] <= r[j]:
                        ans += 1
                elif t[j] == 2:
                    if l[i] <= l[j] <= r[i] or l[i] <= r[j] <= r[i] or l[j] < l[i] <= r[j] or l[j] < r[i] <= r[j]:
                        ans += 1
                elif t[j] == 3:
                    if l[i] < l[j] <= r[i] or l[i] < r[j] <= r[i] or l[j] <= l[i] < r[j] or l[j] <= r[i] < r[j]:
                        ans += 1
                else:
                    if l[i] < l[j] <= r[i] or l[i] < r[j] <= r[i] or l[j] < l[i] < r[j] or l[j] < r[i] < r[j]:
                        ans += 1
            elif t[i] == 2:
                if t[j] == 1:
                    if l[i] <= l[j] <= r[i] or l[i] <= r[j] <= r[i] or l[j] <= l[i] <= r[j] or l[j] <= r[i] <= r[j]:
                        ans += 1
                elif t[j] == 2:
                    if l[i] <= l[j] <= r[i] or l[i] <= r[j] <= r[i] or l[j] < l[i] <= r[j] or l[j] < r[i] <= r[j]:
                        ans += 1
                elif t[j] == 3:
                    if l[i] < l[j] <= r[i]
