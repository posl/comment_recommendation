def main():
    N = int(input())
    S = list(map(int, input().split()))
    T = list(map(int, input().split()))
    # すぬけくんが宝石を受け取る時刻のリスト
    A = [0] * N
    # 高橋くんが宝石を渡す時刻のリスト
    B = [0] * N
    # 高橋くんが渡した宝石の受け取り時刻のリスト
    C = [0] * N
    # すぬけくんが宝石を受け取る時刻を計算
    for i in range(N):
        A[i] = T[i] + S[i]
    # 高橋くんが渡した宝石の受け取り時刻を計算
    for i in range(N):
        B[i] = A[i] + S[(i+1) % N]
    # すぬけくんが宝石を受け取る時刻を計算
    for i in range(N):
        C[i] = B[i] + S[(i+2) % N]
    # すぬけくんが宝石を受け取る時刻を出力
    for i in range(N):
        print(A[i])

if __name__ == '__main__':
    main()