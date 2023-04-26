Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, M = map(int, input().split())
    A = [0] * M
    B = [0] * M
    for i in range(M):
        A[i], B[i] = map(int, input().split())
    #print(A)
    #print(B)
    #print(N, M)
    #print(A)
    #print(B)
    #print("N:", N)
    #print("M:", M)

    # 1からNまでの配列を作る
    arr = [i for i in range(1, N+1)]
    #print(arr)

    # 隣り合っているかのチェック
    for i in range(M):
        #print("A[i]:", A[i])
        #print("B[i]:", B[i])
        #print("arr[A[i]-1]:", arr[A[i]-1])
        #print("arr[B[i]-1]:", arr[B[i]-1])
        #print("arr[A[i]]:", arr[A[i]])
        #print("arr[B[i]]:", arr[B[i]])
        if abs(arr[A[i]-1] - arr[B[i]-1]) != 1:
            print("No")
            return

    print("Yes")

=======
Suggestion 2

def main():
    N, M = map(int, input().split())
    A = [0] * M
    B = [0] * M
    for i in range(M):
        A[i], B[i] = map(int, input().split())
    ans = 'Yes'
    for i in range(M):
        if abs(A[i] - B[i]) == 1:
            continue
        else:
            ans = 'No'
            break
    print(ans)

=======
Suggestion 3

def main():
    N, M = map(int, input().split())
    A = []
    B = []
    for _ in range(M):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    A = [a - 1 for a in A]
    B = [b - 1 for b in B]
    if N == 2:
        if M == 0:
            print('Yes')
            return
        else:
            print('No')
            return
    if M == 0:
        print('Yes')
        return
    if M == 1:
        if A[0] == 0 or B[0] == 0:
            print('Yes')
            return
        if A[0] == N - 1 or B[0] == N - 1:
            print('Yes')
            return
        print('No')
        return
    if M == 2:
        if A[0] == 0 or B[0] == 0:
            if A[1] == 0 or B[1] == 0:
                print('Yes')
                return
            else:
                print('No')
                return
        if A[0] == N - 1 or B[0] == N - 1:
            if A[1] == N - 1 or B[1] == N - 1:
                print('Yes')
                return
            else:
                print('No')
                return
        print('No')
        return
    print('Yes')

main()

=======
Suggestion 4

def main():
    import sys
    input = sys.stdin.readline
    sys.setrecursionlimit(10**6)

    N, M = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(M)]

    # 人iが隣り合う人のリスト
    neighbor = [[] for _ in range(N+1)]
    for a, b in AB:
        neighbor[a].append(b)
        neighbor[b].append(a)

    # 人iが隣り合う人の数
    neighbor_cnt = [len(neighbor[i]) for i in range(1, N+1)]

    # 人iが隣り合う人のうち、隣り合う人のリストに自分自身が含まれているか
    neighbor_cnt2 = [neighbor[i].count(i) for i in range(1, N+1)]

    # 人iが隣り合う人のうち、隣り合う人のリストに自分自身が含まれているか
    neighbor_cnt3 = [neighbor[i].count(i) for i in range(1, N+1)]

    # 人iが隣り合う人のうち、隣り合う人のリストに自分自身が含まれているか
    neighbor_cnt4 = [neighbor[i].count(i) for i in range(1, N+1)]

    # 人iが隣り合う人のうち、隣り合う人のリストに自分自身が含まれているか
    neighbor_cnt5 = [neighbor[i].count(i) for i in range(1, N+1)]

    # 人iが隣り合う人のうち、隣り合う人のリストに自分自身が含まれているか
    neighbor_cnt6 = [neighbor[i].count(i) for i in range(1, N+1)]

    # 人iが隣り合う人のうち、隣り合う人のリストに自分自身が含まれているか
    neighbor_cnt7 = [neighbor[i].count(i

=======
Suggestion 5

def main():
    N, M = map(int, input().split())
    AB = [list(map(int, input().split())) for i in range(M)]
    print("Yes" if solve(N, M, AB) else "No")

=======
Suggestion 6

def main():
    N, M = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(M)]
    ans = 'Yes'
    for i in range(M):
        if AB[i][0] == AB[i][1] - 1:
            ans = 'No'
    print(ans)

=======
Suggestion 7

def main():
    #入力
    N,M = map(int,input().split())
    AB = [list(map(int,input().split())) for _ in range(M)]
    #グラフの作成
    graph = [[] for _ in range(N)]
    for a,b in AB:
        graph[a-1].append(b-1)
        graph[b-1].append(a-1)
    #グラフの探索
    visited = [0]*N
    def dfs(v):
        visited[v] = 1
        for nv in graph[v]:
            if visited[nv] == 0:
                dfs(nv)
    dfs(0)
    #出力
    if 0 in visited:
        print('No')
    else:
        print('Yes')

=======
Suggestion 8

def main():
    N, M = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(M)]
    AB.sort(key=lambda x: x[1])

    left = 0
    right = 0
    for a, b in AB:
        if left < a:
            left = a
        if b <= right:
            continue
        if b - left > 1:
            print('No')
            return
        right = b
    print('Yes')

=======
Suggestion 9

def main():
    N, M = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(M)]
    AB.sort()
    AB = [0] + AB
    for i in range(1, M + 1):
        if AB[i][0] + 1 == AB[i][1] or AB[i][0] - 1 == AB[i][1]:
            print("No")
            exit()
    print("Yes")

=======
Suggestion 10

def main():
    N, M = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(M)]

    # 1. 1からNの番号がついたN人を横一列に並べる

    # 2. 以下の形式のM個の条件全てを満たすものが存在するか判定

    # 3. 条件：人A_iと人B_iは隣り合っている

    # 4. 2番目の条件を満たす並べ方が存在するならYes、存在しないならNo

    # 5. 4番目の条件を満たす並べ方が存在するかどうかを判定

    # 6. 5番目の条件を満たす並べ方が存在するならYes、存在しないならNo

    # 7. Yes or No

    # 8. 7番目の条件を満たす並べ方が存在するならYes、存在しないならNo

    # 9. Yes or No

    # 10. 9番目の条件を満たす並べ方が存在するならYes、存在しないならNo

    # 11. Yes or No

    # 12. 11番目の条件を満たす並べ方が存在するならYes、存在しないならNo

    # 13. Yes or No

    # 14. 13番目の条件を満たす並べ方が存在するならYes、存在しないならNo

    # 15. Yes or No

    # 16. 15番目の条件を満たす並べ方が存在するならYes、存在しないならNo

    # 17. Yes or No

    # 18. 17番目の条件を満たす並べ方が存在するならYes、存在しないならNo

    # 19
