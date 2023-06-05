def problems266_d():
    n = int(input())
    txa = []
    for i in range(n):
        txa.append(list(map(int, input().split())))
    txa.insert(0, [0, 0, 0])
    ans = 0
    for i in range(1, n+1):
        time = txa[i][0] - txa[i-1][0]
        dis = abs(txa[i][1] - txa[i-1][1])
        if dis > time:
            print('No')
            return
        else:
            if (time - dis) % 2 == 1:
                print('No')
                return
            else:
                ans += txa[i][2]
    print('Yes')
    print(ans)

if __name__ == '__main__':
    problems266_d()