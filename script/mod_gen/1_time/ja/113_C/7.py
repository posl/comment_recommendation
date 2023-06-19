def main():
    N, M = map(int, input().split())
    #入力を受け取る
    input_list = []
    for i in range(M):
        P, Y = map(int, input().split())
        input_list.append([P, Y, i])
    #入力を県ごとに分ける
    input_list.sort(key=lambda x: x[0])
    input_list2 = []
    temp = [input_list[0]]
    for i in range(1, M):
        if input_list[i][0] != input_list[i-1][0]:
            input_list2.append(temp)
            temp = [input_list[i]]
        else:
            temp.append(input_list[i])
    input_list2.append(temp)
    #県ごとに誕生年でソート
    for i in range(len(input_list2)):
        input_list2[i].sort(key=lambda x: x[1])
    #誕生順に番号を振る
    ans = [0]*M
    for i in range(len(input_list2)):
        for j in range(len(input_list2[i])):
            ans[input_list2[i][j][2]] = str(input_list2[i][j][0]).zfill(6) + str(j+1).zfill(6)
    #出力
    for i in range(M):
        print(ans[i])
main()
