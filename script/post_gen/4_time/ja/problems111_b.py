Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N = input()
    if N[0] == N[1] == N[2]:
        print(N)
    elif N[1] == N[2]:
        print(N[0]+N[1]+N[1])
    elif N[0] == N[1]:
        print(N[0]+N[0]+N[2])
    elif N[0] == N[2]:
        print(N[0]+N[1]+N[0])
    else:
        print(N[0]+N[1]+N[2])

=======
Suggestion 2

def main():
    # input
    N = int(input())
    # compute
    if N % 111 == 0:
        ans = N
    else:
        ans = (N // 111 + 1) * 111
    # output
    print(ans)

=======
Suggestion 3

def main():
    n = int(input())
    for i in range(111, 1000, 111):
        if n <= i:
            print(i)
            break

=======
Suggestion 4

def main():
    N = int(input())
    while True:
        if N % 111 == 0:
            print(N)
            break
        else:
            N += 1

=======
Suggestion 5

def main():
    N = int(input())
    while True:
        if N % 111 == 0:
            print(N)
            return
        N += 1

=======
Suggestion 6

def main():
    N = int(input())
    if N < 100 or N > 999:
        print('Error: 100 ≦ N ≦ 999')
        return

    if N % 111 == 0:
        print(N)
    else:
        print(((N // 111) + 1) * 111)

=======
Suggestion 7

def main():
    N = int(input())
    while True:
        N += 1
        if N%111 == 0:
            print(N)
            break

=======
Suggestion 8

def main():
    # 標準入力受け取り
    n = int(input())
    # 初期化
    x = 0
    # ループ
    while x < 1000:
        if x >= n:
            print(x)
            break
        else:
            x += 111

=======
Suggestion 9

def main():
    N = int(input())
    print((N-1)//111*111+111)

main()
