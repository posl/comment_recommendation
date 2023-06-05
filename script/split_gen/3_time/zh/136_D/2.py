def main():
    s = input()
    n = len(s)
    ans = [0] * n
    for i in range(n):
        if s[i] == 'R':
            if i % 2 == 0:
                ans[i+1] += 1
            else:
                ans[i-1] += 1
        else:
            if i % 2 == 0:
                ans[i-1] += 1
            else:
                ans[i+1] += 1
    print(' '.join(map(str, ans)))
