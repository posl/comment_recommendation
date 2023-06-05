def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = list(map(int, input().split()))
    # Bの値をキーとして、出現回数をカウント
    cnt_B = [0] * (N + 1)
    for i in range(N):
        cnt_B[B[C[i] - 1]] += 1
    # Aの値をキーとして、Bの値をカウント
    cnt_A = [0] * (N + 1)
    for i in range(N):
        cnt_A[A[i]] += cnt_B[i + 1]
    # 結果を出力
    print(sum(cnt_A))

if __name__ == '__main__':
    main()