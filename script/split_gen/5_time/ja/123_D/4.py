def main():
    # 標準入力を取得
    x, y, z, k = map(int, input().split())
    a_list = list(map(int, input().split()))
    b_list = list(map(int, input().split()))
    c_list = list(map(int, input().split()))
    #print(x, y, z, k)
    #print(a_list)
    #print(b_list)
    #print(c_list)
    # 3つのケーキの選び方は X × Y × Z 通りあり、それらをケーキの美味しさの合計が大きい順に並べると以下の通りです。
    # (A_2, B_2, C_2): 6 + 5 + 8 = 19
    # (A_1, B_2, C_2): 4 + 5 + 8 = 17
    # (A_2, B_1, C_2): 6 + 1 + 8 = 15
    # (A_2, B_2, C_1): 6 + 5 + 3 = 14
    # (A_1, B_1, C_2): 4 + 1 + 8 = 13
    # (A_1, B_2, C_1): 4 + 5 + 3 = 12
    # (A_2, B_1, C_1): 6 + 1 + 3 = 10
    # (A_1, B_1, C_1): 4 + 1 + 3 = 8
    # 3つのケーキの選び方は X × Y × Z 通りあり、それらをケーキの美味しさの合計が大きい順に並べると以下の通りです。
    # (A_2, B_2, C_2): 6 + 5 + 8 = 19
    # (A_1, B_2, C_2): 4 + 5 + 8 = 17
    # (A_2, B_1
