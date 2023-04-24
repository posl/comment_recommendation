Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    S = input()
    K = int(input())
    S = S.replace('1','1 ').replace('2','22 ').replace('3','333 ').replace('4','4444 ').replace('5','55555 ').replace('6','666666 ').replace('7','7777777 ').replace('8','88888888 ').replace('9','999999999 ')
    S = S.split()
    ans = ''
    for i in range(K):
        ans += S[i]
    print(ans[K-1])

=======
Suggestion 2

def main():
    S = input()
    K = int(input())
    S = S.replace('1','1,').replace('2','22,').replace('3','333,').replace('4','4444,').replace('5','55555,').replace('6','666666,').replace('7','7777777,').replace('8','88888888,').replace('9','999999999,')
    S = S.split(',')
    S = list(map(int,S))
    print(S[K-1])

=======
Suggestion 3

def main():
    s = input()
    k = int(input())
    s = s.replace('1','1').replace('2','22').replace('3','333').replace('4','4444').replace('5','55555').replace('6','666666').replace('7','7777777').replace('8','88888888').replace('9','999999999')
    print(s[k-1])

=======
Suggestion 4

def main():
    S = input()
    K = int(input())
    count = 0
    for i in S:
        if i == "1":
            count += 1
        else:
            break
    if count >= K:
        print(1)
    else:
        print(S[count])

=======
Suggestion 5

def main():
    s = input()
    k = int(input())
    #print(s)
    #print(k)
    s = s.replace("2","22")
    s = s.replace("3","333")
    s = s.replace("4","4444")
    s = s.replace("5","55555")
    s = s.replace("6","666666")
    s = s.replace("7","7777777")
    s = s.replace("8","88888888")
    s = s.replace("9","999999999")
    #print(s)
    print(s[k-1])

=======
Suggestion 6

def main():
    S = input()
    K = int(input())
    N = len(S)
    if N == 1:
        print(S)
        return
    if N == 2:
        if S[0] == S[1]:
            print(S[0])
        else:
            print(S[1])
        return
    if S[0] == S[1]:
        if S[1] == S[2]:
            print(S[0])
        else:
            print(S[2])
    else:
        print(S[1])

=======
Suggestion 7

def main():
    S = input()
    K = int(input())
    ans = ""
    for i in range(K):
        ans += S[i%len(S)]
        if ans[-1] != "1":
            print(ans[-1])
            break
    else:
        print(1)

=======
Suggestion 8

def main():
    S = input()
    K = int(input())
    N = len(S)
    if N >= K:
        print(S[K-1])
        return
    else:
        K -= N
        for i in range(N):
            if S[i] == '1':
                continue
            else:
                print(S[i])
                return
        print(S[-1])

=======
Suggestion 9

def main():
    s = input()
    k = int(input())
    #print(s)
    #print(k)
    #print(len(s))
    for i in range(k):
        if i == k-1:
            print(s[0])
        if s[0] == '1':
            s = s[1:]
        else:
            s = s[0] + str(int(s[0])-1) + s[1:]

=======
Suggestion 10

def main():
    S = input()
    K = int(input())
    # print(S,K)

    # 1日後の文字列を作る
    S2 = ""
    for i in range(len(S)):
        s = S[i]
        if s == "1":
            S2 += "1"
        else:
            S2 += s * int(s)

    # 2日後の文字列を作る
    S3 = ""
    for i in range(len(S2)):
        s = S2[i]
        if s == "1":
            S3 += "1"
        else:
            S3 += s * int(s)

    # 3日後の文字列を作る
    S4 = ""
    for i in range(len(S3)):
        s = S3[i]
        if s == "1":
            S4 += "1"
        else:
            S4 += s * int(s)

    # 5000兆日後の文字列を作る
    S5000 = ""
    for i in range(len(S4)):
        s = S4[i]
        if s == "1":
            S5000 += "1"
        else:
            S5000 += s * int(s)

    # 5000兆日後の文字列のK文字目を出力
    print(S5000[K-1])
