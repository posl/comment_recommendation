def main():
    #入力
    H, W = map(int, input().split())
    A = [list(map(int, input().split())) for i in range(H)]
    #Aの合計値を求める
    A_sum = sum([sum(A[i]) for i in range(H)])
    #Aの合計値をH*Wで割った値を求める
    A_avg = A_sum // (H * W)
    #Aの合計値をH*Wで割った余りを求める
    A_mod = A_sum % (H * W)
    #Aの合計値をH*Wで割った余りが0でない場合、A_avgを1増やす
    if A_mod != 0:
        A_avg += 1
    #Aの合計値をH*Wで割った値をA_avgとしたときの、Aの合計値との差を求める
    A_diff = [abs(A_avg - A[i][j]) for i in range(H) for j in range(W)]
    #Aの合計値をH*Wで割った値をA_avgとしたときの、Aの合計値との差の合計値を求める
    A_diff_sum = sum(A_diff)
    #Aの合計値をH*Wで割った値をA_avgとしたときの、Aの合計値との差の合計値を2で割った値を出力する
    print(A_diff_sum // 2)
