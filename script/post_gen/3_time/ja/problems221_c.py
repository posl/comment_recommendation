Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = input()
    N = list(N)
    N.sort(reverse=True)
    a = 0
    b = 0
    for i in range(len(N)):
        if i % 2 == 0:
            a = a * 10 + int(N[i])
        else:
            b = b * 10 + int(N[i])
    print(a * b)

=======
Suggestion 2

def main():
    N = input()
    N = list(N)
    N.sort(reverse=True)
    print(int(''.join(N[0:len(N)//2])) * int(''.join(N[len(N)//2:])))

=======
Suggestion 3

def main():
    N = input()
    N = [int(i) for i in N]
    N.sort(reverse=True)
    N1 = N[0]
    N2 = 0
    for i in range(1, len(N)):
        N2 += N[i] * (10 ** (i - 1))
    print(N1 * N2)

=======
Suggestion 4

def main():
    N = input()
    N = list(N)
    N = list(map(int, N))
    N.sort(reverse=True)
    N = list(map(str, N))
    N = ''.join(N)
    N = int(N)
    N1 = N
    N2 = 0
    for i in range(1, N):
        N1 = N1 // 10
        N2 = N2 * 10 + N % 10
        N = N // 10
        if N1 * N2 > N:
            break
    print(N1 * N2)

=======
Suggestion 5

def main():
    n = input()
    n = list(n)
    n.sort(reverse=True)
    a = n[0]
    b = n[1]
    for i in range(2,len(n)):
        if int(a+b) < int(b+a):
            a += n[i]
        else:
            b += n[i]
    print(int(a)*int(b))

=======
Suggestion 6

def main():
    N = input()
    N = [int(i) for i in N]
    N.sort(reverse=True)
    print(N[0]*N[1])

=======
Suggestion 7

def main():
    N = input()
    N = list(N)
    N = [int(i) for i in N]
    N.sort()
    N.reverse()
    N1 = N[0]
    N2 = N[1]
    for i in range(2,len(N)):
        if N1 <= N2:
            N1 = N1*10 + N[i]
        else:
            N2 = N2*10 + N[i]
    print(N1*N2)

main()

=======
Suggestion 8

def main():
    N = input()
    N = list(N)
    N.sort(reverse=True)
    N = int("".join(N))
    print(N)

=======
Suggestion 9

def main():
    N = input()

    # Nの桁数を取得
    digit = len(N)

    # Nをリストに変換
    N_list = list(map(int, N))

    # Nの各桁の数字を取り出して並べる（並べる順序は好きに変えてよい）
    # 2つの正整数に分離することを考える
    # 例えば、123 という整数に対しては以下の 6 通りの分離の仕方が考えられる
    # 12 と 3
    # 21 と 3
    # 13 と 2
    # 31 と 2
    # 23 と 1
    # 32 と 1
    # なお、ここで分離されたあとの 2 整数に leading zero が含まれていてはなりません。
    # 例えば、101 という整数を 1 と 01 の 2 つに分離することはできない。
    # また上述の「正整数に分離する」という条件より、101 を 11 と 0 の 2 つに分離することもできない。
    # 適切に N を分離したとき、分離後の 2 数の積の最大値はいくらになるか？
    # Nの桁数を取得
    digit = len(N)

    # Nをリストに変換
    N_list = list(map(int, N))

    # Nの各桁の数字を取り出して並べる（並べる順序は好きに変えてよい）
    # 2つの正整数に分離することを考える
    # 例えば、123 という整数に対しては以下の 6 通りの分離の

=======
Suggestion 10

def main():
    n = input()
    # n = 998244353
    n = list(n)
    n = list(map(int, n))
    n.sort()
    n.reverse()
    # print(n)
    a = n[0]
    b = n[1]
    for i in range(2, len(n)):
        if a > b:
            b = b * 10 + n[i]
        else:
            a = a * 10 + n[i]
    print(a * b)
