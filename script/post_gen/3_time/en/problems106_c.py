Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    S = input()
    K = int(input())
    S = S.replace("1", "a")
    S = S.replace("2", "bb")
    S = S.replace("3", "ccc")
    S = S.replace("4", "dddd")
    S = S.replace("5", "eeeee")
    S = S.replace("6", "ffffff")
    S = S.replace("7", "ggggggg")
    S = S.replace("8", "hhhhhhhh")
    S = S.replace("9", "iiiiiiiii")
    S = S.replace("0", "jjjjjjjjjj")
    S = S.replace("a", "1")
    S = S.replace("b", "2")
    S = S.replace("c", "3")
    S = S.replace("d", "4")
    S = S.replace("e", "5")
    S = S.replace("f", "6")
    S = S.replace("g", "7")
    S = S.replace("h", "8")
    S = S.replace("i", "9")
    S = S.replace("j", "0")
    print(S[K-1])

=======
Suggestion 2

def main():
    s = input()
    k = int(input())
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
    for i in range(K):
        if S[i] != '1':
            print(S[i])
            return
    print(1)

=======
Suggestion 4

def main():
    s = input()
    k = int(input())
    s = s.replace('1', '1 ')
    s = s.replace('2', '2 22 ')
    s = s.replace('3', '3 333 ')
    s = s.replace('4', '4 4444 ')
    s = s.replace('5', '5 55555 ')
    s = s.replace('6', '6 666666 ')
    s = s.replace('7', '7 7777777 ')
    s = s.replace('8', '8 88888888 ')
    s = s.replace('9', '9 999999999 ')
    s = s.split()
    print(s[k-1])

=======
Suggestion 5

def main():
    S = input()
    K = int(input())
    if len(S) >= K:
        print(S[K-1])
        return
    for i in range(len(S)):
        if int(S[i]) > 1:
            print(S[i])
            return
    print(1)
main()

=======
Suggestion 6

def main():
    S = input()
    K = int(input())
    for i, s in enumerate(S):
        if s == "1":
            continue
        if i + int(s) >= K:
            print(s)
            break
        K -= int(s)

=======
Suggestion 7

def main():
    S = input()
    K = int(input())
    s = ''
    for i in range(K):
        s += S[i]
        if S[i] != '1':
            break
    if len(s) == K:
        print(S[K-1])
    else:
        print(s[0])

=======
Suggestion 8

def main():
    S = input()
    K = int(input())
    s = list(S)
    for i in range(len(s)):
        if s[i] == '1':
            K -= 1
        else:
            break
        if K == 0:
            print(s[i])
            return
    print(s[i])

=======
Suggestion 9

def  main():
    S = input()
    K = int(input())

    ans = 0
    for i in range(K):
        ans = int(S[i])
        if ans != 1:
            break

    print(ans)

=======
Suggestion 10

def findKthChar(s, k):
    l = len(s)
    if l >= k:
        return s[k - 1]
    else:
        return '1' if s[-1] == '1' else '9'

s = input()
k = int(input())
print(findKthChar(s, k))
