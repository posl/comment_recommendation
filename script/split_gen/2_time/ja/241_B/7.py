def main():
    # 入力
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    # 食事計画が可能かどうか
    for i in range(M):
        if B[i] not in A:
            print("No")
            exit()
    # 食事計画が可能な場合
    print("Yes")
