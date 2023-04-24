Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, X = map(int, input().split())
    L = list(map(int, input().split()))
    D = [0] * (N+1)
    for i in range(1, N+1):
        D[i] = D[i-1] + L[i-1]
    for i in range(N+1):
        if D[i] > X:
            print(i)
            exit()

=======
Suggestion 2

def main():
    N, X = map(int, input().split())
    L = list(map(int, input().split()))
    ans = 1
    d = 0
    for i in range(N):
        d += L[i]
        if d > X:
            break
        ans += 1
    print(ans)

=======
Suggestion 3

def main():
    N, X = map(int, input().split())
    L = list(map(int, input().split()))
    D = [0] * (N+1)
    for i in range(1, N+1):
        D[i] = D[i-1] + L[i-1]
    ans = 0
    for i in range(N+1):
        if D[i] <= X:
            ans += 1
    print(ans)

=======
Suggestion 4

def main():
    N, X = map(int, input().split())
    L = list(map(int, input().split()))
    D = [0]
    for i in range(N):
        D.append(D[i] + L[i])
    ans = 0
    for i in range(N+1):
        if D[i] <= X:
            ans += 1
    print(ans)

main()

=======
Suggestion 5

def main():
    N, X = map(int, input().split())
    L = list(map(int, input().split()))
    D = [0]
    for i in range(1, N + 1):
        D.append(D[i - 1] + L[i - 1])
    print(len([d for d in D if d <= X]))

=======
Suggestion 6

def main():
    # input
    N, X = map(int, input().split())
    Ls = list(map(int, input().split()))

    # compute
    Ds = [0]
    for i in range(N):
        Ds.append(Ds[-1]+Ls[i])

    # output
    print(sum([1 for D in Ds if D<=X]))

=======
Suggestion 7

def main():
    N, X = map(int, input().split())
    L = list(map(int, input().split()))
    d = 0
    ans = 0
    for i in range(N):
        d += L[i]
        if d <= X:
            ans += 1
        else:
            break
    print(ans + 1)

=======
Suggestion 8

def main():
    n,x=map(int,input().split())
    l=list(map(int,input().split()))
    d=[0]
    for i in range(n):
        d.append(d[i]+l[i])
    ans=0
    for i in range(n+1):
        if d[i]<=x:
            ans+=1
        else:
            break
    print(ans)

=======
Suggestion 9

def main():
    N, X = map(int, input().split())
    L = list(map(int, input().split()))
    #print(N, X)
    #print(L)
    D = [0]
    for i in range(N):
        D.append(D[i]+L[i])
    #print(D)
    cnt = 0
    for i in range(N+1):
        if D[i] <= X:
            cnt += 1
    print(cnt)

=======
Suggestion 10

def main():
    #入力
    N, X = map(int, input().split())
    L = list(map(int, input().split()))
    #跳ねる回数
    count = 0
    #跳ねる位置
    pos = 0
    #跳ねる回数をカウント
    for i in range(N):
        pos += L[i]
        if pos > X:
            break
        count += 1
    #跳ねる回数を出力
    print(count + 1)
