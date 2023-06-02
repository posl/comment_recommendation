Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = list(map(int, input().split()))
    num = 0
    for i in range(N):
        num += B.count(C[A[i]-1])
    print(num)

=======
Suggestion 2

def main():
    n = int(input())
    a = [int(x) for x in input().split()]
    b = [int(x) for x in input().split()]
    c = [int(x) for x in input().split()]
    d = [0] * n
    e = [0] * n
    f = [0] * n
    for i in range(n):
        d[a[i] - 1] += 1
        e[b[c[i] - 1] - 1] += 1
        f[c[i] - 1] += 1
    ans = 0
    for i in range(n):
        ans += d[i] * e[i]
    print(ans)

=======
Suggestion 3

def find_pairs(A, B, C):
    A = [a-1 for a in A]
    B = [b-1 for b in B]
    C = [c-1 for c in C]
    #print(A, B, C)
    C_dict = {}
    for i, c in enumerate(C):
        if c not in C_dict:
            C_dict[c] = []
        C_dict[c].append(i)
    #print(C_dict)
    count = 0
    for i, a in enumerate(A):
        if B[a] in C_dict:
            count += len(C_dict[B[a]])
    return count

=======
Suggestion 4

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = list(map(int, input().split()))

    b_dict = {}
    for i in range(n):
        b_dict[b[i]] = b_dict.get(b[i], 0) + 1

    c_dict = {}
    for i in range(n):
        c_dict[c[i]] = c_dict.get(c[i], 0) + 1

    b_c = {}
    for i in range(n):
        b_c[b[i]] = b_c.get(b[i], []) + [c[i]]

    c_a = {}
    for i in range(n):
        c_a[c[i]] = c_a.get(c[i], []) + [a[i]]

    c_a_count = {}
    for k, v in c_a.items():
        c_a_count[k] = {}
        for i in v:
            c_a_count[k][i] = c_a_count[k].get(i, 0) + 1

    count = 0
    for k, v in b_dict.items():
        if k in b_c:
            for i in b_c[k]:
                if i in c_dict:
                    count += b_dict[k] * c_dict[i]
                    if i in c_a_count:
                        count -= b_dict[k] * c_a_count[i][k]

    print(count)

=======
Suggestion 5

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = list(map(int, input().split()))

    # Aの各要素の値をキーにして、出現回数を値にした辞書を作成
    D = {}
    for i in range(N):
        if A[i] not in D:
            D[A[i]] = 1
        else:
            D[A[i]] += 1

    # Cの各要素の値をキーにして、出現回数を値にした辞書を作成
    E = {}
    for i in range(N):
        if C[i] not in E:
            E[C[i]] = 1
        else:
            E[C[i]] += 1

    # Aの要素とCの要素のペアで、Aの要素がキーになっている辞書の値と、Cの要素がキーになっている辞書の値の積を求める
    ans = 0
    for i in range(N):
        if B[i] in D and C[i] in E:
            ans += D[B[i]] * E[C[i]]

    print(ans)

=======
Suggestion 6

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = list(map(int, input().split()))
    D = [0] * (N + 1)
    for i in range(N):
        D[C[i]] += 1
    ans = 0
    for i in range(N):
        ans += D[B[A[i] - 1]]
    print(ans)

=======
Suggestion 7

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = list(map(lambda x: int(x) - 1, input().split()))
    d = [0 for _ in range(n)]
    for i in range(n):
        d[b[c[i]]] += 1
    ans = 0
    for i in range(n):
        ans += d[a[i]]
    print(ans)

=======
Suggestion 8

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = list(map(int, input().split()))

    # 1. 暴力解法
    # count = 0
    # for i in range(n):
    #     for j in range(n):
    #         if a[i] == b[c[j]-1]:
    #             count += 1
    # print(count)

    # 2. 优化
    # a_dic = {}
    # for i in range(n):
    #     a_dic[i+1] = a[i]
    # count = 0
    # for i in range(n):
    #     if a_dic[b[c[i]-1]] == b[c[i]-1]:
    #         count += 1
    # print(count)

    # 3. 优化
    c_dic = {}
    for i in range(n):
        c_dic[i+1] = c[i]
    count = 0
    for i in range(n):
        if a[b[c_dic[i+1]-1]-1] == b[c_dic[i+1]-1]:
            count += 1
    print(count)

=======
Suggestion 9

def main():
    N = int(input())
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))
    C = list(map(int,input().split()))
    cnt = 0
    for i in range(N):
        cnt += B.count(C[A[i]-1])
    print(cnt)

=======
Suggestion 10

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = list(map(int, input().split()))

    # A = [1, 2, 2]
    # B = [3, 1, 2]
    # C = [2, 3, 2]
    # N = 3

    # A = [1, 1, 1, 1]
    # B = [1, 1, 1, 1]
    # C = [1, 2, 3, 4]
    # N = 4

    # A = [2, 3, 3]
    # B = [1, 3, 3]
    # C = [1, 1, 1]
    # N = 3

    # N = 10**5
    # A = [1 for i in range(N)]
    # B = [1 for i in range(N)]
    # C = [i+1 for i in range(N)]

    # print(N)
    # print(A)
    # print(B)
    # print(C)

    # N = 3
    # A = [1, 2, 2]
    # B = [3, 1, 2]
    # C = [2, 3, 2]

    # N = 4
    # A = [1, 1, 1, 1]
    # B = [1, 1, 1, 1]
    # C = [1, 2, 3, 4]

    # N = 3
    # A = [2, 3, 3]
    # B = [1, 3, 3]
    # C = [1, 1, 1]

    # N = 10**5
    # A = [1 for i in range(N)]
    # B = [1 for i in range(N)]
    # C = [i+1 for i in range(N)]

    # print(N)
    # print(A)
    # print(B)
    # print(C)

    # N = 10**5
    # A = [1 for i in range(N)]
    # B = [1 for i in range
