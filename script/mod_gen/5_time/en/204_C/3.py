def main():
    N,M = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(M)]
    ans = 0
    for i in range(1,N+1):
        for j in range(1,N+1):
            if i == j:
                ans += 1
            else:
                for k in range(M):
                    if AB[k][0] == i and AB[k][1] == j:
                        break
                else:
                    ans += 1
    print(ans)

if __name__ == '__main__':
    main()