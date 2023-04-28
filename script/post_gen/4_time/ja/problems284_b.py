Synthesizing 10/10 solutions

=======
Suggestion 1

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
Suggestion 2

def main():
    t = int(input())
    for i in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        ans = 0
        for j in range(n):
            if a[j] % 2 == 1:
                ans += 1
        print(ans)

=======
Suggestion 3

def main():
    n = int(input())
    a = list(map(int, input().split()))
    odd = 0
    for i in a:
        if i % 2 == 1:
            odd += 1
    print(odd)

=======
Suggestion 4

def main():
    T = int(input())
    for i in range(T):
        N = int(input())
        A = list(map(int, input().split()))
        odd = 0
        for j in A:
            if j % 2 == 1:
                odd += 1
        print(odd)

=======
Suggestion 5

def count_odd(n, a):
    count = 0
    for i in range(n):
        if a[i] % 2 == 1:
            count += 1
    return count

t = int(input())
for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    print(count_odd(n, a))

=======
Suggestion 6

def count_odd():
    n = int(input())
    a = list(map(int, input().split()))
    cnt = 0
    for i in range(n):
        if a[i] % 2 == 1:
            cnt += 1
    print(cnt)

t = int(input())
for i in range(t):
    count_odd()

=======
Suggestion 7

def main():
    T = int(input())
    for i in range(T):
        N = int(input())
        A = list(map(int,input().split()))
        print(sum([a%2 for a in A]))

=======
Suggestion 8

def solve():
    # T
    T = int(input())
    for _ in range(T):
        # N
        N = int(input())
        # A_1 A_2 ... A_N
        A = list(map(int, input().split()))
        # 出力
        print(len([a for a in A if a % 2 == 1]))

=======
Suggestion 9

def main():
    # input
    T = int(input())
    ans = []
    for i in range(T):
        N = int(input())
        A = list(map(int, input().split()))
        # compute
        odd = 0
        for a in A:
            if a % 2 == 1:
                odd += 1
        ans.append(odd)
    # output
    for a in ans:
        print(a)

=======
Suggestion 10

def main():
    # Tの入力
    T = int(input())
    # 各テストケースの処理
    for i in range(T):
        # Nの入力
        N = int(input())
        # Aの入力
        A = list(map(int, input().split()))
        # 奇数の数を初期化
        odd = 0
        # Aの要素の数だけ繰り返す
        for j in range(N):
            # Aの要素が奇数なら
            if (A[j] % 2 == 1):
                # 奇数の数をカウントアップ
                odd += 1
        # 答えを出力
        print(odd)
