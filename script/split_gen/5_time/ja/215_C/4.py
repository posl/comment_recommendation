def main():
    s, k = input().split()
    k = int(k)
    s = sorted(s)
    print(s)
    ans = []
    ans.append(s[0])
    for i in range(1, len(s)):
        ans.append(s[i])
        ans.append(s[i - 1] + s[i])
    ans = sorted(list(set(ans)))
    print(ans)
    print(ans[k - 1])
