def main():
    n = int(input())
    s = input()
    ans = 0
    for i in range(n):
        for j in range(i+1,n):
            for k in range(j+1,n):
                if s[i] != s[j] and s[i] != s[k] and s[j] != s[k]:
                    if j - i != k - j:
                        ans += 1
    print(ans)
