def main():
    s = input()
    n = len(s)
    cnt = 0
    ans = [0] * n
    for i in range(n):
        if s[i] == 'L':
            cnt += 1
        else:
            ans[i] += cnt // 2
            ans[i - 1] += (cnt + 1) // 2
            cnt = 0
    print(*ans)
