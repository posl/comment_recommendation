Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    sum = 0
    for i in str(n):
        sum += int(i)
    if n % sum == 0:
        print("Yes")
    else:
        print("No")

=======
Suggestion 2

def main():
    n = int(input())
    sum = 0
    for i in str(n):
        sum += int(i)
    if n % sum == 0:
        print('Yes')
    else:
        print('No')

=======
Suggestion 3

def main():
    n = int(input())
    s = sum([int(i) for i in str(n)])
    if n % s == 0:
        print('Yes')
    else:
        print('No')

=======
Suggestion 4

def main():
    N = int(input())
    S = 0
    while N > 0:
        S += N % 10
        N //= 10
    if S % 3 == 0:
        print("Yes")
    else:
        print("No")

=======
Suggestion 5

def main():
    N = input()
    N = int(N)
    S = 0
    for i in str(N):
        S += int(i)
    if N % S == 0:
        print("Yes")
    else:
        print("No")

=======
Suggestion 6

def main():
    n = input()
    s = 0
    for c in n:
        s += int(c)
    print("Yes" if int(n) % s == 0 else "No")

=======
Suggestion 7

def main():
    N = int(input())
    N_list = list(map(int, list(str(N))))
    S_N = sum(N_list)
    if N % S_N == 0:
        print('Yes')
    else:
        print('No')

=======
Suggestion 8

def main():
    N = input()
    s = sum([int(i) for i in N])
    if int(N)%s == 0:
        print("Yes")
    else:
        print("No")

=======
Suggestion 9

def main():
    N = input()
    N = int(N)
    S = 0
    if N < 10:
        S = N
    else:
        for i in range(len(N)):
            S = S + int(N[i])
    if N % S == 0:
        print("Yes")
    else:
        print("No")

=======
Suggestion 10

def main():
    # 入力
    N = int(input())
    # Nの桁数を調べる
    keta = len(str(N))
    # Nの各桁の値を調べる
    s = 0
    for i in range(keta):
        s += int(str(N)[i])
    # 出力
    if N % s == 0:
        print("Yes")
    else:
        print("No")
