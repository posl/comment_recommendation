Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, M = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(M)]
    CD = [list(map(int, input().split())) for _ in range(M)]
    for i in range(N):
        for j in range(i+1, N):
            AB[i][j] = AB[j][i] = 0
            CD[i][j] = CD[j][i] = 0
    for i in range(M):
        AB[AB[i][0]-1][AB[i][1]-1] = 1
        CD[CD[i][0]-1][CD[i][1]-1] = 1
    for i in range(N):
        for j in range(i+1, N):
            AB[i][j] = AB[j][i] = 0
            CD[i][j] = CD[j][i] = 0
    if AB == CD:
        print("Yes")
    else:
        print("No")

=======
Suggestion 2

def main():
    N, M = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(M)]
    CD = [list(map(int, input().split())) for _ in range(M)]
    for p in permutations(range(1, N + 1)):
        ok = True
        for a, b in AB:
            if (p[a - 1], p[b - 1]) not in CD:
                ok = False
                break
        if ok:
            print('Yes')
            return
    print('No')

=======
Suggestion 3

def main():
    N, M = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(M)]
    CD = [list(map(int, input().split())) for _ in range(M)]

    for i in range(N):
        for j in range(i + 1, N):
            for k in range(N):
                for l in range(k + 1, N):
                    flag = True
                    for a, b in AB:
                        if (a == i + 1 and b == j + 1) or (a == j + 1 and b == i + 1):
                            if not ((k + 1, l + 1) in CD or (l + 1, k + 1) in CD):
                                flag = False
                                break
                        elif (a == k + 1 and b == l + 1) or (a == l + 1 and b == k + 1):
                            if not ((i + 1, j + 1) in CD or (j + 1, i + 1) in CD):
                                flag = False
                                break
                    if flag:
                        print('Yes')
                        return
    print('No')

main()

=======
Suggestion 4

def main():
    N, M = map(int, input().split())
    AB = [tuple(map(int, input().split())) for _ in range(M)]
    CD = [tuple(map(int, input().split())) for _ in range(M)]
    for p in permutations(range(1, N + 1)):
        if all(AB[i] in CD[p[i - 1] - 1] for i in range(1, N + 1)):
            print('Yes')
            exit()
    print('No')

=======
Suggestion 5

def main():
    N, M = map(int, input().split())
    AB = [tuple(map(int, input().split())) for _ in range(M)]
    CD = [tuple(map(int, input().split())) for _ in range(M)]
    for p in permutations(range(1, N+1)):
        if all(AB[i] in CD[p.index(j)] for i, j in enumerate(p)):
            print("Yes")
            return
    print("No")

=======
Suggestion 6

def main():
    N, M = map(int, input().split())
    A = [0] * M
    B = [0] * M
    C = [0] * M
    D = [0] * M
    for i in range(M):
        A[i], B[i] = map(int, input().split())
    for i in range(M):
        C[i], D[i] = map(int, input().split())

    for i in range(M):
        for j in range(M):
            if A[i] == C[j] and B[i] == D[j]:
                print("Yes")
                exit()
    print("No")

=======
Suggestion 7

def main():
    n, m = map(int, input().split())
    ab = [tuple(map(int, input().split())) for _ in range(m)]
    cd = [tuple(map(int, input().split())) for _ in range(m)]
    for p in permutations(range(1, n + 1)):
        if all(ab[i] in zip(p, p) or ab[i] in zip(p, p[::-1]) for i in range(m)) and all(cd[i] in zip(p, p) or cd[i] in zip(p, p[::-1]) for i in range(m)):
            print('Yes')
            break
    else:
        print('No')

=======
Suggestion 8

def main():
    N, M = map(int, input().split())
    AB = [list(map(int, input().split())) for i in range(M)]
    CD = [list(map(int, input().split())) for i in range(M)]

    # 高橋君のおもちゃのボールを結ぶひもの数
    A = [0] * N
    # 青木君のおもちゃのボールを結ぶひもの数
    C = [0] * N

    for a, b in AB:
        A[a-1] += 1
        A[b-1] += 1

    for c, d in CD:
        C[c-1] += 1
        C[d-1] += 1

    if A == C:
        print('Yes')
    else:
        print('No')

=======
Suggestion 9

def main():
    N, M = map(int, input().split())
    if M == 0:
        print('Yes')
        return
    AB = [list(map(int, input().split())) for _ in range(M)]
    CD = [list(map(int, input().split())) for _ in range(M)]
    AB.sort()
    CD.sort()
    for P in permutations(range(1, N+1)):
        for ab in AB:
            if ab not in [(P[ab[0]-1], P[ab[1]-1]), (P[ab[1]-1], P[ab[0]-1])]:
                break
        else:
            print('Yes')
            return
    print('No')

=======
Suggestion 10

def main():
    n, m = map(int, input().split())
    # m = 0のときは、全てのボールが繋がっていることになるのでYes
    if m == 0:
        print("Yes")
        return
    # a, b, c, dについて、i本目のひもがボールa[i]とボールb[i]を結ぶ、ボールc[i]とボールd[i]を結ぶという情報を格納する
    a = []
    b = []
    c = []
    d = []
    for _ in range(m):
        a_i, b_i = map(int, input().split())
        a.append(a_i)
        b.append(b_i)
    for _ in range(m):
        c_i, d_i = map(int, input().split())
        c.append(c_i)
        d.append(d_i)
    # ボール1から順番に、ボール1, 2, 3, ..., nを並べ替えたものを考える
    # このとき、ボール1, 2, 3, ..., nを並べ替えたものをPとする
    # 2人のおもちゃが同じ形かどうかは、Pを固定して、a, b, c, dを全て調べることで判定できる
    # つまり、Pを固定して、a, b, c, dを全て調べることで、2人のおもちゃが同じ形かどうかを判定できる
    # このとき、a, b, c, dのうち、ボール1, 2, 3, ..., nを結ぶひもがあるかどうかを調べることで、Pを固定して、a, b, c, dを全て調べることができる
    # このとき、ボール1, 2
