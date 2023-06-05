def main():
    N, M = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(M)]
    # まず、ABをソートする。
    AB.sort(key=lambda x: x[1])
    # ある橋の左側にある島の数を数える
    left_island = [0] * (N + 1)
    for a, b in AB:
        left_island[b] = left_island[a] + 1
    # ある橋の右側にある島の数を数える
    right_island = [0] * (N + 1)
    for a, b in AB[::-1]:
        right_island[a] = right_island[b] + 1
    # ある橋が倒れたときに不便な島の数を数える
    inconvenience = [0] * M
    for i, (a, b) in enumerate(AB):
        inconvenience[i] = left_island[a] * right_island[b]
    # 不便な島の数を出力する
    for i in inconvenience:
        print(i)
