def main():
    n, k = map(int, input().split())
    s = input()
    s1 = s
    s2 = s[::-1]
    ans = 0
    for i in range(n-1):
        if s1[i] == s1[i+1]:
            ans += 1
        if s2[i] == s2[i+1]:
            ans += 1
    ans += min(ans//2+1, k)
    print(ans)
