def main():
    # 入力
    N = int(input())
    # Nの桁数を調べる
    keta = len(str(N))
    # Nの各桁の値を調べる
    s = 0
    for i in range(keta):
        s += int(str(N)[i])
    # 出力
    if N % s == 0:
        print("Yes")
    else:
        print("No")
