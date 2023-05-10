Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N, M = map(int, input().split())
    A = []
    B = []
    for i in range(M):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    A.sort()
    B.sort()
    if A[0] == 1 and B[-1] == N:
        print("Yes")
    else:
        print("No")

=======
Suggestion 2

def main():
    # n: 人数
    # m: 条件数
    n, m = map(int, input().split())

    # 条件を格納する配列
    conditions = []

    # 条件を配列に格納
    for i in range(m):
        a, b = map(int, input().split())
        conditions.append([a, b])

    # 人数分の配列を作成
    people = [i for i in range(1, n + 1)]

    # 条件を満たすかどうかのフラグ
    flag = False

    # 人を並べ替える
    for i in range(n - 1):
        # 条件を満たすかどうかのフラグ
        flag = False

        # 条件を満たす人がいるかどうか
        for condition in conditions:
            # 条件を満たす人がいればフラグを立てる
            if people[i] == condition[0] and people[i + 1] == condition[1]:
                flag = True

        # 条件を満たす人がいなければ、人を並べ替える
        if not flag:
            people[i], people[i + 1] = people[i + 1], people[i]

    # 条件を満たすかどうかのフラグ
    flag = True

    # 条件を満たす人がいるかどうか
    for condition in conditions:
        # 条件を満たす人がいなければフラグを下げる
        if people[condition[0] - 1] != condition[0] or people[condition[1] - 1] != condition[1]:
            flag = False

    # 条件を満たすかどうかを出力する
    if flag:
        print('Yes')
    else:
        print('No')

=======
Suggestion 3

def main():
    n, m = map(int, input().split())
    a = [0 for _ in range(m)]
    b = [0 for _ in range(m)]
    for i in range(m):
        a[i], b[i] = map(int, input().split())
    a.sort()
    b.sort()
    for i in range(m):
        if a[i] == 1:
            print('POSSIBLE')
            exit()
    for i in range(m):
        if b[i] == n:
            print('POSSIBLE')
            exit()
    print('IMPOSSIBLE')

=======
Suggestion 4

def main():
    N, M = map(int, input().split())
    A = []
    B = []
    for i in range(M):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    A.sort()
    B.sort()
    if A[0] == 1 and B[-1] == N:
        print('Yes')
    else:
        print('No')

=======
Suggestion 5

def main():
    N, M = map(int, input().split())
    A = []
    B = []
    for _ in range(M):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    A.sort()
    B.sort()
    if A[0] == 1 and B[-1] == N:
        print('POSSIBLE')
    else:
        print('IMPOSSIBLE')

=======
Suggestion 6

def main():
    n,m = map(int,input().split())
    a = [0]*m
    b = [0]*m
    for i in range(m):
        a[i],b[i] = map(int,input().split())
    a.sort()
    b.sort()
    if a[0] == 1 and b[m-1] == n:
        print("POSSIBLE")
    else:
        print("IMPOSSIBLE")

=======
Suggestion 7

def main():
    N, M = map(int, input().split())
    A = []
    B = []
    for i in range(M):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)

    #print(N, M)
    #print(A)
    #print(B)

    A.sort()
    B.sort()
    #print(A)
    #print(B)

    if A[0] == 1 and B[M-1] == N and B[0] - A[M-1] >= 2:
        print("Yes")
    else:
        print("No")

=======
Suggestion 8

def main():
    n,m=map(int, input().split())
    a=[]
    b=[]
    for _ in range(m):
        ai,bi=map(int, input().split())
        a.append(ai)
        b.append(bi)
    a.sort()
    b.sort()
    if a[0]==1 and b[-1]==n:
        print("POSSIBLE")
    else:
        print("IMPOSSIBLE")
