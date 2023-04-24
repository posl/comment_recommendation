Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N, K = map(int, input().split())
    ans = 0
    for i in range(1, N+1):
        for j in range(1, K+1):
            ans += i*100 + j
    print(ans)

=======
Suggestion 2

def main():
    N, K = map(int, input().split())
    sum = 0
    for i in range(1, N+1):
        for j in range(1, K+1):
            sum += i*100 + j
    print(sum)

=======
Suggestion 3

def main():
    N, K = map(int, input().split())
    ans = 0
    for i in range(1, N+1):
        for j in range(1, K+1):
            ans += 100*i + j
    print(ans)
    return

=======
Suggestion 4

def main():
    N, K = map(int, input().split())
    sum = 0
    for i in range(1, N+1):
        for j in range(1, K+1):
            sum += int(str(i)+str(j)+str(j))
    print(sum)

=======
Suggestion 5

def main():
    N, K = map(int, input().split())
    
    ans = 0
    for i in range(1, N+1):
        for j in range(1, K+1):
            ans += 100 * i + j
        
    print(ans)

=======
Suggestion 6

def main():
    N,K = map(int,input().split())
    sum = 0
    for i in range(1,N+1):
        for j in range(1,K+1):
            sum = sum + int(i*100+j)
    print(sum)

=======
Suggestion 7

def main():
    #入力
    N, K = map(int, input().split())
    #変数
    sum = 0
    #処理
    for i in range(1, N+1):
        for j in range(1, K+1):
            sum += i*100 + j
    #出力
    print(sum)
