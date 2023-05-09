def main():
    #入力
    N = int(input())
    A = int(input())
    B = int(input())
    C = int(input())
    D = int(input())
    E = int(input())
    #計算
    #都市 6 に到着するまでに最短で何分かかるか
    min_time = min(A,B,C,D,E)
    #都市 6 に到着するまでにかかる時間を計算
    time = (N + min_time - 1) // min_time
    #出力
    print(time + 4)
