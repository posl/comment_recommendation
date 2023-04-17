Synthesizing 10/10 solutions

=======

def main():
    S = input()
    K = int(input())
    S = S.replace('1', '1')
    S = S.replace('2', '22')
    S = S.replace('3', '333')
    S = S.replace('4', '4444')
    S = S.replace('5', '55555')
    S = S.replace('6', '666666')
    S = S.replace('7', '7777777')
    S = S.replace('8', '88888888')
    S = S.replace('9', '999999999')
    print(S[K-1])

=======

def main():
    s = input()
    k = int(input())
    for i in range(k):
        if s[i] != '1':
            print(s[i])
            return
    print(1)

=======

def main():
    S = input()
    K = int(input())
    ans = 0
    for i in range(K):
        if S[i] != "1":
            ans = S[i]
            break
        else:
            ans = "1"
    print(ans)

=======

def main():
    S = input()
    K = int(input())

    for i in range(min(K, len(S))):
        if S[i] != '1':
            print(S[i])
            return
    print('1')

=======

def main():
    S = input()
    K = int(input())
    s = []
    for i in range(len(S)):
        if S[i] == "1":
            s.append("1")
        elif S[i] == "2":
            s.append("22")
        elif S[i] == "3":
            s.append("333")
        elif S[i] == "4":
            s.append("4444")
        elif S[i] == "5":
            s.append("55555")
        elif S[i] == "6":
            s.append("666666")
        elif S[i] == "7":
            s.append("7777777")
        elif S[i] == "8":
            s.append("88888888")
        elif S[i] == "9":
            s.append("999999999")
    s = "".join(s)
    print(s[K-1])

=======

def main():
    S = input()
    K = int(input())
    N = len(S)
    S = list(S)
    for i in range(N):
        if S[i] == '1':
            continue
        else:
            S[i] = '1'
            K -= 1
            if K == 0:
                break
    print(S[i])

main()

=======

def main():
    S = input()
    K = int(input())
    for i in range(5000):
        if len(S) >= K:
            break
        S = S.replace("2", "22")
        S = S.replace("3", "333")
        S = S.replace("4", "4444")
        S = S.replace("5", "55555")
        S = S.replace("6", "666666")
        S = S.replace("7", "7777777")
        S = S.replace("8", "88888888")
        S = S.replace("9", "999999999")
    print(S[K-1])

=======

def main():
    s = input()
    k = int(input())
    n = len(s)
    if k <= n:
        print(s[k-1])
    else:
        s = s.replace('1', '1 ')
        s = s.replace('2', '22 ')
        s = s.replace('3', '333 ')
        s = s.replace('4', '4444 ')
        s = s.replace('5', '55555 ')
        s = s.replace('6', '666666 ')
        s = s.replace('7', '7777777 ')
        s = s.replace('8', '88888888 ')
        s = s.replace('9', '999999999 ')
        s = s.split()
        print(s[k-1][0])

=======

def main():
    S = input()
    K = int(input())
    N = len(S)
    # 5000兆日後の文字列の長さ
    L = 0
    # 5000兆日後の文字列の最初の数字
    first = 0
    # 5000兆日後の文字列の最初の数字が何文字目にあるか
    first_index = 0
    # 5000兆日後の文字列の最初の数字が何文字目にあるかを探す
    for i in range(N):
        if S[i] != "1":
            first_index = i
            first = int(S[i])
            break
    # 5000兆日後の文字列の長さを計算する
    L = N - first_index + (first - 1) * (N - first_index)
    # K文字目が5000兆日後の文字列の最初の数字の場合
    if K <= L - (N - first_index):
        print(first)
    # K文字目が5000兆日後の文字列の最初の数字以外の場合
    else:
        print(S[first_index + K - (L - (N - first_index)) - 1])

=======

def main():
    S = input()
    K = int(input())
    # 5000兆日後の文字列の長さ
    L = len(S)*10**12
    # 5000兆日後の文字列の最初 K 文字が S である場合は K 文字目を出力
    if L <= K:
        print(S[K-1])
        return
    # 5000兆日後の文字列の最初 K 文字が S でない場合は, 5000兆日後の文字列の最初 K 文字が S である場合と同じ処理を行う.
    # 5000兆日後の文字列の最初 K 文字が S である場合と同じ処理を行うことで, 5000兆日後の文字列の最初 K 文字が S である場合と同じ処理を行う.
    # 5000兆日後の文字列の最初 K 文字が S である場合と同じ処理を行うことで, 5000兆日後の文字列の最初 K 文字が S である場合と同じ処理を行う.
    # 5000兆日後の文字列の最初 K 文字が S である場合と同じ処理を行うことで, 5000兆日後の文字列の最初 K 文字が S である場合と同じ処理を行う.
    # 5000兆日後の文字列の最初 K 文字が S である場合と同じ処理を行うことで, 5000兆日後の文字列の最初 K 文字が S である場合と同じ処理を行う.
    # 5000兆日後の文字列の最初 K 文字が S である場合と同じ処理を行うことで, 5000兆日後の文字列の最初 K 文字
