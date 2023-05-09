def main():
    N, M = map(int, input().split())
    H = list(map(int, input().split()))
    AB = [list(map(int, input().split())) for _ in range(M)]
    #print(N, M)
    #print(H)
    #print(AB)
    ans = 0
    for i in range(N):
        flag = True
        for j in range(M):
            if AB[j][0] == i + 1:
                if H[i] <= H[AB[j][1] - 1]:
                    flag = False
                    break
            elif AB[j][1] == i + 1:
                if H[i] <= H[AB[j][0] - 1]:
                    flag = False
                    break
        if flag:
            ans += 1
    print(ans)

if __name__ == '__main__':
    main()