Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n,k = map(int,input().split())
    s = input()
    ans = 0
    for i in range(n-1):
        if s[i] == s[i+1]:
            ans += 1
    ans += min(2*k,n-1)
    print(ans)

main()

=======
Suggestion 2

def main():
    n,k = map(int,input().split())
    s = list(input())
    # print(n,k,s)
    # print(s)
    # print(s[0])
    # print(s[1])
    # print(s[2])
    # print(s[3])
    # print(s[4])
    # print(s[5])
    # print(s[6])
    # print(s[7])
    # print(s[8])
    # print(s[9])
    # print(s[10])
    # print(s[11])
    # print(s[12])

    # print(s[0:2])
    # print(s[2:5])
    # print(s[5:6])
    # print(s[6:9])
    # print(s[9:10])
    # print(s[10:13])

    # print(s[0:3])
    # print(s[3:6])
    # print(s[6:9])
    # print(s[9:12])

    # print(s[0:4])
    # print(s[4:8])
    # print(s[8:12])

    # print(s[0:5])
    # print(s[5:10])
    # print(s[10:13])

    # print(s[0:6])
    # print(s[6:12])

    # print(s[0:7])
    # print(s[7:12])

    # print(s[0:8])
    # print(s[8:12])

    # print(s[0:9])
    # print(s[9:12])

    # print(s[0:10])
    # print(s[10:12])

    # print(s[0:11])
    # print(s[11:12])

    # print(s[0:12])
    # print(s[12:12])

    # print(s[0:13])
    # print(s[13:12])

    # print(s[0:14])
    # print(s[14:12])

    # print(s[0:15])
    # print(s[15:12])

    # print(s[0:16])
    # print(s[16:12])

    # print(s[0:17])
    # print(s[17:12])

    # print(s[0:18])
    # print(s[18:12])

=======
Suggestion 3

def solve():
    N,K = map(int,input().split())
    S = input()
    #print(N,K,S)
    happy_num = 0
    for i in range(N-1):
        if S[i] == S[i+1]:
            happy_num += 1
    #print(happy_num)
    happy_num += 2*K
    #print(happy_num)
    happy_num = min(happy_num,N-1)
    print(happy_num)
    return

=======
Suggestion 4

def main():
    N, K = map(int, input().split())
    S = input()
    happy = 0
    for i in range(N-1):
        if S[i] == S[i+1]:
            happy += 1
    print(min(happy+2*K, N-1))

=======
Suggestion 5

def main():
    N,K = map(int,input().split())
    S = input()
    S = S.replace('LR','R')
    S = S.replace('RL','L')
    if S[0] == 'R':
        S = 'L' + S
    if S[-1] == 'L':
        S = S + 'R'
    #print(S)
    count = 0
    for i in range(N-1):
        if S[i] == 'R' and S[i+1] == 'L':
            count += 1
    #print(count)
    if count <= K:
        print(N-1)
    else:
        print(N-1-(count-K)*2)

=======
Suggestion 6

def happy_people_num(N,K,S):
    happy_num = 0
    for i in range(N-1):
        if S[i] == S[i+1]:
            happy_num += 1
    happy_num = min(happy_num + 2 * K,N-1)
    return happy_num

=======
Suggestion 7

def main():
    pass

=======
Suggestion 8

def calc_happy_people(s):
    happy_people = 0
    for i in range(0, len(s) - 1):
        if s[i] == s[i + 1]:
            happy_people += 1
    return happy_people

=======
Suggestion 9

def main():
    n, k = map(int, input().split())
    s = input()
    num = 0
    for i in range(n-1):
        if s[i] == s[i+1]:
            num += 1
    num += min(2*k, n-1)
    print(num)

=======
Suggestion 10

def main():
    n,k = map(int,input().split())
    s = input()
    ans = 0
    for i in range(n-1):
        if s[i] == s[i+1]:
            ans += 1
    ans += 2*k
    print(min(ans,n-1))
