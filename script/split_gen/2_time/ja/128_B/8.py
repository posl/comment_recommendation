def main():
    N = int(input())
    # リストの要素は、(市名, 点数, レストラン番号)のタプル
    R = []
    for i in range(N):
        S, P = input().split()
        P = int(P)
        R.append((S, P, i+1))
    # 市名で昇順にソート
    R.sort()
    # 同じ市名のレストランの点数で降順にソート
    R = sorted(R, key=lambda x: (x[0], -x[1]))
    for r in R:
        print(r[2])
