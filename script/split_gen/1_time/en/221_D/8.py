def main():
    N = int(input())
    B = []
    for _ in range(N):
        A,B = [int(i) for i in input().split()]
        B.append([A,B])
    B.sort()
    ans = [0]*(N+1)
    for i in range(N):
        ans[1] += B[i][0]-1
        ans[1] -= sum([B[j][1] for j in range(i)])
        ans[1] = max(ans[1],0)
        ans[1] = min(ans[1],B[i][1])
        ans[N] += B[i][0]-1
        ans[N] -= sum([B[j][1] for j in range(i)])
        ans[N] = max(ans[N],0)
        ans[N] = min(ans[N],B[i][1])
        ans[1] += 1
        ans[N] -= 1
        ans[B[i][1]] += 1
        ans[B[i][1]+1] -= 1
    for i in range(1,N):
        ans[i] += ans[i-1]
    for i in range(1,N+1):
        print(ans[i],end=" ")
    print()
