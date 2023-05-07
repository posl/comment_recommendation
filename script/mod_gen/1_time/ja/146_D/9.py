def main():
    N = int(input())
    # a,bの値を格納する
    a = []
    b = []
    for i in range(N-1):
        a_i,b_i = map(int,input().split())
        a.append(a_i)
        b.append(b_i)
    # 隣接リストを作成
    # 隣接リストの中身は、その頂点に隣接する頂点のリスト
    # 例：隣接リスト[1] = [2,3,4,5,6]
    # 頂点1に隣接する頂点は2,3,4,5,6
    # 頂点1に隣接する頂点は5個
    a_list = [[] for i in range(N+1)]
    # 隣接リストを作成
    for i in range(N-1):
        a_list[a[i]].append(b[i])
        a_list[b[i]].append(a[i])
    # 隣接リストの中身をソート
    for i in range(N+1):
        a_list[i].sort()
    # 頂点1から順番にBFSを行う
    # 訪問済みの頂点を記録する
    # 例：visited[1] = True
    # 頂点1は訪問済み
    visited = [False for i in range(N+1)]
    # 頂点1を訪問済みにする
    visited[1] = True
    # 訪問済みの頂点を格納する
    # 例：queue = [1]
    # 頂点1を訪問済みにしたので、queueに頂点1を格納
    queue = [1]
    # 訪問済みの頂点の色を格納する
    # 例：color[1] = 1
    # 頂点1の色は1
    color = [0 for i in range(N+1)]
    # 訪問済みの頂点の

if __name__ == '__main__':
    main()