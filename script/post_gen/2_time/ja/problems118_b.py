Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N, M = map(int, input().split())
    A = [set(map(int, input().split()[1:])) for _ in range(N)]
    print(len(set.intersection(*A)))

=======
Suggestion 2

def main():
    N, M = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(N)]
    ans = 0
    for i in range(1, M+1):
        if all(i in A[j][1:] for j in range(N)):
            ans += 1
    print(ans)

=======
Suggestion 3

def main():
    N, M = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(N)]
    B = [0] * M
    for i in range(N):
        for j in range(1, A[i][0] + 1):
            B[A[i][j] - 1] += 1
    print(sum(1 for i in range(M) if B[i] == N))

=======
Suggestion 4

def main():
    N, M = map(int, input().split())
    d = [0] * M
    for _ in range(N):
        *A, = map(int, input().split())
        for a in A[1:]:
            d[a-1] += 1
    print(sum(1 for i in d if i == N))

=======
Suggestion 5

def main():
    N, M = map(int, input().split())
    A = [list(map(int, input().split())) for i in range(N)]
    ans = 0
    for i in range(M):
        for j in range(N):
            if i + 1 not in A[j][1:]:
                break
        else:
            ans += 1
    print(ans)

=======
Suggestion 6

def main():
    # 入力
    N, M = map(int, input().split())
    A = [0] * N
    for i in range(N):
        A[i] = list(map(int, input().split()))
        A[i].pop(0)

    # 処理
    ans = 0
    for i in range(1, M+1):
        flag = True
        for j in range(N):
            if i not in A[j]:
                flag = False
        if flag:
            ans += 1

    # 出力
    print(ans)

=======
Suggestion 7

def main():
    N, M = map(int, input().split())
    A = []
    for i in range(N):
        A.append(list(map(int, input().split()))[1:])
    #print(A)
    ans = 0
    for i in range(1, M + 1):
        for j in range(N):
            if i not in A[j]:
                break
            if j == N - 1:
                ans += 1
    print(ans)

=======
Suggestion 8

def main():
    N, M = map(int, input().split())
    A = [list(map(int, input().split())) for i in range(N)]
    #print(A)
    ans = 0
    for i in range(1,M+1):
        cnt = 0
        for j in range(N):
            if i in A[j][1:]:
                cnt += 1
        if cnt == N:
            ans += 1
    print(ans)

=======
Suggestion 9

def solve():
    N, M = map(int, input().split())
    foods = [0] * M
    for _ in range(N):
        foods += map(int, input().split())
    print(len(set(foods)))
