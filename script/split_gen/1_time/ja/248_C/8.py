def main():
    N, M, K = map(int, input().split())
    ans = 0
    # Aの1桁目を決める
    for a1 in range(1, M+1):
        # Aの1桁目が決まったときの条件を満たすAの2桁目の個数を数える
        # Aの1桁目がa1のとき、Aの2桁目は1以上M以下の整数である。
        # Aの1桁目がa1のとき、Aの2桁目の個数はM個である。
        # Aの1桁目がa1のとき、Aの2桁目の合計はa1*Mである。
        # Aの1桁目がa1のとき、Aの2桁目の合計がK以下のときのAの2桁目の個数は、
        # K-a1*M以下の整数の個数である。
        # Aの1桁目がa1のとき、Aの2桁目の合計がK以下のときのAの2桁目の個数は、
        # K-a1*M以下の整数の個数は、min(M, K-a1*M)である。
        # Aの1桁目がa1のとき、Aの2桁目の合計がK以下のときのAの2桁目の個数は、
        # min(M, K-a1*M)である。
        # Aの1桁目がa1のとき、Aの2桁目の合計がK以下のときのAの2桁目の個数は、
        # min(M, K-a1*M)である。
        # Aの1桁目がa1のとき、Aの2桁目の合計がK以下のときのAの2桁目の個数は、
        # min(M, K-a1*M)である。
        # Aの1桁