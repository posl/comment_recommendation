Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N = int(input())
    d = list(map(int, input().split()))
    d.sort()
    print(d[N//2] - d[N//2 - 1])

main()

=======
Suggestion 2

def main():
    N = int(input())
    d = list(map(int, input().split()))
    d.sort()
    print(d[N//2]-d[N//2-1])

=======
Suggestion 3

def main():
    n = int(input())
    d = list(map(int, input().split()))
    d.sort()
    print(d[n//2] - d[n//2 - 1])

=======
Suggestion 4

def main():
    N = int(input())
    d = list(map(int, input().split()))
    d.sort()
    K = d[N//2]
    print(K - d[N//2-1])

=======
Suggestion 5

def main():
    #入力
    N = int(input())
    d = [int(x) for x in input().split()]

    #ソート
    d.sort()

    #切り出し
    d = d[N//2:]

    #出力
    print(d[0] - d[-1] + 1)
