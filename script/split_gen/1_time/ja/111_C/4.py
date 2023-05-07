def main():
    n = int(input())
    v = list(map(int,input().split()))
    cnt = [0]*(10**5+1)
    for i in range(n):
        cnt[v[i]] += 1
    cnt.sort(reverse=True)
    ans = 0
    ans += cnt[0]
    ans += cnt[1]
    ans = n-ans
    print(ans)
