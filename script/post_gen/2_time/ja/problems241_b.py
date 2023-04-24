Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A.sort()
    B.sort()
    i = 0
    for b in B:
        while i < N and A[i] < b:
            i += 1
        if i == N or A[i] != b:
            print("No")
            return
        i += 1
    print("Yes")

=======
Suggestion 2

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A.sort()
    B.sort()
    for i in range(M):
        if i == 0:
            if A[i] > B[i]:
                print("No")
                return
        else:
            if A[i] > B[i] or A[i-1] == A[i]:
                print("No")
                return
    print("Yes")

main()

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
            print('No')
            return
    print('Yes')

=======
Suggestion 4

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    a.sort()
    b.sort()
    for i in range(m):
        if a[i] > b[i]:
            print("No")
            return
    print("Yes")

=======
Suggestion 5

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    A.sort()
    B.sort()

    for b in B:
        if len(A) == 0:
            print("No")
            return
        if A[-1] < b:
            print("No")
            return
        while A[-1] > b:
            A.pop()
        A.pop()

    print("Yes")

=======
Suggestion 6

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    
    a.sort()
    b.sort()
    
    for i in range(m):
        if b[i] > a[i]:
            print('No')
            return
    print('Yes')

=======
Suggestion 7

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A.sort()
    B.sort()
    #print(A)
    #print(B)
    for i in range(M):
        if B[i] not in A:
            print("No")
            return
    print("Yes")
    return

=======
Suggestion 8

def main():
    # 入力
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    # 食事計画が可能かどうか
    for i in range(M):
        if B[i] not in A:
            print("No")
            exit()

    # 食事計画が可能な場合
    print("Yes")

=======
Suggestion 9

def main():
    N, M = map(int, input().split())
    A = sorted(list(map(int, input().split())))
    B = list(map(int, input().split()))
    for b in B:
        if b not in A:
            print("No")
            exit()
    print("Yes")

=======
Suggestion 10

def main():
    #入力
    N,M = map(int,input().split())
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))
    #初期化
    A.sort()
    B.sort()
    #処理
    for i in range(M):
        if B[i] not in A:
            print("No")
            return
    print("Yes")
