def main():
    #入力
    L1, R1, L2, R2 = map(int, input().split())
    #処理
    if R1 <= L2:
        print(0)
    elif R2 <= L1:
        print(0)
    else:
        print(min(R1, R2) - max(L1, L2))
