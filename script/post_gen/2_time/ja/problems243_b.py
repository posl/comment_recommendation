Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A_dict = {A[i]: i for i in range(N)}
    B_dict = {B[i]: i for i in range(N)}
    count1 = 0
    count2 = 0
    for i in range(N):
        if A[i] in B_dict and A_dict[A[i]] == B_dict[A[i]]:
            count1 += 1
        if A[i] in B_dict and A_dict[A[i]] != B_dict[A[i]]:
            count2 += 1
    print(count1)
    print(count2)

=======
Suggestion 2

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    dictA = {}
    dictB = {}
    for i in range(N):
        dictA[A[i]] = i
        dictB[B[i]] = i
    count = 0
    for i in range(N):
        if A[i] in dictB and dictB[A[i]] == i:
            count += 1
    print(count)
    count = 0
    for i in range(N):
        if A[i] in dictB and dictB[A[i]] != i:
            count += 1
    print(count)

=======
Suggestion 3

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    A_dict = {a: i for i, a in enumerate(A)}
    B_dict = {b: i for i, b in enumerate(B)}

    A_B_dict = {a: B_dict[a] for a in A_dict.keys() & B_dict.keys()}
    A_B_list = list(A_B_dict.items())

    A_B_list.sort(key=lambda x: x[1])

    A_B_list = [a for a, b in A_B_list]

    A_B_list = [a for a in A_B_list if A_dict[a] == B_dict[a]]

    print(len(A_B_list))
    print(len(A_B_dict) - len(A_B_list))

=======
Suggestion 4

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    a = [0] * N
    b = [0] * N
    for i in range(N):
        a[i] = A[i]
        b[i] = B[i]
    a.sort()
    b.sort()
    i = 0
    j = 0
    cnt = 0
    while i < N and j < N:
        if a[i] == b[j]:
            cnt += 1
            i += 1
            j += 1
        elif a[i] < b[j]:
            i += 1
        else:
            j += 1
    print(cnt)
    print(N - cnt)

=======
Suggestion 5

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    a = set(A)
    b = set(B)
    c = a&b
    d = a^b
    print(len(c))
    print(len(d))

=======
Suggestion 6

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    a2b = [0] * (n + 1)
    b2a = [0] * (n + 1)
    for i in range(n):
        a2b[a[i]] = i
        b2a[b[i]] = i
    ans1 = 0
    ans2 = 0
    for i in range(n):
        if a[i] == b[i]:
            ans1 += 1
        elif a2b[b[i]] == i:
            ans2 += 1
    print(ans1)
    print(ans2)

=======
Suggestion 7

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    #print(N)
    #print(A)
    #print(B)
    #print(A[0])
    #print(B[0])
    #print(A[0] == B[0])
    #print(A[0] == B[1])
    #print(A[1] == B[0])
    #print(A[1] == B[1])
    #print(A[1] == B[2])
    #print(A[2] == B[1])
    #print(A[2] == B[2])
    #print(A[2] == B[3])
    #print(A[3] == B[2])
    #print(A[3] == B[3])
    #print(A[3] == B[4])
    #print(A[4] == B[3])
    #print(A[4] == B[4])
    #print(A[4] == B[5])
    #print(A[5] == B[4])
    #print(A[5] == B[5])
    #print(A[5] == B[6])
    #print(A[6] == B[5])
    #print(A[6] == B[6])
    #print(A[6] == B[7])
    #print(A[7] == B[6])
    #print(A[7] == B[7])
    #print(A[7] == B[8])
    #print(A[8] == B[7])
    #print(A[8] == B[8])
    #print(A[8] == B[9])
    #print(A[9] == B[8])
    #print(A[9] == B[9])
    #print(A[9] == B[10])
    #print(A[10] == B[9])
    #print(A[10] == B[10])
    #print(A[10] == B[11])
    #print(A[11] == B[10])
    #print(A[11] == B[11])
    #print(A[11] == B[12])
    #print(A[12] == B[11])
    #print(A[12] == B

=======
Suggestion 8

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    #Aの要素をkey、インデックスをvalueにした辞書
    A_dic = {A[i]: i for i in range(N)}
    #Bの要素をkey、インデックスをvalueにした辞書
    B_dic = {B[i]: i for i in range(N)}
    #AにもBにも含まれ、その位置も一致している整数の個数
    count_match = 0
    #AにもBにも含まれるが、その位置は異なる整数の個数
    count_diff = 0
    #AにもBにも含まれるが、その位置は異なる整数の組のリスト
    diff_list = []
    #AにもBにも含まれるが、その位置は異なる整数の組のリストを作成
    for i in range(N):
        if A[i] in B:
            if A_dic[A[i]] == B_dic[A[i]]:
                count_match += 1
            else:
                diff_list.append((A[i], B[B_dic[A[i]]]))
    #diff_listから重複を除く
    diff_list = list(set(diff_list))
    #AにもBにも含まれるが、その位置は異なる整数の個数
    count_diff = len(diff_list)
    #出力
    print(count_match)
    print(count_diff)

=======
Suggestion 9

def main():
    #入力
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    #問題文の通りに実装
    ans1 = 0
    ans2 = 0
    for i in range(N):
        for j in range(N):
            if A[i] == B[j] and i == j:
                ans1 += 1
            if A[i] == B[j] and i != j:
                ans2 += 1
    #出力
    print(ans1)
    print(ans2)

=======
Suggestion 10

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    # A と B の各要素を値とする辞書を作成
    dict_A = {A[i]: i for i in range(N)}
    dict_B = {B[i]: i for i in range(N)}

    # 1. A にも B にも含まれ、その位置も一致している整数の個数
    count = 0
    for i in range(N):
        if dict_A[B[i]] == i:
            count += 1
    print(count)

    # 2. A にも B にも含まれるが、その位置は異なる整数の個数
    count = 0
    for i in range(N):
        for j in range(i+1, N):
            if dict_A[B[i]] == j and dict_B[A[i]] == j:
                count += 1
    print(count)
