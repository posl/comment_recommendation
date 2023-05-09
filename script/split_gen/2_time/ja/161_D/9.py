def main():
    K = int(input())
    #K = 100000
    #K = 1
    #K = 13
    #K = 15
    #ルンルン数を格納するリスト
    runrun_list = []
    #ルンルン数を格納するリストの要素数
    runrun_list_length = 0
    #ルンルン数を格納するリストの最後の要素
    runrun_list_last = 0
    #ルンルン数を格納するリストの最後の要素の桁数
    runrun_list_last_digit = 0
    #ルンルン数を格納するリストの最後の要素の最後の桁
    runrun_list_last_digit_last = 0
    #ルンルン数を格納するリストに1を追加
    runrun_list.append(1)
    runrun_list_length += 1
    runrun_list_last = 1
    runrun_list_last_digit = 1
    runrun_list_last_digit_last = 1
    #ルンルン数を格納するリストに2を追加
    runrun_list.append(2)
    runrun_list_length += 1
    runrun_list_last = 2
    runrun_list_last_digit = 1
    runrun_list_last_digit_last = 2
    #ルンルン数を格納するリストに3を追加
    runrun_list.append(3)
    runrun_list_length += 1
    runrun_list_last = 3
    runrun_list_last_digit = 1
    runrun_list_last_digit_last = 3
    #ルンルン数を格納するリストに4を追加
    runrun_list.append(4)
    runrun_list_length += 1
    runrun_list_last = 4
    runrun_list_last_digit = 1
    runrun_list_last_digit_last = 4
    #ルンルン数を格納するリストに5を追加
    runrun_list.append(5)
    runrun_list_length += 1
