Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def func(s, k):
    if k < len(s):
        return s[k-1]
    else:
        return func(s, k-len(s))

=======
Suggestion 2

def main():
    S = input()
    K = int(input())
    for i in range(len(S)):
        if S[i] != '1':
            print(S[i])
            return
        elif i + 1 == K:
            print(S[i])
            return
main()

=======
Suggestion 3

def getKth(s, k):
    if len(s) == 1:
        return s
    if len(s) == 2:
        if k == 1:
            return s[0]
        else:
            return s[1]
    if len(s) == 3:
        if k == 1:
            return s[0]
        elif k == 2:
            return s[1]
        else:
            return s[2]
    if len(s) == 4:
        if k == 1:
            return s[0]
        elif k == 2:
            return s[1]
        elif k == 3:
            return s[2]
        else:
            return s[3]
    else:
        if k <= len(s):
            return s[k-1]
        else:
            return getKth(s[0] * len(s), k % len(s))

=======
Suggestion 4

def main():
    s = input()
    k = int(input())
    for i in range(k):
        if s[i] != '1':
            print(s[i])
            break
        if i == k-1:
            print('1')

=======
Suggestion 5

def problem106_c(s, k):
    s = list(s)
    for i in range(10):
        s = [str(i) if x == str(i) else x for x in s]
        s = [x * (i + 1) if x == str(i) else x for x in s]
    s = ''.join(s)
    print(s[k - 1])

=======
Suggestion 6

def main():
    s = input()
    k = int(input())
    for i in range(k):
        if s[i] != '1':
            print(s[i])
            return
    print(1)

=======
Suggestion 7

def f1(s):
    s1 = ''
    for i in s:
        s1 += i*int(i)
    return s1

=======
Suggestion 8

def get_str(s):
    result = ""
    for i in s:
        result += i * int(i)
    return result

=======
Suggestion 9

def main():
    s = input()
    k = int(input())
    a = 0
    b = 0
    c = 0
    for i in range(len(s)):
        if s[i] == '1':
            a += 1
        elif s[i] == '2':
            b += 1
        elif s[i] == '3':
            c += 1
    if k <= a:
        print('1')
    elif k <= a + b:
        print('2')
    else:
        print('3')
