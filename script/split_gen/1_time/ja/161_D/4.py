def main():
    #Kを取得
    K = int(input())
    #ルンルン数を格納するリストを作成
    runrun_list = []
    #ルンルン数を格納するリストの長さがKになるまでループ
    while len(runrun_list) < K:
        #ルンルン数を格納するリストの長さが0の場合
        if len(runrun_list) == 0:
            #0~9をルンルン数を格納するリストに格納
            for i in range(10):
                runrun_list.append(i)
        #ルンルン数を格納するリストの長さが0以外の場合
        else:
            #ルンルン数を格納するリストの長さを取得
            runrun_list_len = len(runrun_list)
            #ルンルン数を格納するリストの長さ分ループ
            for i in range(runrun_list_len):
                #ルンルン数を格納するリストの最後の要素を取得
                last_num = runrun_list[-1]
                #ルンルン数を格納するリストの最後の要素の最後の桁を取得
                last_num_last_digit = last_num % 10
                #ルンルン数を格納するリストの最後の要素の最後の桁が0の場合
                if last_num_last_digit == 0:
                    #ルンルン数を格納するリストに最後の要素に10を足した値を追加
                    runrun_list.append(last_num + 10)
                #ルンルン数を格納するリストの最後の要素の最後の桁が9の場合
                elif last_num_last_digit == 9:
                    #ルンルン数を格納するリストに最後の要素に10を引いた値を追加
                    runrun_list.append(last_num - 10)
                #ルンルン
