def main():
    # 文字列 S が与えられる
    S = input()
    # 文字列 T を oxx を 10^5 個結合した文字列として定める
    T = "oxx" * 10**5
    # 文字列 S が T の部分文字列であるかどうかを調べる
    if S in T:
        print("Yes")
    else:
        print("No")
    return
