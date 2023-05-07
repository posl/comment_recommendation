def main():
    #入力
    N = int(input())
    H = list(map(int, input().split()))
    #処理
    max_num = max(H)
    max_index = H.index(max_num) + 1
    #出力
    print(max_index)
