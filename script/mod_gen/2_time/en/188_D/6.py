def main():
    N, C = map(int, input().split())
    AB = [tuple(map(int, input().split())) for _ in range(N)]
    AB.sort(key=lambda x: x[1])
    AB.sort(key=lambda x: x[0])
    ans = 0
    for i in range(N):
        ans += AB[i][2]
    ans *= C
    for i in range(N-1):
        for j in range(i+1, N):
            if AB[i][1] >= AB[j][0]:
                ans = min(ans, (AB[j][1]-AB[j][0]+1)*C*AB[j][2]+(AB[i][1]-AB[j][0]+1)*C*AB[i][2])
            else:
                ans = min(ans, (AB[j][1]-AB[j][0]+1)*C*AB[j][2]+(AB[i][1]-AB[i][0]+1)*C*AB[i][2])
    print(ans)

if __name__ == '__main__':
    main()