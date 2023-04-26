Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    a_dict = {}
    b_dict = {}
    for i in range(n):
        a_dict[a[i]] = i
        b_dict[b[i]] = i
    ans1 = 0
    ans2 = 0
    for i in range(n):
        if a_dict[a[i]] == b_dict[a[i]]:
            ans1 += 1
        elif a_dict[a[i]] != b_dict[a[i]]:
            ans2 += 1
    print(ans1)
    print(ans2)

=======
Suggestion 2

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    ans1 = 0
    ans2 = 0
    for i in range(n):
        for j in range(n):
            if a[i] == b[j]:
                if i == j:
                    ans1 += 1
                else:
                    ans2 += 1
    print(ans1)
    print(ans2)

=======
Suggestion 3

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    a_dict = {a[i]: i for i in range(n)}
    b_dict = {b[i]: i for i in range(n)}
    count = 0
    for i in range(n):
        if a[i] in b_dict:
            if a_dict[a[i]] == b_dict[a[i]]:
                count += 1
    print(count)
    count = 0
    for i in range(n):
        if a[i] in b_dict:
            if a_dict[a[i]] != b_dict[a[i]]:
                count += 1
    print(count)

=======
Suggestion 4

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    a_dic = {}
    b_dic = {}
    for i in range(n):
        a_dic[a[i]] = i
        b_dic[b[i]] = i
    count = 0
    for i in range(n):
        if a[i] in b_dic:
            if a_dic[a[i]] == b_dic[a[i]]:
                count += 1
    print(count)
    count = 0
    for i in range(n):
        if a[i] in b_dic:
            if a_dic[a[i]] != b_dic[a[i]]:
                count += 1
    print(count)

=======
Suggestion 5

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    a_dict = dict(zip(a, range(n)))
    b_dict = dict(zip(b, range(n)))
    count1 = 0
    count2 = 0
    for i in range(n):
        if a[i] in b_dict and a_dict[a[i]] == b_dict[a[i]]:
            count1 += 1
        if a[i] in b_dict and a_dict[a[i]] != b_dict[a[i]]:
            count2 += 1
    print(count1)
    print(count2)

=======
Suggestion 6

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    a = dict()
    b = dict()
    for i in range(N):
        a[A[i]] = i
        b[B[i]] = i
    count = 0
    for i in range(N):
        if A[i] == B[i]:
            count += 1
    print(count)
    count = 0
    for i in range(N):
        if A[i] in b and i != b[A[i]]:
            count += 1
    print(count)

main()

=======
Suggestion 7

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = [0] * N
    D = [0] * N
    for i in range(N):
        C[A[i] - 1] = i
        D[B[i] - 1] = i
    cnt = 0
    for i in range(N):
        if C[i] == D[i]:
            cnt += 1
    print(cnt)
    cnt = 0
    for i in range(N):
        if C[i] != D[i]:
            for j in range(i + 1, N):
                if C[i] == D[j] and C[j] == D[i]:
                    cnt += 1
    print(cnt)

=======
Suggestion 8

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    a = {}
    b = {}
    c = 0
    d = 0
    for i in range(N):
        a[A[i]] = i
        b[B[i]] = i
    for i in range(N):
        if A[i] in b:
            d += 1
            if a[A[i]] == b[A[i]]:
                c += 1
    print(c)
    print(d - c)

=======
Suggestion 9

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A.sort()
    B.sort()
    A_dict = {A[i]: i for i in range(N)}
    B_dict = {B[i]: i for i in range(N)}
    A_B_dict = {A[i]: B[i] for i in range(N)}
    A_B_dict2 = {B[i]: A[i] for i in range(N)}
    #print(A_dict)
    #print(B_dict)
    #print(A_B_dict)
    #print(A_B_dict2)
    count1 = 0
    count2 = 0
    for i in range(N):
        if A[i] == B[i]:
            count1 += 1
        elif A_B_dict[A[i]] == B[i]:
            count2 += 1
        elif A_B_dict2[B[i]] == A[i]:
            count2 += 1
    print(count1)
    print(count2)

=======
Suggestion 10

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    # Aの要素をkeyとして、Aの添字をvalueとした辞書を作成
    A_dict = {A[i]:i for i in range(N)}
    # Bの要素をkeyとして、Bの添字をvalueとした辞書を作成
    B_dict = {B[i]:i for i in range(N)}
    # 1.の条件を満たす整数の個数を格納する変数
    cnt1 = 0
    # 2.の条件を満たす整数の組の個数を格納する変数
    cnt2 = 0
    # Aの要素をkeyとして、Aの添字をvalueとした辞書を順番に見ていく
    for key in A_dict:
        # Bの要素をkeyとして、Bの添字をvalueとした辞書にkeyが含まれているか
        if key in B_dict:
            # Aの添字とBの添字が一致しているか
            if A_dict[key] == B_dict[key]:
                # 一致していたら1.の条件を満たすのでカウント
                cnt1 += 1
            # 一致していない場合は2.の条件を満たすのでカウント
            else:
                cnt2 += 1
    # 答えを出力
    print(cnt1)
    print(cnt2)

main()
