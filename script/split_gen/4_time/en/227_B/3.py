def main():
    n = int(input())
    s = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                if s[i] == s[j] == s[k]:
                    ans += 1
    print(ans)
