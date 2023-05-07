def main():
    N, M = map(int, input().split())
    H = list(map(int, input().split()))
    AB = [list(map(int, input().split())) for _ in range(M)]
    ans = 0
    for i in range(N):
        flag = 0
        for j in range(M):
            if AB[j][0] == i+1 and H[AB[j][0]-1] <= H[AB[j][1]-1]:
                flag = 1
            elif AB[j][1] == i+1 and H[AB[j][1]-1] <= H[AB[j][0]-1]:
                flag = 1
        if flag == 0:
            ans += 1
    print(ans)

if __name__ == '__main__':
    main()