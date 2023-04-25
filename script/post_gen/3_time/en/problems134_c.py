Synthesizing 9/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    A = [int(input()) for _ in range(N)]
    maxA = max(A)
    for i in range(N):
        if A[i] == maxA:
            print(max(A[:i] + A[i + 1:]))
        else:
            print(maxA)

=======
Suggestion 2

def main():
    N = int(input())
    A = [int(input()) for _ in range(N)]
    maxA = max(A)
    A.remove(maxA)
    maxA2 = max(A)
    for i in range(N):
        if A[i] == maxA:
            print(maxA2)
        else:
            print(maxA)

=======
Suggestion 3

def main():
    N = int(input())
    A = [int(input()) for _ in range(N)]
    max_a = max(A)
    for a in A:
        if a == max_a:
            print(max(A[:A.index(a)] + A[A.index(a) + 1:]))
        else:
            print(max_a)

=======
Suggestion 4

def main():
    n = int(input())
    a = [int(input()) for _ in range(n)]
    a_max = max(a)
    a_min = min(a)
    a_max_count = a.count(a_max)
    a_min_count = a.count(a_min)
    if a_max == a_min:
        for _ in range(n):
            print(a_max)
    else:
        for i in range(n):
            if a[i] == a_max:
                if a_max_count == 1:
                    print(a_min)
                else:
                    print(a_max)
            else:
                print(a_max)

=======
Suggestion 5

def main():
    n = int(input())
    a = [int(input()) for _ in range(n)]
    max_a = max(a)
    max_a_count = a.count(max_a)
    if max_a_count == 1:
        for i in range(n):
            if a[i] == max_a:
                print(max(a[:i] + a[i + 1:]))
            else:
                print(max_a)
    else:
        for i in range(n):
            print(max_a)

=======
Suggestion 6

def main():
    n = int(input())
    a = [int(input()) for _ in range(n)]
    max_a = max(a)
    max_a_idx = a.index(max_a)
    a.pop(max_a_idx)
    max_a2 = max(a)
    for i in range(n):
        if i == max_a_idx:
            print(max_a2)
        else:
            print(max_a)

=======
Suggestion 7

def main():
    N = int(input())
    A = [int(input()) for _ in range(N)]
    maxA = max(A)
    for a in A:
        if a == maxA:
            maxA2 = max(A)
        else:
            maxA2 = maxA
        print(maxA2)

=======
Suggestion 8

def main():
    N = int(input())
    A = [int(input()) for _ in range(N)]
    maxA = max(A)
    maxAindex = A.index(maxA)
    A.pop(maxAindex)
    maxA2 = max(A)
    for i in range(N):
        if i == maxAindex:
            print(maxA2)
        else:
            print(maxA)

main()

=======
Suggestion 9

def main():
    #入力
    N = int(input())
    A = [int(input()) for _ in range(N)]

    #Aの最大値を求める
    maxA = max(A)
    #Aの最大値のインデックスを求める
    maxA_index = A.index(maxA)

    #Aの最大値を除いた最大値を求める
    maxA2 = max(A[:maxA_index] + A[maxA_index+1:])

    #出力
    for i in range(N):
        if i == maxA_index:
            print(maxA2)
        else:
            print(maxA)
