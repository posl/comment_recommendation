def main():
    N, M = map(int, input().split())
    #print(N, M)
    #print()
    #参加した人のリスト
    people = []
    for i in range(M):
        #舞踏会の参加者
        people.append(list(map(int, input().split())))
        #print(people[i])
    #print()
    #print(people)
    #舞踏会の参加者のリストを一つのリストにまとめる
    people_list = []
    for i in range(M):
        for j in range(1, people[i][0] + 1):
            people_list.append(people[i][j])
    #print()
    #print(people_list)
    #舞踏会の参加者のリストを集合に変換
    people_set = set(people_list)
    #print()
    #print(people_set)
    #舞踏会の参加者のリストの要素数と集合の要素数が同じなら
    #どの二人も少なくとも 1 回同じ舞踏会に参加した
    if len(people_list) == len(people_set):
        print("No")
    else:
        print("Yes")

if __name__ == '__main__':
    main()