def main():
    N, M = map(int, input().split())
    #print(N, M)
    #print("-----")
    #print("-----")
    
    #参加者のリスト
    attend_list = []
    
    for i in range(M):
        #参加者の数
        k = int(input())
        #print(k)
        #参加者の番号
        x = list(map(int, input().split()))
        #print(x)
        #print("-----")
        
        #参加者の番号をリストに追加
        attend_list.append(x)
    
    #print(attend_list)
    
    #参加者の番号を集合に変換
    attend_set = [set(i) for i in attend_list]
    #print(attend_set)
    
    #参加者の集合の積集合
    attend_set_intersect = attend_set[0]
    #print(attend_set_intersect)
    
    for i in range(1, len(attend_set)):
        attend_set_intersect = attend_set_intersect & attend_set[i]
        #print(attend_set_intersect)
    
    #print(attend_set_intersect)
    
    #参加者の集合の積集合が空集合でない場合
    if attend_set_intersect:
        print("Yes")
    else:
        print("No")
