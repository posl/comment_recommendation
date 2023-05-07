def main():
    N, M = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(N)]
    AB.sort(key=lambda x: x[0]) # A_iでソート
    B = [0] # B_iを格納する
    for i in range(N):
        B.append(AB[i][1])
    B.sort(reverse=True) # B_iを大きい順にソート
    ans = 0
    for i in range(M):
        ans += B[i]
    print(ans)
