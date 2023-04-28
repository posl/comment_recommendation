Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    ladders = []
    for _ in range(N):
        A, B = map(int, input().split())
        ladders.append((A, B))
    ladders.sort(key=lambda x: x[1])
    ans = 0
    for A, B in ladders:
        if ans < A:
            ans = B
    print(ans)

=======
Suggestion 2

def main():
    N = int(input())
    A = [0]*N
    B = [0]*N
    for i in range(N):
        A[i], B[i] = map(int, input().split())
    print(max(A) + max(B))

=======
Suggestion 3

def main():
    N = int(input())
    stairs = []
    for i in range(N):
        A, B = map(int, input().split())
        stairs.append([A, B])
    stairs.sort(key=lambda x: x[1])
    #print(stairs)
    max = 0
    for i in range(N):
        if stairs[i][0] > max:
            max = stairs[i][0]
    print(max)

=======
Suggestion 4

def main():
    n = int(input())
    ab = [list(map(int, input().split())) for _ in range(n)]
    ab.sort(key=lambda x:x[1])
    ans = 0
    for i in range(n):
        if ans < ab[i][0]:
            ans = ab[i][1]
    print(ans)

=======
Suggestion 5

def main():
    n = int(input())
    ab = []
    for _ in range(n):
        a,b = map(int, input().split())
        ab.append((a,b))
    ab.sort(key=lambda x:x[1])
    ans = 0
    for i in range(n):
        if i == 0:
            ans = ab[i][1]
        else:
            if ab[i][0] <= ans:
                ans = ab[i][0]
            else:
                ans = ab[i][1]
    print(ans)

=======
Suggestion 6

def main():
    n = int(input())
    ab = [list(map(int, input().split())) for _ in range(n)]
    ab.sort(key=lambda x: x[1])
    cur = 0
    ans = 0
    for a, b in ab:
        if cur < a:
            cur = b
            ans += 1
    print(ans)

=======
Suggestion 7

def main():
    N = int(input())
    AB = [map(int, input().split()) for _ in range(N)]
    A, B = [list(i) for i in zip(*AB)]

    print(min(A) + min(B))

=======
Suggestion 8

def main():
    N = int(input())
    AB = []
    for i in range(N):
        A, B = map(int, input().split())
        AB.append([A, B])
    AB.sort()
    ans = 0
    for i in range(N):
        if ans < AB[i][1]:
            ans = AB[i][1]
    print(ans)
main()

=======
Suggestion 9

def solve():
    n = int(input())
    ab = [list(map(int,input().split())) for _ in range(n)]
    ab.sort(key=lambda x: x[1])
    ans = 0
    for a,b in ab:
        if ans < a:
            ans = b
    print(ans)

=======
Suggestion 10

def solve():
    # 解答アルゴリズム
    # 1. はしごの一番下の階から一番上の階まで、はしごを使って移動する
    # 2. 一番上の階にたどり着いたら、その階の階数を出力する
    # 3. はしごを使って移動する際は、はしごを使った移動をした階の階数を記録する
    # 4. はしごを使って移動する際は、はしごを使った移動をした階の階数が、はしごを使って移動する前の階の階数よりも大きくないことを確認する
    # 5. はしごを使って移動する際は、はしごを使った移動をした階の階数が、はしごを使って移動する前の階の階数よりも大きければ、はしごを使った移動をした階の階数を記録する
    # 6. はしごを使って移動する際は、はしごを使った移動をした階の階数が、はしごを使って移動する前の階の階数よりも小さければ、はしごを使った移動をした階の階数を記録しない
    # 7. はしごを使って移動する際は、はしごを使った移動をした階の階数が、はしごを使って移動する前の階の階数よりも小さければ、はしごを使った移動をした階の階数を記録しない
    # 8. はしごを使って移動する際は、はしごを使った移動をした階の階数
