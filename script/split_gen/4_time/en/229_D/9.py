def main():
    S = input()
    K = int(input())
    N = len(S)
    # Sの中の連続した.の最大値を求める
    # 例えばS = XX...X.X.X.の場合、
    # 連続した.の最大値は2
    max_dot = 0
    tmp = 0
    for i in range(N):
        if S[i] == '.':
            tmp += 1
        else:
            max_dot = max(max_dot, tmp)
            tmp = 0
    max_dot = max(max_dot, tmp)
    # Sの中に連続した.が存在しない場合
    if max_dot == 0:
        print(min(N, K * 2 + 1))
        return
    # Sの中に連続した.が存在する場合
    # 連続した.をXに変換することで、
    # 連続したXの最大値は、連続した.の最大値 + K
    print(min(N, max_dot + K * 2))
