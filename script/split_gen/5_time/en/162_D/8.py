def main():
    n = int(input())
    s = input()
    ans = 0
    for i in range(n):
        for j in range(i+1,n):
            k = 2*j - i
            if k < n and s[i] != s[j] and s[j] != s[k] and s[k] != s[i]:
                ans += 1
    print(ans)
