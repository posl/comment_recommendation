def main():
    N,M = map(int,input().split())
    data = [list(map(int,input().split())) for _ in range(M)]
    bridge = [0 for _ in range(N)]
    bridge[0] = N*(N-1)//2
    for i in range(1,N):
        bridge[i] = bridge[i-1] - i
    ans = []
    for i in range(M-1,-1,-1):
        ans.append(bridge[data[i][0]-1]+bridge[data[i][1]-1])
        bridge[data[i][0]-1] -= 1
        bridge[data[i][1]-1] -= 1
    for i in range(M-1,-1,-1):
        print(ans[i])
