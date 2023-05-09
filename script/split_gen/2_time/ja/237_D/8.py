def main():
    N = int(input())
    S = input()
    # 0をN個入れたリストを作成
    A = [0] * (N + 1)
    # 0の位置を探す
    zero_index = A.index(0)
    # Sの各文字に対して処理
    for i, s in enumerate(S):
        # Lなら0の左にi+1を挿入
        if s == "L":
            A.insert(zero_index, i + 1)
        # Rなら0の右にi+1を挿入
        else:
            A.insert(zero_index + 1, i + 1)
        # 0の位置を探す
        zero_index = A.index(0)
    print(*A)
