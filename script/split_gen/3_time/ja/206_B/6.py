def main():
    N = int(input())
    #貯金箱の中身
    money = 0
    #何日目の夜か
    day = 0
    #貯金箱の中身がN以上になるまで繰り返す
    while money < N:
        #何日目かをカウント
        day += 1
        #貯金箱の中身に何日目かを足す
        money += day
    #何日目の夜かを出力
    print(day)
