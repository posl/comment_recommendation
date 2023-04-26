Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N, K = map(int, input().split())
    d = [0] * K
    A = [0] * K
    for i in range(K):
        d[i] = int(input())
        A[i] = list(map(int, input().split()))
    
    #print(N, K)
    #print(d)
    #print(A)
    
    # いたずらを受ける人数
    cnt = 0
    
    for i in range(N):
        # すぬけ君 i がいたずらを受けるかどうかのフラグ
        flag = 0
        
        for j in range(K):
            if (i+1) in A[j]:
                flag = 1
                break
        
        if flag == 0:
            cnt += 1
    
    print(cnt)

=======
Suggestion 2

def main():
    N, K = map(int, input().split())
    d = [0] * K
    A = [0] * K
    for i in range(K):
        d[i] = int(input())
        A[i] = list(map(int, input().split()))
    ans = 0
    for i in range(1, N + 1):
        for j in range(K):
            if i in A[j]:
                break
            if j == K - 1:
                ans += 1
    print(ans)

=======
Suggestion 3

def main():
    N, K = map(int, input().split())
    S = [0] * N
    for i in range(K):
        d = int(input())
        A = list(map(int, input().split()))
        for j in range(d):
            S[A[j] - 1] += 1
    print(S.count(0))

=======
Suggestion 4

def main():
    N, K = map(int, input().split())
    d = [0] * N
    for i in range(K):
        di = int(input())
        for j in map(int, input().split()):
            d[j-1] += 1
    print(d.count(0))

=======
Suggestion 5

def main():
    n, k = map(int, input().split())
    d = [0] * n
    for i in range(k):
        di = int(input())
        for j in map(int, input().split()):
            d[j - 1] += 1
    print(d.count(0))

=======
Suggestion 6

def main():
    N, K = map(int, input().split())
    d = []
    for i in range(K):
        d.append(int(input()))
        a = []
        for j in range(d[i]):
            a.append(int(input()))
        print(a)

=======
Suggestion 7

def main():
    N, K = map(int, input().split())
    sweets = [0] * N
    for _ in range(K):
        for a in map(int, input().split()[1:]):
            sweets[a - 1] += 1
    print(sweets.count(0))

=======
Suggestion 8

def main():
    N, K = map(int, input().split())

    # お菓子を持っている人数をカウントする
    # お菓子を持っていない場合は0
    # お菓子を持っている場合は1
    # すべての人が持っている場合はK
    cnt = [0] * N

    for _ in range(K):
        d = int(input())
        for a in map(int, input().split()):
            cnt[a - 1] += 1

    # 0の人数をカウント
    print(cnt.count(0))

=======
Suggestion 9

def main():
    N, K = map(int, input().split())
    #A = []
    A = [0]*N
    for i in range(K):
        d = int(input())
        A_ = list(map(int,input().split()))
        for j in range(d):
            A[A_[j]-1] += 1
    ans = 0
    for i in range(N):
        if A[i] == 0:
            ans += 1
    print(ans)
