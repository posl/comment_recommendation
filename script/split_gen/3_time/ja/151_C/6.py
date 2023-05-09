def main():
    N,M = map(int,input().split())
    p = [0 for i in range(N)]
    s = [0 for i in range(N)]
    for i in range(M):
        a,b = input().split()
        p[int(a)-1] += 1
        s[int(a)-1] += 1 if b == "AC" else 0
    ans = 0
    ans2 = 0
    for i in range(N):
        if s[i] > 0:
            ans += 1
            ans2 += p[i] - s[i]
    print(ans,ans2)
