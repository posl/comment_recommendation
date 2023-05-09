def main():
    N = int(input())
    A = list(map(int, input().split()))
    #親の番号を格納するリスト
    parent = [0]*(2*N+1)
    #アメーバの世代を格納するリスト
    generation = [0]*(2*N+1)
    #親の番号を格納する
    for i in range(N):
        parent[2*i+1] = A[i]
        parent[2*i+2] = A[i]
    #アメーバの世代を格納する
    for i in range(2*N+1):
        if i == 0:
            generation[i] = 0
        else:
            generation[i] = generation[parent[i]-1] + 1
    #アメーバの世代を出力する
    for i in range(2*N+1):
        print(generation[i])

if __name__ == '__main__':
    main()