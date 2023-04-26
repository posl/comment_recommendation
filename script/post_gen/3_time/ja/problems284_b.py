Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    T = int(input())
    for i in range(T):
        N = int(input())
        A = list(map(int, input().split()))
        count = 0
        for j in range(N):
            if A[j] % 2 != 0:
                count += 1
        print(count)

=======
Suggestion 2

def main():
    T = int(input())
    for i in range(T):
        N = int(input())
        A = list(map(int, input().split()))
        count = 0
        for j in range(N):
            if A[j] % 2 == 1:
                count += 1
        print(count)

=======
Suggestion 3

def main():
    T = int(input())
    for i in range(T):
        N = int(input())
        A = list(map(int, input().split()))
        cnt = 0
        for j in range(N):
            if A[j] % 2 == 1:
                cnt += 1
        print(cnt)

=======
Suggestion 4

def main():
    T = int(input())
    for i in range(T):
        N = int(input())
        A = list(map(int, input().split()))
        cnt = 0
        for j in range(N):
            if A[j] % 2 == 1:
                cnt += 1
        print(cnt)
main()

=======
Suggestion 5

def main():
    T = int(input())
    for t in range(T):
        N = int(input())
        A = list(map(int, input().split()))
        ans = 0
        for a in A:
            if a % 2 == 1:
                ans += 1
        print(ans)

=======
Suggestion 6

def main():
    T = int(input())
    for i in range(T):
        N = int(input())
        A = list(map(int, input().split()))
        print(len([a for a in A if a % 2 != 0]))

=======
Suggestion 7

def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        A = list(map(int,input().split()))
        print(len([a for a in A if a%2 == 1]))

=======
Suggestion 8

def main():
    # 1行目の入力
    T = int(input())
    # T回のループ
    for i in range(T):
        # 2行目の入力
        N = int(input())
        # 3行目の入力
        A = list(map(int, input().split()))
        # 奇数の数をカウントする変数
        count = 0
        # N回のループ
        for j in range(N):
            # 奇数ならカウントする
            if A[j] % 2 == 1:
                count += 1
        # 結果の出力
        print(count)

=======
Suggestion 9

def main():
    # 1行目の入力
    T = int(input())
    # T個のテストケースについて処理を行う
    for i in range(T):
        # 2行目の入力
        N = int(input())
        # 3行目の入力
        A = list(map(int, input().split()))
        # Aの中に奇数が何個あるかをカウントする
        cnt = 0
        for j in range(N):
            if A[j] % 2 == 1:
                cnt += 1
        # 結果を出力する
        print(cnt)
