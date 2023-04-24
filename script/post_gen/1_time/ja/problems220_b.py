Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    K = int(input())
    A, B = input().split()
    A = int(A, K)
    B = int(B, K)
    print(A*B)

=======
Suggestion 2

def main():
    K = int(input())
    A, B = input().split()
    print(int(A, K) * int(B, K))

=======
Suggestion 3

def main():
    K = int(input())
    A, B = map(str, input().split())
    print(int(A, K) * int(B, K))

=======
Suggestion 4

def main():
    k = int(input())
    a, b = input().split()
    print(int(a, k) * int(b, k))

=======
Suggestion 5

def main():
    # 入力
    K = int(input())
    A, B = input().split()
    # 処理
    A10 = int(A, K)
    B10 = int(B, K)
    C10 = A10 * B10
    # 出力
    print(C10)

=======
Suggestion 6

def main():
    k = int(input())
    a,b = map(int, input().split())
    print(a*k+b)
