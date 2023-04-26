Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n, k = map(int, input().split())
    h = list(map(int, input().split()))
    cnt = 0
    for i in range(n):
        if h[i] >= k:
            cnt += 1
    print(cnt)

=======
Suggestion 2

def main():
    n, k = map(int, input().split())
    h = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        if h[i] >= k:
            ans += 1
    print(ans)

=======
Suggestion 3

def main():
    N, K = map(int, input().split())
    h = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        if h[i] >= K:
            ans += 1
    print(ans)

=======
Suggestion 4

def main():
    n,k = map(int,input().split())
    h = list(map(int,input().split()))
    count = 0
    for i in range(n):
        if h[i] >= k:
            count += 1
    print(count)

=======
Suggestion 5

def main():
    n,k = map(int,input().split())
    h = list(map(int,input().split()))
    ans = 0
    for i in h:
        if i >= k:
            ans += 1
    print(ans)

=======
Suggestion 6

def solve():
    n, k = map(int, input().split())
    h = list(map(int, input().split()))
    cnt = 0
    for i in range(n):
        if h[i] >= k:
            cnt += 1
    print(cnt)

=======
Suggestion 7

def main():
    n,k = [int(i) for i in input().split()]
    h = [int(i) for i in input().split()]
    count = 0
    for i in h:
        if i >= k:
            count += 1
    print(count)

=======
Suggestion 8

def main():
    # 標準入力から値を取得する
    n, k = map(int, input().split())
    h = list(map(int, input().split()))

    # 一番人気のジェットコースターに乗ることができる人の数を出力
    count = 0
    for i in range(n):
        if h[i] >= k:
            count += 1
    print(count)

=======
Suggestion 9

def main():
    input_line1 = input()
    input_line2 = input()
    input_line1_split = input_line1.split()
    input_line2_split = input_line2.split()
    input_line1_split_int = [int(x) for x in input_line1_split]
    input_line2_split_int = [int(x) for x in input_line2_split]
    
    n = input_line1_split_int[0]
    k = input_line1_split_int[1]
    
    count = 0
    for i in range(n):
        if input_line2_split_int[i] >= k:
            count += 1
    
    print(count)
