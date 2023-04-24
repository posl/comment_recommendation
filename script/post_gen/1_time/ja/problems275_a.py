Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N = int(input())
    H = list(map(int, input().split()))
    print(H.index(max(H)) + 1)

=======
Suggestion 2

def main():
    N = int(input())
    H = list(map(int, input().split()))
    maxH = max(H)
    for i in range(N):
        if H[i] == maxH:
            print(i+1)
            exit()

=======
Suggestion 3

def main():
    n = int(input())
    h = list(map(int,input().split()))
    print(h.index(max(h))+1)

=======
Suggestion 4

def main():
    N = int(input())
    H = list(map(int,input().split()))
    H_max = max(H)
    print(H.index(H_max)+1)

=======
Suggestion 5

def main():
    #入力
    N = int(input())
    H = list(map(int, input().split()))
    #処理
    max_num = max(H)
    max_index = H.index(max_num) + 1
    #出力
    print(max_index)

=======
Suggestion 6

def main():
    #入力
    N = int(input())
    H = list(map(int,input().split()))
    #最大値を求める
    max_h = max(H)
    #最大値の添字を求める
    max_h_index = H.index(max_h)
    #出力
    print(max_h_index+1)
