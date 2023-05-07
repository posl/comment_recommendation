def main():
    #入力
    N, M, Q = map(int, input().split())
    abcd = [list(map(int, input().split())) for _ in range(Q)]
    #初期値
    A = [1]*N
    ans = 0
    #dfs
    def dfs(A, index):
        global ans
        if index == N:
            #得点計算
            score = 0
            for i in range(Q):
                if A[abcd[i][1]-1] - A[abcd[i][0]-1] == abcd[i][2]:
                    score += abcd[i][3]
            ans = max(ans, score)
            return
        for i in range(A[index-1], M+1):
            A[index] = i
            dfs(A, index+1)
    dfs(A, 1)
    print(ans)
