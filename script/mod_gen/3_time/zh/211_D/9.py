def main():
    N, M = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(M)]
    AB = sorted(AB, key=lambda x: x[1])
    #print(AB)
    ans = 1
    max_v = AB[0][1]
    for i in range(1, M):
        if AB[i][0] >= max_v:
            max_v = AB[i][1]
            ans += 1
    print(ans)

if __name__ == '__main__':
    main()