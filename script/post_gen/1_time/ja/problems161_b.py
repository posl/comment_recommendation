Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort(reverse=True)
    total = sum(a)
    for i in range(m):
        if a[i] < total / (4 * m):
            print("No")
            return
    print("Yes")

=======
Suggestion 2

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    if sum(A) < 4 * M * A[-1]:
        print("No")
    else:
        print("Yes")

=======
Suggestion 3

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort(reverse=True)
    if A[M-1] >= sum(A) / (4*M):
        print("Yes")
    else:
        print("No")

=======
Suggestion 4

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    sumA = sum(A)
    A.sort(reverse=True)
    if A[M-1] >= sumA/(4*M):
        print("Yes")
    else:
        print("No")

=======
Suggestion 5

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort(reverse=True)
    total = sum(a)
    if a[m-1] >= total / (4*m):
        print("Yes")
    else:
        print("No")

=======
Suggestion 6

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort(reverse=True)
    if a[m-1] < sum(a)/(4*m):
        print("No")
    else:
        print("Yes")

=======
Suggestion 7

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    if sum(A) < M * 4:
        print("No")
        return
    A.sort(reverse=True)
    if A[M-1] < sum(A[0:M]) / (4*M):
        print("No")
        return
    print("Yes")

=======
Suggestion 8

def main():
    N,M = map(int,input().split())
    A = list(map(int,input().split()))
    A.sort(reverse=True)
    sumA = sum(A)
    cnt = 0
    for i in range(M):
        if A[i] < (sumA/(4*M)):
            break
        else:
            cnt += 1
    if cnt == M:
        print("Yes")
    else:
        print("No")

=======
Suggestion 9

def main():
	N, M = map(int, input().split())
	A = list(map(int, input().split()))
	# 人気商品の得票数の合計が総投票数の (1/(4M)) 以上であることを確認する
	# 人気商品の得票数の合計を求める
	# 人気商品の得票数の合計が総投票数の (1/(4M)) 以上であることを確認する
	# 人気商品の得票数の合計を求める
	# 人気商品の得票数の合計が総投票数の (1/(4M)) 以上であることを確認する
	# 人気商品の得票数の合計を求める

	# 人気商品の得票数の合計が総投票数の (1/(4M)) 以上であることを確認する
	# 人気商品の得票数の合計を求める
	# 人気商品の得票数の合計が総投票数の (1/(4M)) 以上であることを確認する
	# 人気商品の得票数の合計を求める
	# 人気商品の得票数の合計が総投票数の (1/(4M)) 以上であることを確認する
	# 人気商品の得票数の合計を求める

	# 人気商品の得票数の合計が総投票数の (1/(4M)) 以上であることを確認する
	# 人気商品の得票数の合計を求める
	# 人気商品の得票数の合計が総投票数の (1/(4M)) 以上であることを確認する
	# 人気商品の得票数の合計を求める
	# 人気
