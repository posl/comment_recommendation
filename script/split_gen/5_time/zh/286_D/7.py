def main():
    n,x = map(int,input().split())
    coin = []
    for i in range(n):
        coin.append(list(map(int,input().split())))
    if x == 0:
        print('Yes')
    else:
        for i in range(n):
            if coin[i][1] >= x:
                print('Yes')
                break
            else:
                x -= coin[i][1]
                if x == 0:
                    print('Yes')
                    break
                elif i == n-1:
                    print('No')
                    break
