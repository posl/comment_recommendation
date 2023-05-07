def main():
    N = int(input())
    A = list(map(int, input().split()))
    # A[i] が最大値の人の番号を求める
    max_index = 0
    for i in range(N):
        if A[i] > A[max_index]:
            max_index = i
    # 最大値の人を中心に時計回りに並べる
    B = [0] * N
    for i in range(N):
        B[i] = A[(max_index + i) % N]
    # 時計回りに並べたときの心地よさを求める
    C = [0] * N
    C[0] = 0
    C[1] = B[0]
    for i in range(2, N):
        C[i] = min(C[i-1], B[i-1])
    # 時計回りに並べたときの心地よさの合計を求める
    ans = 0
    for i in range(N):
        ans += C[i]
    print(ans)

if __name__ == '__main__':
    main()