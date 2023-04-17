Synthesizing 10/10 solutions (Duplicates hidden)

=======

def main():
    A = list(map(int, input().split()))
    A.sort()
    print(A[1] - A[0] + A[2] - A[1])

=======

def main():
    # 入力
    A = list(map(int, input().split()))
    # 処理
    A.sort()
    ans = A[2] - A[0]
    # 出力
    print(ans)

=======

def main():
    A = list(map(int, input().split()))
    A.sort()
    print(A[2] - A[0])

=======

def main():
    A = list(map(int,input().split()))
    A.sort()
    ans = 0
    for i in range(1,3):
        ans += abs(A[i] - A[i-1])
    print(ans)

=======

def main():
    # 入力
    A = list(map(int, input().split()))
    # 処理
    A.sort()
    # 出力
    print(A[2] - A[0])

=======

def main():
    a, b, c = map(int, input().split(' '))
    print(min(abs(a - b), abs(b - c), abs(c - a)))

=======

def main():
    A = list(map(int, input().split()))
    print(sum(A) - max(A))
