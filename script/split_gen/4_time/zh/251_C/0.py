def main():
    N = int(input())
    ts = []
    for i in range(N):
        s, t = input().split()
        t = int(t)
        ts.append((s, t, i + 1))
    ts.sort()
    max_s = None
    max_t = 0
    ans = 0
    for t in ts:
        if t[0] != max_s:
            max_s = t[0]
            max_t = t[1]
            ans = t[2]
        else:
            if t[1] > max_t:
                max_t = t[1]
                ans = t[2]
    print(ans)
