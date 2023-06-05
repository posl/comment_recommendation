Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    s = input()
    q = int(input())
    for i in range(q):
        t, k = map(int, input().split())
        for j in range(t):
            s = s.replace('a', 'bc').replace('b', 'ca').replace('c', 'ab')
        print(s[k-1])

=======
Suggestion 2

def main():
    s = input()
    q = int(input())
    t_list = []
    k_list = []
    for i in range(q):
        t,k = map(int,input().split())
        t_list.append(t)
        k_list.append(k)

    for i in range(q):
        t = t_list[i]
        k = k_list[i]
        for j in range(t):
            s = s.replace('a','bc')
            s = s.replace('b','ca')
            s = s.replace('c','ab')
        print(s[k-1])

=======
Suggestion 3

def replace(s):
    s2 = ''
    for i in range(len(s)):
        if s[i] == 'a':
            s2 += 'bc'
        elif s[i] == 'b':
            s2 += 'ca'
        else:
            s2 += 'ab'
    return s2

s = input()
q = int(input())

for i in range(q):
    t, k = map(int, input().split())
    for j in range(t):
        s = replace(s)
    print(s[k - 1])

=======
Suggestion 4

def replace(s):
    s = s.replace('a', 'bc')
    s = s.replace('b', 'ca')
    s = s.replace('c', 'ab')
    return s

=======
Suggestion 5

def main():
    s = input()
    q = int(input())
    for _ in range(q):
        t,k = map(int, input().split())
        for i in range(t+1):
            s = s.replace('a', 'bc')
            s = s.replace('b', 'ca')
            s = s.replace('c', 'ab')
        print(s[k-1])

=======
Suggestion 6

def main():
    s = input()
    q = int(input())
    for i in range(q):
        t, k = map(int, input().split())
        k -= 1
        for j in range(t):
            k = (k + 1) % len(s)
            if s[k] == 'a':
                s = s[:k] + 'bc' + s[k + 1:]
            elif s[k] == 'b':
                s = s[:k] + 'ca' + s[k + 1:]
            elif s[k] == 'c':
                s = s[:k] + 'ab' + s[k + 1:]
        print(s[k])

=======
Suggestion 7

def problem242_d():
    pass

=======
Suggestion 8

def main():
    s = input()
    q = int(input())
    for i in range(q):
        t, k = map(int, input().split())
        for j in range(t+1):
            s = s.replace('a', 'bc')
            s = s.replace('b', 'ca')
            s = s.replace('c', 'ab')
        print(s[k-1])

=======
Suggestion 9

def main():
    s = input()
    q = int(input())
    for _ in range(q):
        t, k = map(int, input().split())
        t %= 3
        k -= 1
        for i in range(t, t + k):
            k %= 3
            if s[i] == 'a':
                if k == 0:
                    print('a')
                    break
                elif k == 1:
                    print('b')
                    break
                else:
                    print('c')
                    break
            elif s[i] == 'b':
                if k == 0:
                    print('b')
                    break
                elif k == 1:
                    print('c')
                    break
                else:
                    print('a')
                    break
            else:
                if k == 0:
                    print('c')
                    break
                elif k == 1:
                    print('a')
                    break
                else:
                    print('b')
                    break
