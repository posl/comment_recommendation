def main():
    s = input()
    n = len(s)
    ans = [0] * n
    ans[0] = 1
    ans[-1] = 1
    for i in range(n):
        if s[i] == 'R':
            ans[i+1] += ans[i]
            ans[i] = 0
        else:
            ans[i-1] += ans[i]
            ans[i] = 0
    print(*ans)
