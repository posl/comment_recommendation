def main():
    n = int(input())
    s = input()
    ans = 0
    for i in range(n):
        for j in range(i+1, n):
            if s[i] != s[j]:
                k = j + (j - i)
                if k < n and s[i] != s[k] and s[j] != s[k]:
                    ans += 1
    print(ans)
