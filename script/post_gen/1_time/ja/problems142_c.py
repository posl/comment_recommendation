Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = [0] * N
    for i in range(N):
        ans[A[i] - 1] = i + 1
    for i in range(N):
        print(ans[i], end=" ")

=======
Suggestion 2

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = [0] * N
    for i in range(N):
        B[A[i] - 1] = i + 1
    for i in range(N):
        print(B[i], end=" ")

main()

=======
Suggestion 3

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = [0] * N
    for i in range(N):
        B[A[i] - 1] = i + 1
    print(' '.join(map(str, B)))

=======
Suggestion 4

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = [0] * N
    for i in range(N):
        B[A[i] - 1] = i + 1
    print(*B)

=======
Suggestion 5

def main():
    n = int(input())
    a = list(map(int,input().split()))
    ans = [0]*n
    for i in range(n):
        ans[a[i]-1] = i+1
    print(*ans)

=======
Suggestion 6

def main():
    N = int(input())
    A = list(map(int,input().split()))
    ans = [0]*N
    for i in range(N):
        ans[A[i]-1] = i+1
    for i in range(N):
        print(ans[i],end=' ')

=======
Suggestion 7

def main():
    N = int(input())
    A = list(map(int,input().split()))
    print(" ".join(map(str,sorted(A,key = lambda x: -x))))

=======
Suggestion 8

def main():
    N = int(input())
    A = list(map(int, input().split()))

    #Aの各要素の値を、出席番号に変換する
    #0番目は使わない
    B = [0] * (N+1)
    for i in range(N):
        B[A[i]] = i+1

    #Bの各要素の値を、Aの各要素の値に変換する
    #0番目は使わない
    C = [0] * (N+1)
    for i in range(N):
        C[i+1] = B[i+1]

    #Cの各要素の値を、出席番号に変換する
    #0番目は使わない
    D = [0] * (N+1)
    for i in range(N):
        D[C[i+1]] = i+1

    #出席番号の順に出力する
    for i in range(N):
        print(D[i+1], end=" ")
    print()

=======
Suggestion 9

def solve(N, A):
    # write your code
    return
