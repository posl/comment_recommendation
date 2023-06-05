def main():
    n, k = map(int, input().split())
    s = input()
    # print(n, k, s)
    # print(s.count('0'), s.count('1'))
    if s.count('0') <= k:
        print(n)
        return
    ans = 0
    for i in range(n):
        j = i
        while j < n and s[j] == '0':
            j += 1
        ans = max(ans, j - i)
        k -= 1
        if k < 0:
            break
    print(ans)
