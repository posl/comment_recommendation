def main():
    N, M, Q = map(int, input().split())
    LR = [list(map(int, input().split())) for _ in range(M)]
    PQ = [list(map(int, input().split())) for _ in range(Q)]
    # 1. LRを左端でソートする
    # 2. PQを左端でソートする
    # 3. LRを左端がPQの左端以降のものを抽出し、右端でソートする
    # 4. LRを右端がPQの右端以前のものを抽出する
    # 5. LRを右端でソートする
    # 6. LRを右端がPQの左端以降のものを抽出する
    # 7. LRの長さを出力する
    LR = sorted(LR, key=lambda x: x[0])
    PQ = sorted(PQ, key=lambda x: x[0])
    LR = sorted([lr for lr in LR if lr[0] >= PQ[0][0]], key=lambda x: x[1])
    LR = [lr for lr in LR if lr[1] <= PQ[0][1]]
    LR = sorted(LR, key=lambda x: x[1])
    LR = [lr for lr in LR if lr[1] >= PQ[0][0]]
    print(len(LR))
