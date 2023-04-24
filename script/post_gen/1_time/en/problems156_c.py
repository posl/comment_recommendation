Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N = int(input())
    X = list(map(int, input().split()))
    X.sort()
    ans = 0
    for i in range(N):
        ans += (X[i] - X[N // 2]) ** 2
    print(ans)

=======
Suggestion 2

def main():
    n = int(input())
    x = list(map(int, input().split()))
    x.sort()
    ans = 0
    for i in range(n):
        ans += (x[i] - x[n//2])**2
    print(ans)

=======
Suggestion 3

def main():
    N = int(input())
    X = list(map(int,input().split()))
    ans = 0
    for i in range(min(X),max(X)+1):
        temp = 0
        for j in range(N):
            temp += (X[j]-i)**2
        if ans == 0:
            ans = temp
        else:
            ans = min(ans,temp)
    print(ans)

=======
Suggestion 4

def main():
    n = int(input())
    x = [int(x) for x in input().split()]
    x.sort()
    ans = 0
    for i in range(n):
        ans += (x[i] - x[n//2])**2
    print(ans)

=======
Suggestion 5

def main():
    N = int(input())
    X = list(map(int, input().split()))
    ans = 10 ** 9
    for i in range(1, 101):
        s = 0
        for j in X:
            s += (i - j) ** 2
        ans = min(ans, s)
    print(ans)

=======
Suggestion 6

def main():
    N = int(input())
    X = list(map(int,input().split()))
    X.sort()
    tmp = 0
    for i in range(N):
        tmp += abs(i+1-X[i])
    print(tmp)

=======
Suggestion 7

def main():
    # 1行目の入力
    N = int(input())
    # 2行目の入力
    X = [int(i) for i in input().split()]
    # 結果出力
    print(min([sum([(x - p) ** 2 for x in X]) for p in range(1, 101)]))
