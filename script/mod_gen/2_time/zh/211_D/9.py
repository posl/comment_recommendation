def main():
    N, M = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(M)]
    AB.sort(key=lambda x: x[1])
    #print(AB)
    ans = 0
    tmp = 0
    for i in range(M):
        if AB[i][0] == 1:
            tmp += 1
            if AB[i][1] == N:
                ans += 1
        else:
            if tmp > 0:
                ans += 1
            break
    print(ans)

if __name__ == '__main__':
    main()