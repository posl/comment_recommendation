Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N = int(input())
    H = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        if ans < H[i]:
            ans = H[i]
    print(ans)

=======
Suggestion 2

def main():
    n = int(input())
    h = list(map(int,input().split()))
    ans = 0
    for i in range(n-1):
        if h[i] >= h[i+1]:
            h[i+1] = h[i]
        ans = max(ans,h[i+1])
    print(ans)

=======
Suggestion 3

def main():
    N = int(input())
    H = list(map(int, input().split()))

    max_H = 0

    for i in range(N):
        if H[i] >= max_H:
            max_H = H[i]

    print(max_H)

=======
Suggestion 4

def main():
    N = int(input())
    H = list(map(int, input().split()))
    print(max(H))

=======
Suggestion 5

def main():
    n = int(input())
    h = list(map(int, input().split()))
    print(max(h))

=======
Suggestion 6

def main():
    N = int(input())
    H = list(map(int, input().split()))
    #print(N)
    #print(H)
    max = 0
    for i in range(N):
        if max <= H[i]:
            max = H[i]
    print(max)

=======
Suggestion 7

def main():
    N = int(input())
    H = list(map(int,input().split()))
    #print(N)
    #print(H)
    maxH = H[0]
    for i in range(1,N):
        if H[i] >= maxH:
            maxH = H[i]
    print(maxH)

=======
Suggestion 8

def main():
    N = int(input())
    H = list(map(int,input().split()))
    #print(N)
    #print(H)
    H_max = H[0]
    for i in range(1,N):
        if H[i-1] <= H[i]:
            H_max = H[i]
    print(H_max)

=======
Suggestion 9

def main():
    # 入力
    N = int(input())
    H = list(map(int, input().split()))
    # ここに処理を書く
    max_h = H[0]
    for i in range(N):
        if H[i] >= max_h:
            max_h = H[i]
    # 出力
    print(max_h)
