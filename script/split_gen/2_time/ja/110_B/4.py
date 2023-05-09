def main():
    # 入力
    N, M, X, Y = map(int, input().split())
    x = list(map(int, input().split()))
    y = list(map(int, input().split()))
    # 処理
    Z = max(x) + 1
    if Z <= Y and Z > X:
        for i in range(M):
            if Z <= y[i]:
                print("War")
                break
        else:
            print("No War")
    else:
        print("War")
