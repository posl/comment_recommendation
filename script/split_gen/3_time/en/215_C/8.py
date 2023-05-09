def main():
    S, K = input().split()
    K = int(K)
    S = list(S)
    S.sort()
    S = ''.join(S)
    ans = []
    def dfs(s, path):
        if not s:
            ans.append(path)
        for i in range(len(s)):
            if i > 0 and s[i] == s[i-1]:
                continue
            dfs(s[:i] + s[i+1:], path + s[i])
    dfs(S, '')
    print(ans[K-1])
