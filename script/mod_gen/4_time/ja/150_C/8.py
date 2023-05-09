def main():
    N = int(input())
    P = list(map(int, input().split()))
    Q = list(map(int, input().split()))
    #順列の数を計算
    P_num = 0
    Q_num = 0
    for i in range(N):
        P_num += P[i] * (N - 1 - i) * math.factorial(N - 1 - i)
        Q_num += Q[i] * (N - 1 - i) * math.factorial(N - 1 - i)
    print(abs(P_num - Q_num))

if __name__ == '__main__':
    main()