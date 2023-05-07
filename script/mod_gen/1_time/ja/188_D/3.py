def main():
    N, C = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(N)]
    AB.sort(key=lambda x: x[0])
    ans = 0
    for i in range(N):
        if i == 0:
            ans += AB[i][1] * C
        else:
            if AB[i][0] <= AB[i-1][1]:
                if AB[i][1] > AB[i-1][1]:
                    ans += (AB[i][1] - AB[i-1][1]) * C
            else:
                ans += (AB[i][1] - AB[i][0] + 1) * C
    print(ans)
main()

if __name__ == '__main__':
    main()