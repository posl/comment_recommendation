Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    total = sum(A)
    A.sort(reverse=True)
    if A[M-1] >= total / (4*M):
        print("Yes")
    else:
        print("No")

=======
Suggestion 2

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    sum_A = sum(A)
    A.sort(reverse=True)
    if A[M-1] >= sum_A/(4*M):
        print("Yes")
    else:
        print("No")

=======
Suggestion 3

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort(reverse=True)
    total = sum(A)
    if A[M-1] * 4 * M >= total:
        print("Yes")
    else:
        print("No")

=======
Suggestion 4

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort(reverse=True)
    sumA = sum(A)
    if A[M-1] >= sumA/(4*M):
        print("Yes")
    else:
        print("No")

=======
Suggestion 5

def main():
    # input
    N, M = map(int, input().split())
    As = list(map(int, input().split()))

    # compute
    total = sum(As)
    As.sort(reverse=True)
    if As[M-1] >= total / (4*M):
        ans = 'Yes'
    else:
        ans = 'No'

    # output
    print(ans)

=======
Suggestion 6

def main():
    N,M = map(int,input().split())
    A = list(map(int,input().split()))
    A.sort(reverse=True)
    sum_A = sum(A)
    if A[M-1] >= sum_A/(4*M):
        print('Yes')
    else:
        print('No')

=======
Suggestion 7

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    total = sum(A)
    limit = total // (4 * M)
    A.sort(reverse=True)
    print("Yes" if A[M - 1] >= limit else "No")

=======
Suggestion 8

def main():
    #入力
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    #総投票数
    total = sum(A)
    #人気商品の得票数
    A.sort(reverse=True)
    popular = A[:M]
    #人気商品の得票数が総投票数の (1/(4M)) 未満であるか
    if min(popular) < total//(4*M):
        print("No")
    else:
        print("Yes")

=======
Suggestion 9

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))

    #総投票数
    total = sum(A)

    #総得票数の (1/(4M)) 未満であるような商品は選べない
    #総得票数の (1/(4M)) 以上であるような商品は選べる
    #総得票数の (1/(4M)) 以上であるような商品のうち、最も得票数が少ないものを選ぶ

    #総得票数の (1/(4M)) 以上であるような商品のうち、最も得票数が少ないものを選ぶ
    #総得票数の (1/(4M)) 以上であるような商品のうち、最も得票数が少ないものの得票数
    min_vote = total / (4 * M)

    #総得票数の (1/(4M)) 以上であるような商品のうち、最も得票数が少ないものを選ぶ
    #総得票数の (1/(4M)) 以上であるような商品のうち、最も得票数が少ないものの個数
    count = 0

    #総得票数の (1/(4M)) 以上であるような商品のうち、最も得票数が少ないものを選ぶ
    #総得票数の (1/(4M)) 以上であるような商品のうち、最も得票数が少ないものを選ぶ
    for i in range(N):
        if A[i] >= min_vote:
            count += 1

    #総得票数の (1/(4M)) 以上であるような商品のうち、最も得票数が少ないものを選

=======
Suggestion 10

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    A.reverse()
    sum_A = sum(A)

    if sum_A / (4 * M) <= A[M - 1]:
        print("Yes")
    else:
        print("No")
