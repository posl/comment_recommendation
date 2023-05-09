def main():
    N = int(input())
    AB = []
    for _ in range(N-1):
        AB.append(list(map(int, input().split())))
    #print(N, AB)
    #先頭に1を追加
    AB.insert(0, [1, 0])
    #print(N, AB)
    #ABをソート
    AB.sort(key=lambda x:x[0])
    #print(N, AB)
    #ABを1から順番に辿っていく
    path = []
    path.append(1)
    for i in range(1, N):
        #print(i)
        #print(AB[i])
        #print(path)
        #print(path.index(AB[i][0]))
        #print(AB[i][0] in path)
        if AB[i][0] in path:
            #print("in")
            path.insert(path.index(AB[i][0]), AB[i][1])
        else:
            #print("not in")
            path.append(AB[i][1])
    #print(path)
    #pathの重複を削除
    path = list(dict.fromkeys(path))
    #print(path)
    #pathの重複を削除
    path = list(dict.fromkeys(path))
    #pathの先頭に1を追加
    path.insert(0, 1)
    #pathの先頭に1を追加
    path.append(1)
    #pathを出力
    print(*path)
