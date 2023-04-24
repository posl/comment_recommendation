Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    P = list(map(int, input().split()))
    ans = 1
    min = P[0]
    for i in range(1, N):
        if P[i] <= min:
            ans += 1
            min = P[i]
    print(ans)

=======
Suggestion 2

def main():
    n = int(input())
    p = list(map(int, input().split()))
    cnt = 1
    min_p = p[0]
    for i in range(1, n):
        if p[i] <= min_p:
            cnt += 1
            min_p = p[i]
    print(cnt)

=======
Suggestion 3

def main():
    N = int(input())
    P = list(map(int, input().split()))
    count = 0
    for i in range(N):
        if P[i] == min(P[:i+1]):
            count += 1
    print(count)

=======
Suggestion 4

def main():
    N = int(input())
    P = list(map(int, input().split()))
    ans = 0
    minP = P[0]
    for i in range(N):
        if minP >= P[i]:
            ans += 1
            minP = P[i]
    print(ans)

=======
Suggestion 5

def main():
    N = int(input())
    P = list(map(int, input().split()))
    count = 0
    min = P[0]
    for i in range(1, N):
        if P[i] <= min:
            count += 1
            min = P[i]
    print(count+1)

=======
Suggestion 6

def main():
    N = int(input())
    P = list(map(int, input().split()))
    ans = 0
    min_num = P[0]
    for i in range(1, N):
        if P[i] <= min_num:
            ans += 1
            min_num = P[i]
    print(ans + 1)

=======
Suggestion 7

def main():
    N = int(input())
    P = list(map(int, input().split()))
    ans = 0
    min_num = P[0]
    for i in range(1, N):
        if min_num >= P[i]:
            ans += 1
            min_num = P[i]
    print(ans + 1)

=======
Suggestion 8

def main():
    N = int(input())
    P = list(map(int, input().split()))
    ans = 0
    min_P = P[0]
    for i in range(1, N):
        if P[i] <= min_P:
            ans += 1
        min_P = min(min_P, P[i])
    print(ans + 1)

=======
Suggestion 9

def main():
    N = int(input())
    P = list(map(int, input().split()))

    # 1, ..., N の順列 P_1, ..., P_N が与えられます。
    # 次の条件を満たす整数 i(1 ≦ i ≦ N) の個数を数えてください。
    # 任意の整数 j(1 ≦ j ≦ i) に対して、 P_i ≦ P_j

    # P_i ≦ P_j となる i, j を満たす i, j の組み合わせの個数を数える
    # 1 ≦ i ≦ N, 1 ≦ j ≦ i を満たす i, j の組み合わせの個数を数える

    # i=1,2,4 が条件を満たします。
    # i=3 は条件を満たしません。

    # 1 ≦ i ≦ N, 1 ≦ j ≦ i を満たす i, j の組み合わせの個数を数える
    # 1 ≦ i ≦ N, 1 ≦ j ≦ i を満たす i, j の組み合わせの個数を数える
    # 1 ≦ i ≦ N, 1 ≦ j ≦ i を満たす i, j の組み合わせの個数を数える
    # 1 ≦ i ≦ N, 1 ≦ j ≦ i を満たす i, j の組み合わせの個数を数える
    # 1 ≦ i ≦ N, 1 ≦ j ≦ i を満たす i, j の組み合わせの個数を数える
    # 1 ≦ i ≦ N, 1 ≦ j ≦ i を満たす i, j の組み合わせの個数を数える
    # 1 ≦ i ≦ N, 1 ≦

=======
Suggestion 10

def main():
    N = int(input())
    P = list(map(int, input().split()))
    #print(N)
    #print(P)
    cnt = 0
    minP = 10**9
    for i in range(N):
        if minP >= P[i]:
            cnt += 1
            minP = P[i]
    print(cnt)
