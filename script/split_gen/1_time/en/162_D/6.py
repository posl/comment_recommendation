def main():
    n = int(input())
    s = input()
    ans = 0
    for i in range(n-2):
        for j in range(i+1,n-1):
            if s[i] != s[j]:
                for k in range(j+1,n):
                    if s[i] != s[k] and s[j] != s[k] and j-i != k-j:
                        ans += 1
    print(ans)
