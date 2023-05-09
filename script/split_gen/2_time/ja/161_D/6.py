def main():
    K = int(input())
    #ルンルン数を格納するリスト
    runrun_list = []
    #ルンルン数の個数
    runrun_num = 0
    #ルンルン数を探索するためのリスト
    search_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    #ルンルン数の個数が K に達するまでルンルン数を探索する
    while runrun_num < K:
        #探索リストの先頭の数字を取り出し
        num = search_list.pop(0)
        #ルンルン数の個数を 1 増やす
        runrun_num += 1
        #ルンルン数の個数が K に達したらルンルン数を出力してプログラムを終了する
        if runrun_num == K:
            print(num)
            return
        #ルンルン数をリストに追加する
        runrun_list.append(num)
        #ルンルン数の末尾の数字を取り出す
        num_tail = num % 10
        #ルンルン数の末尾の数字が 0 でないとき
        if num_tail != 0:
            #ルンルン数に 1 を足した数を探索リストに追加する
            search_list.append(num * 10 + num_tail - 1)
        #ルンルン数の末尾の数字が 9 でないとき
        if num_tail != 9:
            #ルンルン数に 1 を足した数を探索リストに追加する
            search_list.append(num * 10 + num_tail + 1)
