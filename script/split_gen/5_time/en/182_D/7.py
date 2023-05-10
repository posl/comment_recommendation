def main():
    n = int(input())
    a = list(map(int,input().split()))
    s = [0]
    for i in range(n):
        s.append(s[i] + a[i])
    s.sort()
    ans = 0
    for i in range(n):
        ans = max(ans, s[i+1] - s[i])
    print(ans)
