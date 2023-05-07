def main():
    n = int(input())
    s = [0] * n
    t = [0] * n
    for i in range(n):
        s[i], t[i] = input().split()
    ans = "Yes"
    for i in range(n):
        for j in range(i + 1, n):
            if s[i] == s[j] or s[i] == t[j] or t[i] == s[j] or t[i] == t[j]:
                ans = "No"
    print(ans)
