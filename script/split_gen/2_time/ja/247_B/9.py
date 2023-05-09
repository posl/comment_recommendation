def main():
    N = int(input())
    #名前のリスト
    name_list = [input().split() for i in range(N)]
    #名前の辞書
    name_dict = {}
    for i in range(N):
        name_dict[name_list[i][0]] = 0
        name_dict[name_list[i][1]] = 0
    for i in range(N):
        if name_dict[name_list[i][0]] == 0 and name_dict[name_list[i][1]] == 0:
            name_dict[name_list[i][0]] = 1
            name_dict[name_list[i][1]] = 1
        else:
            print("No")
            return
    print("Yes")
