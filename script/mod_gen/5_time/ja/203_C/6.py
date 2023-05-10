def solve():
    n,k = map(int, input().split())
    ab = [list(map(int, input().split())) for _ in range(n)]
    ab.sort(key=lambda x:x[0])
    # print(ab)
    money = k
    for i in range(n):
        if money >= ab[i][0]:
            money += ab[i][1]
        else:
            print(ab[i][0]-1)
            exit()
    print(money+ab[-1][0])

if __name__ == '__main__':
    solve()