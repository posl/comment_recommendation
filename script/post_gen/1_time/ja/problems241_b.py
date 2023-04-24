Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A.sort()
    B.sort()
    for i in range(M):
        if A[i] != B[i]:
            print("No")
            return
    print("Yes")

=======
Suggestion 2

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A.sort()
    B.sort()
    i = 0
    j = 0
    while i < N and j < M:
        if A[i] == B[j]:
            i += 1
            j += 1
        elif A[i] < B[j]:
            i += 1
        else:
            j += 1
    if j == M:
        print("Yes")
    else:
        print("No")

=======
Suggestion 3

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A.sort()
    B.sort()
    for i in range(M):
        if B[i] not in A:
            print("No")
            return
    print("Yes")

=======
Suggestion 4

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    A.sort()
    B.sort()

    for i in range(M):
        if B[i] < A[0]:
            print("No")
            return
        elif B[i] > A[N-1]:
            print("No")
            return
        else:
            a = 0
            b = N-1
            while True:
                c = (a+b)//2
                if A[c] == B[i]:
                    print("No")
                    return
                elif A[c] > B[i]:
                    if A[c-1] < B[i]:
                        print("No")
                        return
                    else:
                        b = c
                elif A[c] < B[i]:
                    if A[c+1] > B[i]:
                        print("Yes")
                        break
                    else:
                        a = c
    return

=======
Suggestion 5

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    
    A.sort()
    B.sort()
    
    for i in range(M):
        if B[i] in A:
            A.remove(B[i])
        else:
            print("No")
            return
        
    print("Yes")

=======
Suggestion 6

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A.sort()
    B.sort()
    ans = 'Yes'
    for i in range(M):
        if B[i] not in A:
            ans = 'No'
            break
    print(ans)

=======
Suggestion 7

def main():
    # 1行目
    N, M = map(int, input().split())
    # 2行目
    A = list(map(int, input().split()))
    # 3行目
    B = list(map(int, input().split()))

    # Aの中にBの要素があるかどうかを判定する。
    # あればYes、なければNo
    if all([b in A for b in B]):
        print("Yes")
    else:
        print("No")

=======
Suggestion 8

def main():
    import sys
    from bisect import bisect_left
    input = sys.stdin.readline
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A.sort()
    for b in B:
        if bisect_left(A, b) == N or A[bisect_left(A, b)] != b:
            print("No")
            return
    print("Yes")

=======
Suggestion 9

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A.sort() #ソート
    B.sort() #ソート
    i = 0
    j = 0
    while i < N and j < M:
        if A[i] == B[j]:
            i += 1
            j += 1
        elif A[i] > B[j]:
            print("No")
            return
        else:
            i += 1
    if j == M:
        print("Yes")
    else:
        print("No")

=======
Suggestion 10

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    # Aの中にBの要素があればYesを出力
    if set(B) <= set(A):
        print("Yes")
    else:
        print("No")
