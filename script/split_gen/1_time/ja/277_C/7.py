def main():
    #input
    N = int(input())
    AB = [[int(i) for i in input().split()] for _ in range(N)]
    #compute
    AB.sort(key=lambda x: x[0])
    ans = 1
    for i in range(N):
        ans = max(ans, AB[i][1])
        if i < N-1:
            ans = max(ans, AB[i+1][0])
    #output
    print(ans)
