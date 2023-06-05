def main():
    s = input()
    k = int(input())
    n = len(s)
    if k >= n:
        print(n)
        return
    ans = 0
    for i in range(n):
        if s[i] == 'X':
            ans += 1
    for i in range(k):
        if s[i] == 'X':
            ans -= 1
    for i in range(k, n):
        if s[i] == 'X':
            ans -= 1
        if s[i - k] == 'X':
            ans += 1
        if ans > k:
            ans = k
            break
    print(ans)
