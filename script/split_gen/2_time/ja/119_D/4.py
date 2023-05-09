def main():
    A,B,Q = map(int,input().split())
    s = []
    t = []
    x = []
    for i in range(A):
        s.append(int(input()))
    for i in range(B):
        t.append(int(input()))
    for i in range(Q):
        x.append(int(input()))
    for i in range(Q):
        ans = 10**10
        for j in range(A):
            for k in range(B):
                if s[j] <= x[i] <= t[k]:
                    ans = min(ans, max(x[i] - s[j], t[k] - x[i]) + t[k] - s[j])
                elif x[i] < s[j]:
                    ans = min(ans, s[j] - x[i] + t[k] - s[j])
                elif t[k] < x[i]:
                    ans = min(ans, x[i] - t[k] + t[k] - s[j])
        print(ans)
