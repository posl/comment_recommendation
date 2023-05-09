def main():
    N = int(input())
    t = [0] * N
    l = [0] * N
    r = [0] * N
    for i in range(N):
        t[i], l[i], r[i] = map(int, input().split())
    ans = 0
    for i in range(N):
        for j in range(i+1, N):
            if t[i] == 1:
                if t[j] == 1:
                    ans += (l[i] <= l[j] <= r[i]) or (l[j] <= l[i] <= r[j])
                elif t[j] == 2:
                    ans += (l[i] <= l[j] < r[i]) or (l[j] < l[i] <= r[j])
                elif t[j] == 3:
                    ans += (l[i] < l[j] <= r[i]) or (l[j] <= l[i] < r[j])
                elif t[j] == 4:
                    ans += (l[i] < l[j] < r[i]) or (l[j] < l[i] < r[j])
            elif t[i] == 2:
                if t[j] == 1:
                    ans += (l[i] < l[j] <= r[i]) or (l[j] <= l[i] < r[j])
                elif t[j] == 2:
                    ans += (l[i] < l[j] < r[i]) or (l[j] < l[i] < r[j])
                elif t[j] == 3:
                    ans += (l[i] < l[j] < r[i]) or (l[j] < l[i] < r[j])
                elif t[j] == 4:
                    ans += (l[i] < l[j] < r[i]) or (l[j] < l[i] < r[j])
            elif t[i] == 3:
                if t[j] == 1:
                    ans += (l[i] <= l[j] < r[i]) or (l[j] < l[i] <= r[j])
                elif t[j] == 2:
                    ans += (l[i] < l[j] < r[i]) or (l[j] < l[i] < r[j])
                elif t[j] == 3:
                    ans += (l[i] < l[j
