def main():
    # おもりの数
    N = int(input())
    # おもりの重さ
    W = int(input())
    # おもりの重さをリストに格納
    A = list(map(int, input().split()))
    # 良い整数の個数
    count = 0
    # おもりの重さの和
    sum = 0
    # おもりの重さの和を格納するリスト
    sum_list = []
    # おもりの重さの和を格納するリストに0を追加
    sum_list.append(0)
    # おもりの重さの和を格納するリストに1を追加
    sum_list.append(1)
    # おもりの重さの和を格納するリストを作成
    for i in range(N):
        sum += A[i]
        sum_list.append(sum)
    # おもりの重さの和を格納するリストの中から、
    # 重さの和がW以下のものをカウント
    for i in sum_list:
        if i <= W:
            count += 1
    print(count)

if __name__ == '__main__':
    main()