Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N, K = map(int, input().split())
    h = list(map(int, input().split()))
    count = 0
    for i in range(N):
        if h[i] >= K:
            count += 1
    print(count)

=======
Suggestion 2

def main():
    N, K = map(int, input().split())
    h = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        if h[i] >= K:
            ans += 1
    print(ans)

=======
Suggestion 3

def main():
    N, K = map(int, input().split())
    h = list(map(int, input().split()))
    cnt = 0
    for i in range(N):
        if h[i] >= K:
            cnt += 1
    print(cnt)

=======
Suggestion 4

def main():
    N, K = list(map(int, input().split()))
    h = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        if h[i] >= K:
            ans += 1
    print(ans)

=======
Suggestion 5

def main():
    #入力
    N, K = map(int, input().split())
    h = list(map(int, input().split()))
    
    #処理
    count = 0
    for i in range(N):
        if h[i] >= K:
            count += 1
            
    #出力
    print(count)
