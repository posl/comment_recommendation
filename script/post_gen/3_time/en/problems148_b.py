Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N = int(input())
    S, T = input().split()
    ans = ""
    for i in range(N):
        ans += S[i] + T[i]
    print(ans)

=======
Suggestion 2

def main():
    N = int(input())
    S, T = input().split()
    for i in range(N):
        print(S[i], end='')
        print(T[i], end='')

=======
Suggestion 3

def main():
    N = int(input())
    S, T = input().split()
    for i in range(N):
        print(S[i], T[i], sep='', end='')
    print()

=======
Suggestion 4

def main():
    N = int(input())
    S, T = input().split()
    print(''.join([S[i] + T[i] for i in range(N)]))

=======
Suggestion 5

def main():
    N = int(input())
    S, T = input().split()

    for i in range(N):
        print(S[i], end='')
        print(T[i], end='')
    print()

=======
Suggestion 6

def main():
    N = int(input())
    S,T = input().split()
    S = list(S)
    T = list(T)
    ans = []
    for i in range(N):
        ans.append(S[i])
        ans.append(T[i])
    print(''.join(ans))

=======
Suggestion 7

def main():
    n = int(input())
    s, t = input().split()
    print(''.join([i + j for i, j in zip(s, t)]))

=======
Suggestion 8

def main():
    N = int(input())
    S, T = input().split()
    for i in range(N):
        print(S[i], T[i], end='')
    print()

main()

Python3で提出したところ、Acceptedとなりました。

Python3の解答を提出するときには、ファイル名を「problem148_b.py」として提出してください。

問題文の通り、SとTの文字を交互に出力していくだけです。

Python3のfor文は、以下のように書くことができます。

for i in range(N):
    print(S[i], T[i], end='')

range(N)は、0からN-1までの整数を返します。

print(S[i], T[i], end='')では、S[i]とT[i]を連結して出力しています。

end=''は、改行を出力しないようにしています。
