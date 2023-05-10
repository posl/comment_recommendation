def main():
    S = input()
    MOD = 10**9 + 7
    # 1. ?をA, B, Cに置換した文字列を作る
    # 2. ABCの数を数える
    # 3. 1と2を繰り返す
    # 4. 答えを出力する
    # 1
    S = S.replace('?', 'D')
    # 2
    count = 0
    ABC_count = 0
    for i in range(len(S)):
        if S[i] == 'A':
            count += 1
        elif S[i] == 'B':
            ABC_count += count
        elif S[i] == 'C':
            ABC_count = (ABC_count * 3 + count) % MOD
        else:
            ABC_count = (ABC_count * 3 + count * 3) % MOD
            count = (count * 3) % MOD
    # 3
    print(ABC_count)
