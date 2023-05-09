def main():
    K = int(input())
    #ルンルン数のリスト
    runrun_list = []
    #ルンルン数のリストの長さ
    runrun_len = 0
    #ルンルン数のリストの長さがKを超えるまでループ
    while runrun_len < K:
        #ルンルン数のリストの長さが0の時
        if runrun_len == 0:
            #ルンルン数のリストに0を追加
            runrun_list.append(0)
            #ルンルン数のリストの長さに1を加算
            runrun_len += 1
        #ルンルン数のリストの長さが0ではない時
        else:
            #ルンルン数のリストの末尾の値を取得
            num = runrun_list[-1]
            #ルンルン数のリストの末尾の値が9の時
            if num % 10 == 9:
                #ルンルン数のリストに末尾の値に10を加算した値を追加
                runrun_list.append(num + 10)
                #ルンルン数のリストの長さに1を加算
                runrun_len += 1
            #ルンルン数のリストの末尾の値が9ではない時
            else:
                #ルンルン数のリストに末尾の値に1を加算した値を追加
                runrun_list.append(num + 1)
                #ルンルン数のリストの長さに1を加算
                runrun_len += 1
                #ルンルン数のリストの末尾の値が0の時
                if num % 10 == 0:
                    #ルンルン数のリストに末尾の値に10を加算した値を追加
                    runrun_list.append(num + 10)
                    #ルンルン数のリ
