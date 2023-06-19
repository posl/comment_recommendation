def main():
    N,K = map(int,input().split())
    ans = 0
    for i in range(N):
        for j in range(K):
            room = (i+1)*100 + (j+1)
            ans += room
    print(ans)
