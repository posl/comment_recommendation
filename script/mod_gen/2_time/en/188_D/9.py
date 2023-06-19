def main():
    #入力
    N, C = map(int, input().split())
    ABC = [tuple(map(int, input().split())) for _ in range(N)]
    #初期化
    ABC.sort()
    #print(ABC)
    ans = 0
    for i in range(N):
        #print(i, ABC[i])
        ans += ABC[i][2]
        #print(ans)
        for j in range(i+1, N):
            #print(j, ABC[j])
            if ABC[i][1] >= ABC[j][0]:
                ans += min(ABC[j][2], C*(ABC[j][0]-ABC[i][1]))
            else:
                break
            #print(ans)
    print(ans)
main()
