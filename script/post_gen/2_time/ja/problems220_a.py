Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    A, B, C = map(int, input().split())
    ans = -1
    for i in range(A, B + 1):
        if i % C == 0:
            ans = i
            break
    print(ans)

=======
Suggestion 2

def main():
    a, b, c = map(int, input().split())
    for i in range(a, b+1):
        if i % c == 0:
            print(i)
            return
    print(-1)

=======
Suggestion 3

def main():
    A, B, C = map(int, input().split())
    for i in range(A, B+1):
        if i % C == 0:
            print(i)
            return
    print(-1)

=======
Suggestion 4

def main():
    # A, B, C = map(int, input().split())
    A, B, C = 123, 456, 100
    # A, B, C = 630, 940, 314
    # A, B, C = 1, 1000, 1
    # A, B, C = 1, 1000, 1000

    if A > B:
        print(-1)
        return

    for i in range(A, B + 1):
        if i % C == 0:
            print(i)
            return

    print(-1)

=======
Suggestion 5

def main():
    #入力
    A,B,C = map(int,input().split())
    
    #処理
    ans = -1
    for i in range(A,B+1):
        if i%C == 0:
            ans = i
            break
    #出力
    print(ans)

=======
Suggestion 6

def main():
    #入力
    A, B, C = map(int, input().split())
    #Cの倍数をリストに格納
    multiples = [i for i in range(A, B + 1) if i % C == 0]
    #リストが空なら-1を出力
    if not multiples:
        print(-1)
    #リストが空でないなら最小値を出力
    else:
        print(min(multiples))
