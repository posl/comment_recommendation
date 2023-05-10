def main():
    N, K = map(int, input().split())
    score = [list(map(int, input().split())) for _ in range(N)]
    rank = [0] * N
    for i in range(N):
        rank[i] = score[i][0] + score[i][1] + score[i][2]
    for i in range(N):
        if rank[i] >= rank[K-1]:
            if rank[i] == rank[K-1]:
                if score[i][0] + score[i][1] + score[i][2] > score[K-1][0] + score[K-1][1] + score[K-1][2]:
                    print("Yes")
                else:
                    print("No")
            else:
                print("Yes")
        else:
            print("No")
