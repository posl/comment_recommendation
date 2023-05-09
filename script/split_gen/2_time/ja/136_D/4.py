def main():
    s = input()
    n = len(s)
    ans = [0] * n
    for i in range(n):
        if s[i] == 'R':
            ans[i+1] += 1
        else:
            ans[i-1] += 1
    for i in range(n):
        print(ans[i]//2, end=' ')
    print()
