Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    S = input()
    K = int(input())
    n = len(S)
    i = 0
    while i < n and int(S[i]) == 1:
        i += 1
    if i == n:
        print(1)
    elif K <= i:
        print(1)
    else:
        print(S[i])
main()

=======
Suggestion 2

def main():
    S = input()
    K = int(input())
    #print(S)
    #print(K)
    if K == 1:
        print(S[0])
        return
    if K == 2:
        print(S[0])
        return
    if K == 3:
        if S[0] == '1':
            print(1)
            return
        else:
            print(S[0])
            return
    if K == 4:
        if S[0] == '1':
            print(2)
            return
        else:
            print(S[0])
            return
    if K == 5:
        if S[0] == '1':
            print(2)
            return
        else:
            print(S[0])
            return
    if K == 6:
        if S[0] == '1':
            print(2)
            return
        else:
            print(S[0])
            return
    if K == 7:
        if S[0] == '1':
            print(2)
            return
        else:
            print(S[0])
            return
    if K == 8:
        if S[0] == '1':
            print(2)
            return
        else:
            print(S[0])
            return
    if K == 9:
        if S[0] == '1':
            print(2)
            return
        else:
            print(S[0])
            return
    if K == 10:
        if S[0] == '1':
            print(2)
            return
        else:
            print(S[0])
            return
    #print(S)
    #print(K)
    if S[0] == '1':
        print(2)
        return
    else:
        print(S[0])
        return

=======
Suggestion 3

def main():
    s = input()
    k = int(input())
    print(solve(s,k))

=======
Suggestion 4

def main():
    s = input()
    k = int(input())
    i = 0
    while i < k:
        if s[i] == '1':
            i += 1
        else:
            break
    print(s[i])

=======
Suggestion 5

def replace_num(num):
    num = str(num)
    num = num.replace('2','22')
    num = num.replace('3','333')
    num = num.replace('4','4444')
    num = num.replace('5','55555')
    num = num.replace('6','666666')
    num = num.replace('7','7777777')
    num = num.replace('8','88888888')
    num = num.replace('9','999999999')
    return num

=======
Suggestion 6

def get_next(s):
    next_s = ''
    for i in s:
        next_s += i*i
    return next_s

=======
Suggestion 7

def main():
    s = input()
    k = int(input())
    #print(s)
    #print(k)
    #print(len(s))
    if len(s) >= k:
        print(s[k-1])
    else:
        #print("here")
        #print(len(s))
        #print(k)
        #print(k % len(s))
        print(s[k % len(s) - 1])
    return 0

=======
Suggestion 8

def main():
    str = input()
    k = int(input())
    i = 0
    while i < k:
        if str[i] == '1':
            i += 1
        else:
            str = str.replace(str[i], str[i] * int(str[i]), 1)
            i += int(str[i])
    print(str[k - 1])
main()

=======
Suggestion 9

def main():
    s = input()
    k = int(input())
    s = list(s)
    for i in range(k):
        if s[i] == '1':
            continue
        else:
            print(s[i])
            break

=======
Suggestion 10

def count_num(s):
    return s.count('1') + s.count('2') * 2 + s.count('3') * 3 + s.count('4') * 4 + s.count('5') * 5 + s.count('6') * 6 + s.count('7') * 7 + s.count('8') * 8 + s.count('9') * 9
