def main():
    N = int(input())
    S = input()
    # 0 は固定で最後に入れる
    # 1 から N までの数字をリストに入れる
    A = [0]
    for i in range(N):
        if S[i] == "L":
            A.insert(0, i + 1)
        else:
            A.append(i + 1)
    # 答えを出力
    print(*A)
