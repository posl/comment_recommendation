def main():
    #従業員数
    N = int(input())
    #A_i, B_i
    A_B = [list(map(int, input().split())) for i in range(N)]
    #A_i, B_iの最小値を格納するリスト
    min_A_B = []
    #A_i, B_iの最小値を格納するリストの作成
    for i in range(N):
        min_A_B.append(min(A_B[i]))
    #A_i, B_iの最小値を格納するリストの最小値を出力
    print(min(min_A_B))

if __name__ == '__main__':
    main()