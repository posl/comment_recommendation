def main():
    s = input()
    n = len(s)
    ans = [0] * n
    for i in range(n):
        if s[i] == 'L':
            ans[i-1] += (n-i) // 2 + 1
            ans[i] += (n-i) // 2
        else:
            ans[i] += (i+1) // 2
            ans[i-1] += (i+1) // 2 + 1
    print(' '.join(map(str, ans)))
