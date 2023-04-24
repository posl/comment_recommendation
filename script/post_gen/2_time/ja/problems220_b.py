Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    K = int(input())
    A, B = map(str, input().split())
    print(int(A, K) * int(B, K))

main()

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
    a, b = map(str, input().split())
    a = int(a, k)
    b = int(b, k)
    print(a * b)

main()

=======
Suggestion 5

def main():
    k = int(input())
    a, b = map(int, input().split())
    a10 = int(str(a), k)
    b10 = int(str(b), k)
    print(a10 * b10)

=======
Suggestion 6

def main():
    K = int(input())
    A, B = map(int, input().split())
    A = int(str(A), K)
    B = int(str(B), K)
    print(A*B)

=======
Suggestion 7

def main():
    # 入力
    K = int(input())
    A, B = map(str, input().split())
    # 処理
    A10 = int(A, K)
    B10 = int(B, K)
    # 出力
    print(A10 * B10)

=======
Suggestion 8

def main():
    K = int(input())
    A,B = map(str,input().split())
    ans = int(A,K)*int(B,K)
    print(ans)

=======
Suggestion 9

def main():
    # 入力
    K = int(input())
    A,B = map(int,input().split())
    # 10進数に変換
    A10 = int(str(A),K)
    B10 = int(str(B),K)
    # 出力
    print(A10*B10)
