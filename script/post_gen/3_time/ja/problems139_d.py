Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    if n % 2 == 0:
        print(n // 2 - 1)
    else:
        print(n // 2)

=======
Suggestion 2

def main():
    N = int(input())
    if N == 1:
        print(0)
    else:
        print(N * (N - 1) // 2)

=======
Suggestion 3

def main():
    N = int(input())
    ans = 0
    for i in range(1, N):
        ans += (N // i) * (i - (N % i))
    print(ans)

=======
Suggestion 4

def main():
    N = int(input())
    if N == 1:
        print(0)
        return
    if N % 2 == 0:
        print(N - 1)
    else:
        print(N + 1)

=======
Suggestion 5

def main():
    N = int(input())
    if N == 1:
        print(0)
        return
    if N % 2 == 0:
        print(N // 2 - 1)
        return
    else:
        print(N // 2)

=======
Suggestion 6

def main():
    N = int(input())
    if N == 1:
        print(0)
        return
    print(N * (N - 1) // 2)

=======
Suggestion 7

def main():
    # 入力
    N = int(input())

    # 出力
    if N % 2 == 0:
        print(N * (N // 2) - N // 2)
    else:
        print(N * (N // 2))

=======
Suggestion 8

def main():
    N = int(input())
    M = [0 for i in range(N)]
    for i in range(1, N):
        M[i] = N // i * (N // i - 1) // 2 * i
        M[i] += (N % i + 1) * (N // i)
    print(sum(M))

=======
Suggestion 9

def main():
    N = int(input())
    M = [0] * N
    for i in range(1, N + 1):
        M[i - 1] = i % N
    print(sum(M))

=======
Suggestion 10

def main():
    N = int(input())
    if N == 1:
        print(0)
        return
    elif N == 2:
        print(1)
        return
    #Nが3以上の時
    #N-1を最大値にする場合は、N-1をNで割った余りは1になる
    #N-2を最大値にする場合は、N-2をNで割った余りは2になる
    #N-3を最大値にする場合は、N-3をNで割った余りは3になる
    #N-4を最大値にする場合は、N-4をNで割った余りは4になる
    #N-5を最大値にする場合は、N-5をNで割った余りは0になる
    #N-6を最大値にする場合は、N-6をNで割った余りは1になる
    #N-7を最大値にする場合は、N-7をNで割った余りは2になる
    #N-8を最大値にする場合は、N-8をNで割った余りは3になる
    #N-9を最大値にする場合は、N-9をNで割った余りは4になる
    #N-10を最大値にする場合は、N-10をNで割った余りは0になる
    #N-11を最大値にする場合は、N-11をNで割った余りは1になる
    #N-12を最大値にする場合は、N-12をNで割った余りは2になる
    #N-13を最大値にする場合は、N-13をNで割った余りは3になる
    #N-14を最大値に
