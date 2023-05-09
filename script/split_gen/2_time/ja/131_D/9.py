def main():
    #入力
    N = int(input())
    AB = []
    for i in range(N):
        AB.append(list(map(int,input().split())))
    #仕事の終了時間でソート
    AB.sort(key=lambda x: x[1])
    #print(AB)
    #仕事の終了時間が早い順に仕事を終わらせる
    time = 0
    for i in range(N):
        time += AB[i][0]
        if time > AB[i][1]:
            print('No')
            return
    print('Yes')
    return
