Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N,K,Q = map(int,input().split())
    #print(N,K,Q)
    A = []
    for i in range(Q):
        A.appen

=======
Suggestion 2

def main():
    N,K,Q = map(int,input().split())
    A = [int(input()) for i in range(Q)]
    score = [K for i in range(N)]
    for i in range(Q):
        score[A[i]-1] -= 1
    for i in range(N):
        if score[i] <= 0:
            print('No')
        else:
            print('Yes')

=======
Suggestion 3

def main():
    N, K, Q = map(int, input().split())
    A = [int(input()) for _ in range(Q)]
    #print(N, K, Q, A)
    #print(N, K, Q, A)
    #print("A: ", A)
    score = [K] * N
    #print("score: ", score)
    for i in range(Q):
        score[A[i] - 1] += 1
        #print("score: ", score)
    for i in range(N):
        if score[i] - Q <= 0:
            print("No")
        else:
            print("Yes")

=======
Suggestion 4

def solve():
    N, K, Q = map(int, input().split())
    A = [int(input()) for _ in range(Q)]
    ans = [True] * N
    for a in A:
        ans[a-1] = not ans[a-1]
    for i in range(N):
        if ans[i]:
            print("Yes")
        else:
            print("No")

=======
Suggestion 5

def get_input():
    n,k,q = map(int,input().split())
    alist = []
    for i in range(q):
        alist.append(int(input()))
    return n,k,q,alist

=======
Suggestion 6

def problems141_c():
    pass

=======
Suggestion 7

def main():
    n,k,q = map(int,input().split())
    A = [0]*n
    for i in range(q):
        a = int(input())
        A[a-1] += 1
    for i in range(n):
        if k+ A[i] - q > 0:
            print("Yes")
        else:
            print("No")
main()

=======
Suggestion 8

def main():
	n,k,q = map(int,input().split())
	scores = [k for i in range(n)]
	for i in range(q):
		a = int(input())
		scores[a-1] -= 1
	for i in range(n):
		if scores[i] <= 0:
			print('No')
		else:
			print('Yes')

=======
Suggestion 9

def main():
    #读入数据
    N, K, Q = map(int, input().split())
    A = [int(input()) for i in range(Q)]

    #初始化玩家得分
    score = [K-Q for i in range(N)]

    #计算玩家得分
    for i in range(Q):
        score[A[i]-1] += 1

    #输出
    for i in range(N):
        if score[i] > 0:
            print("Yes")
        else:
            print("No")

=======
Suggestion 10

def main():
    n,k,q = map(int,input().split())
    a = [int(input()) for i in range(q)]
    p = [0 for i in range(n)]
    for i in range(q):
        p[a[i]-1] += 1
    for i in range(n):
        if k + p[i] - q > 0:
            print("Yes")
        else:
            print("No")
