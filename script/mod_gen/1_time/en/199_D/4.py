def main():
    N, M = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(M)]
    ans = 3 ** N
    for i in range(M):
        for j in range(i + 1, M):
            if AB[i][0] == AB[j][0] or AB[i][0] == AB[j][1] or AB[i][1] == AB[j][0] or AB[i][1] == AB[j][1]:
                ans -= 1
    print(ans)

if __name__ == '__main__':
    main()