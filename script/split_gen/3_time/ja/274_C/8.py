def main():
    N = int(input())
    A = list(map(int,input().split()))
    #親のリスト
    parent = [0]*(2*N+1)
    #親のリストを作成
    for i in range(N):
        parent[2*i+1] = A[i]
        parent[2*i+2] = A[i]
    #親のリストから何代親かを求める
    for i in range(2*N+1):
        if parent[i] == 0:
            print(0)
        else:
            count = 0
            while parent[i] != 1:
                i = parent[i]-1
                count += 1
            print(count+1)
