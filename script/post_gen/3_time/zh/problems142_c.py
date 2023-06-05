Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = input()
    a = map(int, raw_input().split())
    b = [0] * n
    for i in range(n):
        b[a[i] - 1] = i + 1
    print " ".join(map(str, b))

=======
Suggestion 2

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = [0] * n
    for i in range(n):
        b[a[i] - 1] = i + 1
    print(' '.join(str(x) for x in b))

=======
Suggestion 3

def solve(n, a):
    b = [0] * n
    for i in range(n):
        b[a[i]-1] = i + 1
    return b

=======
Suggestion 4

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = [0] * N
    for i in range(N):
        B[A[i]-1] = i + 1
    print(" ".join(map(str, B)))

=======
Suggestion 5

def main():
    n = int(input())
    a = [int(i) for i in input().split()]
    b = [0] * n
    for i in range(n):
        b[a[i]-1] = i+1
    print(' '.join(str(i) for i in b))

=======
Suggestion 6

def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = [0] * n
    for i in range(n):
        ans[a[i] - 1] = i + 1
    print(" ".join(map(str, ans)))

=======
Suggestion 7

def main():
    N = int(input())
    A = list(map(int, input().split()))

    B = [0] * N
    for i in range(N):
        B[A[i]-1] = i+1

    print(*B)

=======
Suggestion 8

def main():
    n = int(input())
    a = [int(x) for x in input().split()]
    b = [0] * n
    for i in range(n):
        b[a[i]-1] = str(i+1)
    print(" ".join(b))

=======
Suggestion 9

def main():
    N = int(input())
    A = list(map(int,input().split()))
    B = [0] * N
    for i in range(N):
        B[A[i]-1] = i+1
    print(' '.join(map(str,B)))

=======
Suggestion 10

def main():
    n = int(input())
    a = list(map(int, input().split()))

    # 逆向きに処理する
    # 1からNまでの数字がそれぞれ何回出現するかを記録する
    cnt = [0] * (n + 1)
    for i in range(n):
        cnt[a[i]] += 1

    # 1からNまでの数字が何番目に出現するかを記録する
    pos = [0] * (n + 1)
    for i in range(1, n + 1):
        pos[i] = i

    # 出現回数が多い順に並べ替える
    for i in range(n):
        for j in range(1, n - i):
            if cnt[j] < cnt[j + 1]:
                cnt[j], cnt[j + 1] = cnt[j + 1], cnt[j]
                pos[j], pos[j + 1] = pos[j + 1], pos[j]

    # 出現回数が多い順に出力する
    for i in range(1, n + 1):
        print(pos[i], end=' ')
    print()
