def main():
    A, B, X = map(int, input().split())
    # 一番高い値段を買えるか？
    if A + B > X:
        print(0)
        return
    # 一番高い値段を買う
    N = X // (A + B)
    # 一番高い値段を買った後の金額
    X -= N * (A + B)
    # 一番高い値段を買った後の金額を使って、一番高い値段を買えるか？
    if A > X:
        print(N)
        return
    # 一番高い値段を買った後の金額を使って、一番高い値段を買う
    N = X // A
    # 一番高い値段を買った後の金額を使って、一番高い値段を買った後の金額
    X -= N * A
    # 一番高い値段を買った後の金額を使って、一番高い値段を買った後の金額を使って、一番高い値段を買えるか？
    if A + B > X:
        print(N)
        return
    # 一番高い値段を買った後の金額を使って、一番高い値段を買った後の金額を使って、一番高い値段を買う
    N = X // (A + B)
    # 一番高い値段を買った後の金額を使って、一番高い値段を買った後の金額を使って、一番高い値段を買った後の金額
    X -= N * (A + B)
    # 一番高い値段を買った後の金額を使って、一番高い値段を買った後の
