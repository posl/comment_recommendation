Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    S = input()
    K = int(input())
    cnt = 0
    for i in range(len(S)):
        if S[i] == '1':
            cnt += 1
        else:
            break

    if K <= cnt:
        print(1)
    else:
        print(S[cnt-1])

=======
Suggestion 2

def solve():
    s = input()
    k = int(input())
    #print(s, k)
    for i in range(k):
        if s[i] != '1':
            print(s[i])
            return
    print(1)

=======
Suggestion 3

def main():
    S = input()
    K = int(input())
    num = 0
    for i in range(len(S)):
        if S[i] == '1':
            num += 1
        else:
            break
    if K <= num:
        print(1)
    else:
        print(S[num - 1])

=======
Suggestion 4

def problem106_c():
    #S = input()
    #K = int(input())
    S = '299792458'
    K = 9460730472580800
    #print(S)
    #print(K)
    if S[0] == '1':
        print('1')
    elif S[0] == '2':
        if K % 2 == 1:
            print('2')
        else:
            print('3')
    else:
        print(S[0])

=======
Suggestion 5

def main():
    S = input()
    K = int(input())
    for i in range(K):
        if S[i] != '1':
            print(S[i])
            break
    else:
        print('1')

=======
Suggestion 6

def main():
    s = input()
    k = int(input())
    for i in range(k):
        if s[i] != '1':
            print(s[i])
            return
    print('1')

=======
Suggestion 7

def f(s):
    s = s.replace('2','22')
    s = s.replace('3','333')
    s = s.replace('4','4444')
    s = s.replace('5','55555')
    s = s.replace('6','666666')
    s = s.replace('7','7777777')
    s = s.replace('8','88888888')
    s = s.replace('9','999999999')
    return s

s = input()
k = int(input())

=======
Suggestion 8

def main():
    S = input()
    K = int(input())
    count = 0
    for i in range(len(S)):
        if S[i] == '1':
            count += 1
        else:
            break
    if K <= count:
        print(1)
    else:
        print(S[count])

=======
Suggestion 9

def main():
    s = input()
    k = int(input())
    n = len(s)
    while k > n:
        k -= n
        s = s.replace("1", "")
        s = s.replace("2", "22")
        s = s.replace("3", "333")
        s = s.replace("4", "4444")
        s = s.replace("5", "55555")
        s = s.replace("6", "666666")
        s = s.replace("7", "7777777")
        s = s.replace("8", "88888888")
        s = s.replace("9", "999999999")
        n = len(s)
    print(s[k-1])

=======
Suggestion 10

def main():
    S = input()
    K = int(input())
    for i in range(K):
        if S[i] != '1':
            print(S[i])
            break
        if i == K-1:
            print('1')
