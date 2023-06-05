def main():
    N, M = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(M)]
    AB.sort(key=lambda x: x[1])
    AB.sort(key=lambda x: x[0])
    #print(AB)
    if AB[0][0] != 1 or AB[-1][1] != N:
        print(0)
        return
    else:
        ans = 1
        for i in range(M-1):
            if AB[i][1] != AB[i+1][0]:
                ans *= 2
                ans %= 10**9+7
        print(ans)
        return
main()
