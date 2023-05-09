def main():
    N = int(input())
    s = [input() for _ in range(N)]
    s.sort()
    ans = 0
    for i in range(N):
        for j in range(i + 1, N):
            if s[i] == s[j]:
                continue
            if sorted(s[i]) == sorted(s[j]):
                ans += 1
    print(ans)
