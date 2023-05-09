def main():
    N = int(input())
    A = list(map(int, input().split()))
    if N == 1:
        print(A[0])
        return
    if N == 2:
        print(A[0] ^ A[1])
        return
    if N == 3:
        print(A[0] ^ A[1] ^ A[2])
        return
    # 4以上の場合は、A[0]とA[1]のXORを求める
    # XORの結果の値を求める
    # その値とA[2]とA[3]のXORを求める
    # その値とA[4]とA[5]のXORを求める
    # ・・・
    # その値とA[N-2]とA[N-1]のXORを求める
    # その値とA[N-1]とA[0]のXORを求める
    # その値とA[1]とA[2]のXORを求める
    # ・・・
    # その値とA[N-3]とA[N-2]のXORを求める
    # その値とA[N-2]とA[N-1]のXORを求める
    # その値とA[N-1]とA[0]のXORを求める
    # ・・・
    # その値とA[N-4]とA[N-3]のXORを求める
    # その値とA[N-3]とA[N-2]のXORを求める
    # ・・・
    # ・・・
    # ・・・
    # その値とA[1]とA[0]のXORを求める
    # その値とA[0]とA[N-1]のXORを求める
    # ・・・
    # ・・・
    # ・・・
    # その値とA[3]とA[2]のXORを求める
    # その値
