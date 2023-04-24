Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, L = map(int, input().split())
    apple = [L + i - 1 for i in range(1, N + 1)]
    print(sum(apple) - min(apple, key=abs))

=======
Suggestion 2

def main():
    N, L = map(int, input().split())
    ans = 0
    for i in range(1, N + 1):
        ans += L + i - 1
    if L <= 0 and 0 <= L + N - 1:
        print(ans)
    elif L > 0:
        print(ans - L)
    else:
        print(ans - (L + N - 1))

=======
Suggestion 3

def main():
    n, l = map(int, input().split())
    ans = 0
    for i in range(1, n+1):
        ans += l+i-1
    if l > 0:
        ans -= l
    elif l+n-1 < 0:
        ans -= l+n-1
    print(ans)

=======
Suggestion 4

def main():
    N, L = map(int, input().split())
    ans = 0
    for i in range(1, N):
        ans += L + i - 1
    if L <= 0 and L + N - 1 >= 0:
        print(ans)
    elif L > 0:
        print(ans - L)
    else:
        print(ans - (L + N - 1))

=======
Suggestion 5

def main():
    N, L = map(int, input().split())
    ans = 0
    if L >= 0:
        ans = sum(i for i in range(L, L+N))
    elif L+N-1 <= 0:
        ans = sum(i for i in range(L, L+N))
    else:
        ans = sum(i for i in range(L, L+N)) - min(i for i in range(L, L+N))
    print(ans)

=======
Suggestion 6

def main():
    N, L = map(int, input().split())
    #1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30
    #1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30
    #1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30
    #1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30
    #1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30
    #1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30
    #1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30
    #1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25

=======
Suggestion 7

def main():
    N, L = map(int, input().split())
    print(sum(i for i in range(1, N) if L + i > 0) + sum(i for i in range(1, N) if L + i - 1 < 0))

=======
Suggestion 8

def main():
    N, L = map(int, input().split())
    # 全て食べる場合のアップルパイの味
    all = sum([L+i-1 for i in range(1, N+1)])
    # 一番味の悪いリンゴを食べない場合のアップルパイの味
    not_eat = sum([L+i-1 for i in range(1, N+1) if i != N])
    # 一番味の悪いリンゴを食べる場合のアップルパイの味
    eat = sum([L+i-1 for i in range(1, N+1) if i != 1])

    # 一番味の悪いリンゴを食べない場合と食べる場合のうちどちらがアップルパイの味が近いかで場合分け
    if abs(all - not_eat) < abs(all - eat):
        print(not_eat)
    else:
        print(eat)

=======
Suggestion 9

def main():
    N,L = map(int,input().split())
    a = [i for i in range(L,L+N)]
    print(sum(a)-min(a,key=abs))

=======
Suggestion 10

def main():
    N, L = map(int, input().split())
    # 1個食べると、残りのN-1個のリンゴの味の総和は
    # L+L+1+...+L+N-2
    # これを最も小さくするには、L+L+1+...+L+N-2を最大化する必要がある
    # つまり、L+L+1+...+L+N-2を最大化するには、L+1+2+...+N-1が最大化される必要がある
    # つまり、L+1+2+...+N-1=L+N-2
    # つまり、N-2=L+N-2
    # つまり、N=2L-1
    # つまり、L=N/2+0.5
    # つまり、L=N//2+0.5
    # つまり、L=N//2+1/2
    # つまり、L=N//2+1/2
    # つまり、L=N//2+1//2
    # ��
