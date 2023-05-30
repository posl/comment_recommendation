def main():
    N = int(input())
    p = list(map(int, input().split()))
    q = [0]*N
    for i in range(N):
        q[p[i]] = i
    ans = 0
    cnt = 0
    for i in range(N):
        if q[i] > cnt:
            cnt = q[i]
        else:
            ans += 1
    print(ans)
    
main()
