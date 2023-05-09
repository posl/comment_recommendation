Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    s = input()
    k = int(input())
    for i in range(k):
        if s[i] != '1':
            print(s[i])
            return
    print('1')

=======
Suggestion 2

def main():
    s = input()
    k = int(input())
    if k <= len(s):
        print(s[k-1])
    else:
        for i in range(len(s)):
            if s[i] != '1':
                print(s[i])
                break

=======
Suggestion 3

def main():
    S = input()
    K = int(input())
    for i in range(len(S)):
        if S[i] != '1':
            print(S[i])
            return
        elif i == K-1:
            print(S[i])
            return

=======
Suggestion 4

def main():
    s = input()
    k = int(input())
    
    count = 0
    for c in s:
        if c == '1':
            count += 1
        else:
            break

    if k <= count:
        print(1)
    else:
        print(s[count])

=======
Suggestion 5

def main():
    s = input()
    k = int(input())

    for i in range(k):
        if s[i] != "1":
            print(s[i])
            break
    else:
        print("1")

=======
Suggestion 6

def main():
    S = input()
    K = int(input())
    for i in range(len(S)):
        if S[i] != '1':
            print(S[i])
            break
        elif K == i+1:
            print(1)
            break
main()

=======
Suggestion 7

def main():
    S = input()
    K = int(input())
    if S[0] != '1':
        print(S[0])
    else:
        cnt = 0
        for s in S:
            if s == '1':
                cnt += 1
            else:
                break
        if K <= cnt:
            print('1')
        else:
            print(S[cnt-1])

=======
Suggestion 8

def main():
    s = input()
    k = int(input())
    print(s[k-1])

=======
Suggestion 9

def main():
    s = input()
    k = int(input())
    l = len(s)
    if k <= l:
        print(s[k-1])
        exit()
    i = 0
    while True:
        if 2**i >= k:
            break
        i += 1
    print(s[i-1])
main()

=======
Suggestion 10

def get_input():
    S = input()
    K = int(input())
    return S, K
