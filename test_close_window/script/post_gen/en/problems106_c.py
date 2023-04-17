Synthesizing 10/10 solutions

=======

def main():
    S = input()
    K = int(input())
    S = S.replace('1', 'a')
    S = S.replace('2', 'b')
    S = S.replace('3', 'c')
    S = S.replace('4', 'd')
    S = S.replace('5', 'e')
    S = S.replace('6', 'f')
    S = S.replace('7', 'g')
    S = S.replace('8', 'h')
    S = S.replace('9', 'i')
    print(S[K-1])

=======

def main():
    S = input()
    K = int(input())
    l = len(S)
    if l >= K:
        print(S[K-1])
    else:
        for i in range(l):
            if S[i] != '1':
                print(S[i])
                break

=======

def main():
    S = input()
    K = int(input())
    for i in range(K):
        if S[i] != "1":
            print(S[i])
            return
    print(1)
    return

=======

def main():
    s = input()
    k = int(input())
    ans = '1'
    for i in range(len(s)):
        if s[i] != '1':
            ans = s[i]
            break
    if k <= i:
        ans = '1'
    print(ans)

=======

def main():
    S = input()
    K = int(input())

    for i in range(len(S)):
        if S[i] != '1':
            if K > i:
                print(S[i])
                return
            else:
                print(1)
                return

    print(S[-1])

=======

def main():
    S = input()
    K = int(input())
    ans = 0
    for i in range(K):
        ans = S[i]
        if ans != "1":
            break
    print(ans)

=======

def main():
    S = input()
    K = int(input())
    #print(S)
    #print(K)
    S = S.replace('1', 'a')
    S = S.replace('2', 'b')
    S = S.replace('3', 'c')
    S = S.replace('4', 'd')
    S = S.replace('5', 'e')
    S = S.replace('6', 'f')
    S = S.replace('7', 'g')
    S = S.replace('8', 'h')
    S = S.replace('9', 'i')
    #print(S)
    #print(len(S))
    if len(S) < K:
        print(S[-1])
    else:
        print(S[K-1])

=======

def main():
    S = input()
    K = int(input())
    #print(S)
    #print(K)
    count = 0
    for s in S:
        if s == '1':
            count += 1
            if count == K:
                print(1)
                return
        else:
            print(s)
            return

=======

def main():
    S = input()
    K = int(input())
    if S == "1":
        print(1)
        return
    if S[0] == "1":
        if K == 1:
            print(1)
            return
        else:
            S = S[1:]
            K -= 1
    for i in range(len(S)):
        if int(S[i]) != 1:
            print(S[i])
            return

=======

def find_nth_digit(n):
    n = int(n)
    if n == 0:
        return 0
    #Find the length of the number where the nth digit is from
    #Number starts from 1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99, 111, 222, 333, 444, 555, 666, 777, 888, 999, 1111, 2222, 3333, 4444, 5555, 6666, 7777, 8888, 9999, 11111, 22222, 33333, 44444, 55555, 66666, 77777, 88888, 99999, 111111, 222222, 333333, 444444, 555555, 666666, 777777, 888888, 999999, 1111111, 2222222, 3333333, 4444444, 5555555, 6666666, 7777777, 8888888, 9999999, 11111111, 22222222, 33333333, 44444444, 55555555, 66666666, 77777777, 88888888, 99999999, 111111111, 222222222, 333333333, 444444444, 555555555, 666666666, 777777777, 888888888, 999999999, 1111111111, 2222222222, 3333333333, 4444444444, 5555555555, 6666666666, 7777777777, 8888888888, 9999999999, 11111111111, 22222222222, 33333333333, 44444444444, 55555555555, 66666666666, 77777777777, 88888888888, 99999999999, 111111111111, 222222222222, 333333333333, 444444444444,
