def main():
    n = int(input())
    s = [input() for i in range(n)]
    ans = 0
    for i in range(10):
        for j in range(1,n):
            if s[0][i:] == s[j][i:]+s[j][:i]:
                break
        else:
            ans += 1
    print(ans)
