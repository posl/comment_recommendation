def main():
    K = int(input())
    #ルンルン数を格納するリスト
    runrun_list = []
    #ルンルン数の数
    runrun_count = 0
    #ルンルン数を探す
    for i in range(1, 10):
        #ルンルン数を格納するスタック
        stack = [i]
        while len(stack) > 0:
            #スタックから取り出す
            num = stack.pop()
            #ルンルン数をリストに追加
            runrun_list.append(num)
            runrun_count += 1
            #ルンルン数の数がKを超えたらルンルン数の探索を終了
            if runrun_count > K:
                break
            #ルンルン数のリストの最後の数字の1の位を取得
            last_num = num % 10
            #ルンルン数のリストの最後の数字の1の位が0の場合、1を足した数をスタックに追加
            if last_num == 0:
                stack.append(num * 10 + last_num + 1)
            #ルンルン数のリストの最後の数字の1の位が9の場合、1を引いた数をスタックに追加
            elif last_num == 9:
                stack.append(num * 10 + last_num - 1)
            #ルンルン数のリストの最後の数字の1の位が0でも9でもない場合、1を足した数と1を引いた数をスタックに追加
            else:
                stack.append(num * 10 + last_num + 1)
                stack.append(num * 10 + last_num - 1)
    #ルンルン数のリストのK番目の数字を出力
    print(runrun_list[K - 1])
