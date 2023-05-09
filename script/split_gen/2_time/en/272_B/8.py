def main():
    N, M = map(int, input().split())
    # 2次元配列を宣言
    attended_party = [[0 for i in range(N)] for j in range(N)]
    for i in range(M):
        k = list(map(int, input().split()))
        for j in range(1, k[0]):
            attended_party[k[j]-1][k[j+1]-1] = 1
            attended_party[k[j+1]-1][k[j]-1] = 1
    for i in range(N):
        if 0 in attended_party[i]:
            print("No")
            return
    print("Yes")
