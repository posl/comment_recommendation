def main():
    n = int(input())
    s = input()
    w = list(map(int, input().split()))
    
    #print(n)
    #print(s)
    #print(w)
    
    #子供の数をカウント
    count = 0
    for i in range(n):
        if s[i] == '0':
            count += 1
    
    #print(count)
    
    #重さのリストを作成
    weight = []
    for i in range(n):
        if s[i] == '0':
            weight.append(w[i])
    
    #print(weight)
    
    #重さのリストをソート
    weight.sort()
    
    #print(weight)
    
    #重さのリストの重複を削除
    weight = list(set(weight))
    
    #print(weight)
    
    #重さのリストの重複を削除した結果の長さを取得
    weight_len = len(weight)
    
    #print(weight_len)
    
    #重さのリストの重複を削除した結果の長さが1の場合
    if weight_len == 1:
        #子供の数を出力
        print(count)
        #終了
        exit()
    
    #重さのリストの重複を削除した結果の長さが2の場合
    if weight_len == 2:
        #子供の数を出力
        print(count)
        #終了
        exit()
    
    #重さのリストの重複を削除した結果の長さが3以上の場合
    if weight_len >= 3:
        #子供の数を出力
        print(count)
        #終了
        exit()

if __name__ == '__main__':
    main()