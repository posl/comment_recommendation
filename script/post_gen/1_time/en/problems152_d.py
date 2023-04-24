Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    ans = 0
    for i in range(1, N+1):
        for j in range(1, N+1):
            if str(i)[-1] == str(j)[0]:
                ans += 1
    print(ans)

=======
Suggestion 2

def main():
    N = int(input())
    cnt = 0
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if str(i)[-1] == str(j)[0] and str(i)[0] == str(j)[-1]:
                cnt += 1
    print(cnt)

=======
Suggestion 3

def solve():
    N = int(input())
    ans = 0
    for i in range(1, N+1):
        for j in range(1, N+1):
            if str(i)[-1] == str(j)[0] and str(i)[0] == str(j)[-1]:
                ans += 1
    print(ans)

solve()

=======
Suggestion 4

def main():
    N = int(input())
    D = [0] * 100
    for i in range(1, N + 1):
        s = str(i)
        D[int(s[0]) * 10 + int(s[-1])] += 1
    ans = 0
    for i in range(10):
        for j in range(10):
            ans += D[i * 10 + j] * D[j * 10 + i]
    print(ans)

main()

=======
Suggestion 5

def main():
    N = int(input())
    ans = 0
    for i in range(10):
        for j in range(10):
            ans += (N//10 + (1 if i <= N % 10 else 0)) * (N//10 + (1 if j <= N % 10 else 0))
    print(ans)

=======
Suggestion 6

def main():
    N = int(input())
    print(N * (N + 1) * (2 * N + 1) // 6)

=======
Suggestion 7

def main():
    N = int(input())
    ans = 0

    for i in range(1, N+1):
        ans += (N // i) ** 2

    print(ans)

=======
Suggestion 8

def main():
    N = int(input())
    ans = 0
    for i in range(N):
        ans += (N-i)//10 + 1
    print(ans)

=======
Suggestion 9

def main():
    N = int(input())
    # N = 100
    # N = 200000
    # N = 2020
    # N = 1
    # N = 25

    # 1桁目と10桁目を考える
    # 1桁目は0~9までの10通り
    # 10桁目は0~9までの10通り
    # 1桁目と10桁目の組み合わせは100通り
    # 1桁目と10桁目の組み合わせが一致するのは、
    # 1桁目と10桁目が同じ数字の場合のみ
    # 1桁目と10桁目が同じ数字の場合は、
    # 1桁目と10桁目が同じ数字の数が同じ
    # 1桁目と10桁目が同じ数字の数は、
    # 1桁目が0~9までの数字のうち、N以下の数字の数
    # 10桁目が0~9までの数字のうち、N以下の数字の数
    # 1桁目と10桁目の組み合わせが一致するのは、
    # 1桁目が0~9までの数字のうち、N以下の数字の数
    # 10桁目が0~9までの数字のうち、N以下の数字の数
    # 1桁目と10桁目の組み合わせが一致するのは、
    # 1桁目が0~9までの数字のうち、N以下の数字の数
    # 10桁目が0~9までの数字のうち、N以下の数字の数
    # 1桁目と10桁目の組み合わせが一致するのは、
    # 1桁目が0~9までの数字のうち、N以下の数字

=======
Suggestion 10

def main():
    n = int(input())
    # 1桁の数字の個数をカウントする
    # 00, 01, ..., 99
    c1 = [0] * 10
    # 2桁の数字の個数をカウントする
    # 000, 001, ..., 999
    c2 = [0] * 10
    # 3桁の数字の個数をカウントする
    # 0000, 0001, ..., 9999
    c3 = [0] * 10
    for i in range(1, n + 1):
        if i < 10:
            c1[i] += 1
        elif i < 100:
            c2[i // 10] += 1
        else:
            c3[i // 100] += 1
    ans = 0
    for i in range(1, n + 1):
        if i < 10:
            ans += c1[i]
        elif i < 100:
            ans += c2[i % 10]
        else:
            ans += c3[i % 10]
    print(ans)
