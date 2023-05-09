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

if __name__ == '__main__':
    main()