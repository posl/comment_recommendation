def main():
    # 入力
    N = int(input())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    # 高橋氏の票数を計算
    T = 0
    for i in range(N):
        T += B[i]
    # 青木氏の票数を計算
    A.sort()
    B.sort()
    A.reverse()
    B.reverse()
    S = 0
    for i in range(N):
        S += A[i]
        if S > T:
            print(i + 1)
            return

if __name__ == '__main__':
    main()