def main():
    #input
    N, X = map(int, input().split())
    VPs = [list(map(int, input().split())) for _ in range(N)]
    #compute
    ans = -1
    for i in range(N):
        if X < VPs[i][0]*VPs[i][1]/100:
            ans = i+1
            break
    #output
    print(ans)
