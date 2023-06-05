def dfs(i, cnt, used, n, k, s):
    if i == n:
        return cnt == k
    if dfs(i + 1, cnt, used, n, k, s):
        return True
    for j in range(len(s[i])):
        if not used[ord(s[i][j]) - ord('a')]:
            used[ord(s[i][j]) - ord('a')] = True
            cnt += 1
    if dfs(i + 1, cnt, used, n, k, s):
        return True
    for j in range(len(s[i])):
        if not used[ord(s[i][j]) - ord('a')]:
            used[ord(s[i][j]) - ord('a')] = False
            cnt -= 1
    return False

if __name__ == '__main__':
    dfs()