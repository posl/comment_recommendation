def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    s = [0]
    for x in a:
        s.append(s[-1] + x)
    s.append(0)
    # print(s)
    ans = 0
    for i in range(n+1):
        for j in range(i+1, n+2):
            if s[j] - s[i] >= k:
                # print(i, j, s[j] - s[i])
                ans += 1
    print(ans)
