Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    s = input()
    k = int(input())
    i = 0
    while i < len(s):
        if s[i] != "1":
            break
        i += 1
    if k <= i:
        print(1)
    else:
        print(s[i])

=======
Suggestion 2

def main():
    s = input()
    k = int(input())
    cnt = 0
    for i in range(len(s)):
        if s[i] != '1':
            cnt = i
            break
    if k <= cnt:
        print(1)
    else:
        print(s[cnt])

=======
Suggestion 3

def main():
    S = input()
    K = int(input())
    print(S[(K-1)%len(S)])

=======
Suggestion 4

def main():
    s = input()
    k = int(input())
    print(s[k-1])

=======
Suggestion 5

def get_string(s, k):
    if k == 0:
        return s[0]
    i = 0
    while True:
        if i >= len(s):
            break
        n = int(s[i])
        if n != 1:
            if k <= len(s[i:]) * (n - 1):
                return s[i + (k - 1) // (n - 1)]
            k -= len(s[i:]) * (n - 1)
        i += 1
    return s[-1]

=======
Suggestion 6

def main():
    s = input()
    k = int(input())
    if k < len(s):
        print(s[k-1])
        return
    else:
        if s[0] == '1':
            for i in range(len(s)):
                if s[i] != '1':
                    print(s[i])
                    return
        else:
            print(s[0])
            return

=======
Suggestion 7

def main():
    s = input()
    k = int(input())
    i = 0
    while i < len(s) and s[i] == '1':
        i += 1
    if i >= k:
        print(1)
    else:
        print(s[i])

=======
Suggestion 8

def main():
    s = input()
    k = int(input())
    #print(s)
    #print(k)
    s_list = []
    s_list.append(s)
    for i in range(1, k + 1):
        #print(i)
        s_list.append(s_list[i - 1])
        #print(s_list)
        s_list[i] = s_list[i].replace('2', '22')
        s_list[i] = s_list[i].replace('3', '333')
        s_list[i] = s_list[i].replace('4', '4444')
        s_list[i] = s_list[i].replace('5', '55555')
        s_list[i] = s_list[i].replace('6', '666666')
        s_list[i] = s_list[i].replace('7', '7777777')
        s_list[i] = s_list[i].replace('8', '88888888')
        s_list[i] = s_list[i].replace('9', '999999999')
        #print(s_list[i])
    print(s_list[k - 1][k - 1])

=======
Suggestion 9

def main():
    s = input()
    k = int(input())
    n = len(s)
    #print(s)
    #print(k)
    #print(n)
    #print(s[0])
    #print(s[1])
    #print(s[2])
    #print(s[3])

    for i in range(n):
        if i == k-1:
            print(s[i])
            break

=======
Suggestion 10

def main():
    S = input()
    K = int(input())
    print(S[(K-1)%(len(S))])
