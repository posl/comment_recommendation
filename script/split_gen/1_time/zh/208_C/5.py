def main():
    N, K = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    a.append(a[0] + K)
    #print(a)
    ans = [K//N for i in range(N)]
    #print(ans)
    tmp = K%N
    for i in range(tmp):
        ans[a[i]-1] += 1
    for i in range(N):
        print(ans[i])
