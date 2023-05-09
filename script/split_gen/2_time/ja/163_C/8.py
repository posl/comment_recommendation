def main():
    n = int(input())
    a = list(map(int, input().split()))
    # 1から始まるので、要素数はn+1にする
    # このリストのi番目は、社員番号iの部下の数
    b = [0] * (n+1)
    # aの要素を走査する
    for i in a:
        # aの要素は、社員番号iの直属の上司
        # したがって、社員番号iの部下の数を1増やす
        b[i] += 1
    # 1からnまでの社員の部下の数を出力する
    for i in range(1, n+1):
        print(b[i])
