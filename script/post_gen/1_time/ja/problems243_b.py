Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A_dict = {}
    B_dict = {}
    for i in range(N):
        A_dict[A[i]] = i
        B_dict[B[i]] = i
    count1 = 0
    count2 = 0
    for i in range(N):
        if A_dict[A[i]] == B_dict[A[i]]:
            count1 += 1
        else:
            count2 += 1
    print(count1)
    print(count2)

=======
Suggestion 2

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    a_dict = {}
    b_dict = {}
    for i in range(n):
        a_dict[a[i]] = i
        b_dict[b[i]] = i
    count1 = 0
    count2 = 0
    for i in range(n):
        if a[i] in b_dict:
            if a_dict[a[i]] == b_dict[a[i]]:
                count1 += 1
            else:
                count2 += 1
    print(count1)
    print(count2)

=======
Suggestion 3

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A_dict = {A[i]: i for i in range(N)}
    B_dict = {B[i]: i for i in range(N)}
    A_B = [A_dict[i] for i in B if i in A_dict]
    B_A = [B_dict[i] for i in A if i in B_dict]
    print(len(set(A_B)))
    print(len(set(A_B) & set(B_A)))

=======
Suggestion 4

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    a_dict = {a[i]: i for i in range(n)}
    b_dict = {b[i]: i for i in range(n)}
    ans1 = 0
    ans2 = 0
    for i in range(n):
        if a[i] == b[i]:
            ans1 += 1
        elif a_dict[b[i]] == i:
            ans2 += 1
    print(ans1)
    print(ans2)

=======
Suggestion 5

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    a_dict = {a[i]:i for i in range(n)}
    b_dict = {b[i]:i for i in range(n)}
    count = 0
    for i in range(n):
        if a_dict[a[i]] == b_dict[a[i]]:
            count += 1
    print(count)
    count = 0
    for i in range(n):
        if a_dict[a[i]] != b_dict[a[i]]:
            count += 1
    print(count)

=======
Suggestion 6

def main():
    N = int(input())
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))
    A_dict = {A[i]:i for i in range(N)}
    B_dict = {B[i]:i for i in range(N)}
    count = 0
    for i in range(N):
        if A[i] == B[i]:
            count += 1
    print(count)
    count = 0
    for i in range(N):
        if A[i] in B_dict and A_dict[A[i]] != B_dict[A[i]]:
            count += 1
    print(count)

=======
Suggestion 7

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    a_dic = {a[i]: i for i in range(n)}
    b_dic = {b[i]: i for i in range(n)}
    count1 = 0
    count2 = 0
    for i in range(n):
        if a[i] in b_dic:
            if a_dic[a[i]] == b_dic[a[i]]:
                count1 += 1
            else:
                count2 += 1
    print(count1)
    print(count2)

=======
Suggestion 8

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    A_dict = dict()
    B_dict = dict()
    for i in range(N):
        A_dict[A[i]] = i
        B_dict[B[i]] = i

    count = 0
    for i in range(N):
        if A[i] == B[i]:
            count += 1

    print(count)

    count = 0
    for i in range(N):
        if A_dict[A[i]] != B_dict[A[i]]:
            count += 1

    print(count)

=======
Suggestion 9

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    a = {a: i for i, a in enumerate(A)}
    b = {b: i for i, b in enumerate(B)}
    c = {a: b for a, b in a.items() if a in b}
    print(len(c))
    print(sum([1 for a, b in a.items() if a in b and a[b] != b[a]]))

=======
Suggestion 10

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    # Aの要素はすべて異なる
    # Bの要素もすべて異なる
    # A_i = B_i を満たす整数 i の個数
    # A_i = B_j, i ≠ j を満たす整数の組 (i, j) の個数
    # A にも B にも含まれ、その位置も一致している整数の個数
    # A にも B にも含まれるが、その位置は異なる整数の個数

    # A_i = B_i を満たす整数 i の個数
    # A にも B にも含まれ、その位置も一致している整数の個数
    # A_i = B_j, i ≠ j を満たす整数の組 (i, j) の個数
    # A にも B にも含まれるが、その位置は異なる整数の個数

    # A_i = B_i を満たす整数 i の個数
    # A にも B にも含まれ、その位置も一致している整数の個数
    # A_i = B_j, i ≠ j を満たす整数の組 (i, j) の個数
    # A にも B にも含まれるが、その位置は異なる整数の個数

    # A_i = B_i を満たす整数 i の個数
    # A にも B にも含まれ、その位置も一致している整数の個数
    # A_i = B_j, i ≠ j を満たす整数の組 (i, j) の個数
    # A にも B にも含まれるが、その位置は異なる整
