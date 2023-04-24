Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    for i in range(n):
        if a[i] != x:
            print(a[i], end=" ")

=======
Suggestion 2

def main():
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    for i in a:
        if i != x:
            print(i, end=" ")

=======
Suggestion 3

def main():
    N, X = map(int, input().split())
    A = list(map(int, input().split()))
    A = [a for a in A if a != X]
    print(*A)

=======
Suggestion 4

def main():
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    a = [i for i in a if i != x]
    print(*a)

=======
Suggestion 5

def main():
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    ans = [i for i in a if i != x]
    print(*ans)

=======
Suggestion 6

def main():
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    print(*[i for i in a if i != x])

=======
Suggestion 7

def main():
    #入力
    N, X = map(int, input().split())
    A = list(map(int, input().split()))
    #A から X と等しい要素を全て取り除き、残った要素をそのままの順序で並べた数列 A' を出力してください。  
    #A から X と等しい要素を全て取り除き、残った要素をそのままの順序で並べた数列 A' を出力してください。  
    for i in A:
        if i == X:
            A.remove(i)
    print(*A)

=======
Suggestion 8

def main():
    N, X = map(int, input().split())
    A = list(map(int, input().split()))
    A_prime = [a for a in A if a != X]
    print(*A_prime)

=======
Suggestion 9

def main():
    N,X = map(int,input().split())
    A = list(map(int,input().split()))
    for i in range(N):
        if A[i] != X:
            print(A[i],end = " ")

=======
Suggestion 10

def main():
    #N個の数値をintで取得
    N, X = map(int, input().split())
    #N個の数値をlistで取得
    A = list(map(int, input().split()))
    #Xと等しい要素を全て取り除き、残った要素をそのままの順序で並べた数列を出力
    #print(A)
    #print(A.pop(1))
    #print(A)
    #print(A.index(5))
    #print(A.count(5))
    #print(A.re
