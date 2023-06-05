def main():
    s = input()
    k = int(input())
    n = len(s)
    l = []
    cnt = 0
    for i in range(n):
        if s[i] == "X":
            cnt += 1
        else:
            l.append(cnt)
            cnt = 0
    l.append(cnt)
    m = len(l)
    ans = 0
    if m <= 2 * k + 1:
        ans = n
    else:
        for i in range(m - 2 * k):
            tmp = sum(l[i:i + 2 * k + 1]) + k
            ans = max(ans, tmp)
    print(ans)
