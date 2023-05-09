def main():
    A = int(input())
    B = int(input())
    C = int(input())
    D = int(input())
    E = int(input())
    #print(A, B, C, D, E)
    
    #料理の調理時間をリストに格納
    cook_time = [A, B, C, D, E]
    #料理の調理時間を昇順にソート
    cook_time.sort()
    #print(cook_time)
    
    #料理の調理時間が最小の料理の調理時間を取得
    min_cook_time = cook_time[0]
    #print(min_cook_time)
    
    #料理の調理時間が最小の料理の調理時間を 10 で割った余りを取得
    #余りが 0 でなければ、料理の調理時間が最小の料理の調理時間を 10 で割った商に 1 を足した値を取得
    if min_cook_time % 10 == 0:
        min_cook_time_10 = min_cook_time // 10
    else:
        min_cook_time_10 = min_cook_time // 10 + 1
    #print(min_cook_time_10)
    
    #料理の調理時間が最小の料理の調理時間を 10 で割った商に 10 を掛けた値を取得
    #print(min_cook_time_10 * 10)
    
    #料理の調理時間が最小の料理の調理時間を 10 で割った商に 10 を掛けた値を最も早く注文できる時刻とする
    #print(min_cook_time_10 * 10)
    
    #料理の調理時間が最小の料理の調理時間を 10 で割った商に 10 を掛けた値 + 料理の調理時間が最大の料理の調理時間を取得
