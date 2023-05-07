def main():
    N = int(input())
    A = list(map(int, input().split()))
    # 200個の空リストを作る
    # 0-199のリストを作る
    # それぞれのリストに、Aの中で割った余りが同じものがあれば、そのインデックスを入れる
    # その中で、2つ以上あれば、それらを出力する
    # なければ、Noを出力する
    B = [[] for _ in range(200)]
    for i, a in enumerate(A):
        B[a % 200].append(i + 1)
    for b in B:
        if len(b) >= 2:
            print("Yes")
            print("2")
            print(b[0], b[1])
            return
    print("No")
