def main():
    #入力
    N = int(input())
    H = list(map(int,input().split()))
    #最大値を求める
    max_h = max(H)
    #最大値の添字を求める
    max_h_index = H.index(max_h)
    #出力
    print(max_h_index+1)
