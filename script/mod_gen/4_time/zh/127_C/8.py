def main():
    #N张ID卡，M个闸门
    N, M = map(int, input().split())
    #N张ID卡可以通过的闸门的范围
    L = []
    R = []
    for i in range(M):
        l, r = map(int, input().split())
        L.append(l)
        R.append(r)
    #每张ID卡可以通过的闸门的数量
    num = [0] * (N+1)
    for i in range(M):
        num[L[i]-1] += 1
        num[R[i]] -= 1
    #前缀和
    for i in range(1, N):
        num[i] += num[i-1]
    #通过所有闸门的ID卡数量
    ans = 0
    for i in range(N):
        if num[i] == M:
            ans += 1
    print(ans)

if __name__ == '__main__':
    main()