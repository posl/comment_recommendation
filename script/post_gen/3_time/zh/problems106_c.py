Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    s = input()
    k = int(input())
    n = len(s)
    for i in range(n):
        if s[i] != '1':
            break
    if i == n-1:
        print(1)
        return
    if k <= i+1:
        print(1)
        return
    if k > n:
        print(s[i+1])
        return
    print(s[k-1])

=======
Suggestion 2

def main():
    s = input()
    k = int(input())
    for i in range(k):
        if s[i] != "1":
            print(s[i])
            break
    else:
        print(1)

=======
Suggestion 3

def main():
    s = input()
    k = int(input())
    if k == 1:
        print(s[0])
        return
    i = 0
    while i < k:
        if s[i] == '1':
            i += 1
        else:
            break
    if i == k:
        print(1)
        return
    print(s[i])

=======
Suggestion 4

def main():
    S = input()
    K = int(input())
    print(S[K-1])

=======
Suggestion 5

def main():
    s = input()
    k = int(input())
    cnt = 0
    for i in range(len(s)):
        if s[i] != "1":
            cnt += 1
            if cnt == k:
                print(s[i])
                return
        else:
            cnt = 0
            if cnt == k:
                print(1)
                return
    print(1)
    return

=======
Suggestion 6

def main():
    S = input()
    K = int(input())
    count = 0
    for i in range(len(S)):
        if S[i] == '1':
            count += 1
        else:
            break
    if count >= K:
        print(1)
    else:
        print(S[count])

=======
Suggestion 7

def main():
    S = input()
    K = int(input())
    i = 0
    while i < K:
        if S[i] != "1":
            break
        i += 1
    print(S[i])

=======
Suggestion 8

def main():
    s = input()
    k = int(input())
    s = list(s)
    for i in range(k):
        if s[i] != '1':
            print(s[i])
            break
        if i == k - 1:
            print('1')

=======
Suggestion 9

def main():
    s = input()
    k = int(input())
    #print(s)
    #print(k)
    #print(len(s))
    #print(s.count('2'))
    #print(s.count('3'))
    #print(s.count('4'))
    #print(s.count('5'))
    #print(s.count('6'))
    #print(s.count('7'))
    #print(s.count('8'))
    #print(s.count('9'))
    #print(s.count('1'))
    #print(s[0])
    
    #k = k % 100
    #print(k)
    #print(s.count('2') * 2)
    #print(s.count('3') * 3)
    #print(s.count('4') * 4)
    #print(s.count('5') * 5)
    #print(s.count('6') * 6)
    #print(s.count('7') * 7)
    #print(s.count('8') * 8)
    #print(s.count('9') * 9)
    #print(s.count('1') * 1)
    #print(s.count('2') * 2 + s.count('3') * 3 + s.count('4') * 4 + s.count('5') * 5 + s.count('6') * 6 + s.count('7') * 7 + s.count('8') * 8 + s.count('9') * 9 + s.count('1') * 1)
    #print(len(s))
    #print(s.count('2') * 2 + s.count('3') * 3 + s.count('4') * 4 + s.count('5') * 5 + s.count('6') * 6 + s.count('7') * 7 + s.count('8') * 8 + s.count('9') * 9 + s.count('1') * 1)
    #print( k - (s.count('2') * 2 + s.count('3') * 3 + s.count('4') * 4 + s.count('5') * 5 + s.count('6') * 6 + s.count('7') * 7 + s.count('8') * 8 + s.count('9') * 9 + s.count('1') * 1))
    #print(s.count('2

=======
Suggestion 10

def main():
    s = input()
    k = int(input())
    # print(s)
    # print(k)
    count = 0
    for i in range(len(s)):
        if s[i] == '1':
            count += 1
        else:
            break
    if k <= count:
        print(1)
    else:
        print(s[count-1])
