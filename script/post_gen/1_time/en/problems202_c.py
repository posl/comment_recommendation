Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        for j in range(N):
            if A[i] == B[C[j]-1]:
                ans += 1
    print(ans)

=======
Suggestion 2

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = list(map(int, input().split()))
    count = 0
    for i in range(N):
        for j in range(N):
            if A[i] == B[C[j]-1]:
                count += 1
    print(count)

=======
Suggestion 3

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = list(map(int, input().split()))
    #print(A)
    #print(B)
    #print(C)
    #print(N)
    #print(len(A))
    #print(len(B))
    #print(len(C))
    #print(A[0])
    #print(A[1])
    #print(A[2])
    #print(B[0])
    #print(B[1])
    #print(B[2])
    #print(C[0])
    #print(C[1])
    #print(C[2])
    #print(A[0] == B[C[0]])
    #print(A[0] == B[C[1]])
    #print(A[0] == B[C[2]])
    #print(A[1] == B[C[0]])
    #print(A[1] == B[C[1]])
    #print(A[1] == B[C[2]])
    #print(A[2] == B[C[0]])
    #print(A[2] == B[C[1]])
    #print(A[2] == B[C[2]])
    #print(A[0] == B[C[0]] or A[0] == B[C[1]] or A[0] == B[C[2]])
    #print(A[1] == B[C[0]] or A[1] == B[C[1]] or A[1] == B[C[2]])
    #print(A[2] == B[C[0]] or A[2] == B[C[1]] or A[2] == B[C[2]])
    #print(A[0] == B[C[0]] or A[0] == B[C[1]] or A[0] == B[C[2]] or A[1] == B[C[0]] or A[1] == B[C[1]] or A[1] == B[C[2]] or A[2] == B[C[0]] or A[2] == B[C[1]] or A[2] == B[C[2]])
    #print(A[0] == B[C[0]])
    #print(A[0] == B[C[1]])
    #print(A[0] == B

=======
Suggestion 4

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = list(map(int, input().split()))

    B_C = [0] * (N + 1)
    for i in range(N):
        B_C[C[i]] += 1

    B_C_S = [0] * (N + 1)
    for i in range(1, N + 1):
        B_C_S[i] = B_C_S[i - 1] + B_C[i]

    ans = 0
    for i in range(N):
        ans += B_C_S[B[A[i]]]

    print(ans)

=======
Suggestion 5

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = list(map(int, input().split()))
    C = [B[x-1] for x in C]
    print(sum(A.count(x) for x in C))

=======
Suggestion 6

def solve():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = list(map(int, input().split()))
    
    B_count = [0] * N
    for b in B:
        B_count[b - 1] += 1

    C_count = [0] * N
    for c in C:
        C_count[c - 1] += 1

    ans = 0
    for a in A:
        ans += B_count[a - 1] * C_count[a - 1]

    return ans

=======
Suggestion 7

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = list(map(int, input().split()))

    B2C = {}
    for i in range(N):
        if B[i] in B2C:
            B2C[B[i]].append(C[i])
        else:
            B2C[B[i]] = [C[i]]

    ans = 0
    for i in range(N):
        if A[i] in B2C:
            ans += len(B2C[A[i]])

    print(ans)

=======
Suggestion 8

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = list(map(int, input().split()))
    # N = 10**5
    # A = [1]*N
    # B = [1]*N
    # C = [1]*N

    # Bの値ごとのインデックスを取得
    B_idx = [[] for _ in range(N)]
    for i, b in enumerate(B):
        B_idx[b-1].append(i)

    # AとCの値が一致するときのBのインデックスの組み合わせを取得
    ans = 0
    for a in A:
        ans += len(B_idx[C[a-1]-1])
    print(ans)

=======
Suggestion 9

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = list(map(int, input().split()))

    #Bの各要素に対して、Cの何番目にあるかを記録しておく
    C_dict = {}
    for i in range(N):
        if B[C[i] - 1] in C_dict:
            C_dict[B[C[i] - 1]].append(i + 1)
        else:
            C_dict[B[C[i] - 1]] = [i + 1]

    #Aの各要素に対して、Cの何番目にあるかを記録しておく
    A_dict = {}
    for i in range(N):
        if A[i] in C_dict:
            if A[i] in A_dict:
                A_dict[A[i]].extend(C_dict[A[i]])
            else:
                A_dict[A[i]] = C_dict[A[i]]

    #A_dictの各要素に対して、Cの何番目にあるかを記録しておく
    ans = 0
    for i in range(N):
        if A[i] in A_dict:
            ans += len(A_dict[A[i]])

    print(ans)

=======
Suggestion 10

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = list(map(int, input().split()))

    # Bの値でソートしたときのインデックスを保持
    B_sorted = sorted(enumerate(B), key=lambda x: x[1])

    # Cの値でソートしたときのインデックスを保持
    C_sorted = sorted(enumerate(C), key=lambda x: x[1])

    # Cの値でソートしたときのインデックスを保持
    A_sorted = sorted(enumerate(A), key=lambda x: x[1])

    # Bの値でソートしたときのインデックスを保持
    B_sorted = sorted(enumerate(B), key=lambda x: x[1])

    # Cの値でソートしたときのインデックスを保持
    C_sorted = sorted(enumerate(C), key=lambda x: x[1])

    # Bの値でソートしたときのインデックスを保持
    B_sorted = sorted(enumerate(B), key=lambda x: x[1])

    # Cの値でソートしたときのインデックスを保持
    C_sorted = sorted(enumerate(C), key=lambda x: x[1])

    # Bの値でソートしたときのインデックスを保持
    B_sorted = sorted(enumerate(B), key=lambda x: x[1])

    # Cの値でソートしたときのインデックスを保持
    C_sorted = sorted(enumerate(C), key=lambda x: x[1])

    # Bの値でソートしたときのインデックスを保持
    B_sorted = sorted(enumerate(B), key=lambda x: x[1])

    # Cの値でソートしたときのインデックスを保持
    C_sorted = sorted(enumerate(C), key=lambda x: x[1])

    # Bの値でソートしたときのインデックスを保持
    B_sorted = sorted(enumerate(B
