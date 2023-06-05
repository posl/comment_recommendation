def main():
    s = input()
    n = len(s)
    ans = [0] * n
    #print(ans)
    cnt = 0
    for i in range(n):
        if s[i] == 'R':
            cnt += 1
            if i == n - 1:
                ans[i] += cnt
        else:
            ans[i] += cnt
            cnt = 0
    #print(ans)
    cnt = 0
    for i in range(n - 1, -1, -1):
        if s[i] == 'L':
            cnt += 1
            if i == 0:
                ans[i] += cnt
        else:
            ans[i] += cnt
            cnt = 0
    print(' '.join(map(str, ans)))
