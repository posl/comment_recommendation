def main():
    S = input()
    Q = int(input())
    query = [list(map(int, input().split())) for _ in range(Q)]
    # Sの各文字の出現回数
    cnt = [0] * 3
    for s in S:
        cnt[ord(s) - ord("A")] += 1
    # Sの各文字の出現回数を3で割った余り
    mod = [0] * 3
    for i in range(3):
        mod[i] = cnt[i] % 3
    # Sの各文字の出現回数を3で割った商
    div = [0] * 3
    for i in range(3):
        div[i] = cnt[i] // 3
    # 3で割った余りが0の文字を格納
    zero = []
    for i in range(3):
        if mod[i] == 0:
            zero.append(i)
    # 3で割った余りが1の文字を格納
    one = []
    for i in range(3):
        if mod[i] == 1:
            one.append(i)
    # 3で割った余りが2の文字を格納
    two = []
    for i in range(3):
        if mod[i] == 2:
            two.append(i)
    # 3で割った余りが0の文字が2つ以上ある場合
    if len(zero) >= 2:
        # 3で割った余りが0の文字が2つある場合
        if len(zero) == 2:
            # 3で割った余りが0の文字がAとBの場合
            if zero[0] == 0 and zero[1] == 1:
                # 3で割った余りが0の文字がAとCの場合
                if zero[0] == 0 and zero[1] == 2:
                    # 3で割った余りが0の文字がBとCの場合
                    if zero[0] == 1
