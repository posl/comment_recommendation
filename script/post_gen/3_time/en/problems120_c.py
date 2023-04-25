Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    S = input()
    red = 0
    blue = 0
    for i in range(len(S)):
        if S[i] == "0":
            red += 1
        else:
            blue += 1
    print(min(red, blue) * 2)

=======
Suggestion 2

def main():
    S = input()
    count = 0
    for i in range(len(S) - 1):
        if S[i] != S[i + 1]:
            count += 1
    print(count)

=======
Suggestion 3

def main():
    s = input()
    ans = 0
    for i in range(len(s)-1):
        if s[i] != s[i+1]:
            ans += 1
    print(ans)

=======
Suggestion 4

def main():
    S = input()
    print(min(S.count('0'), S.count('1')) * 2)

=======
Suggestion 5

def main():
    s = input()
    print(min(s.count('0'), s.count('1')) * 2)

=======
Suggestion 6

def main():
    S = input()
    N = len(S)
    if N == 1:
        print(0)
        return
    if N == 2:
        if S == '00' or S == '11':
            print(0)
        else:
            print(1)
        return
    if S[0] == S[1]:
        print(1 + main(S[1:]))
    else:
        print(2 + main(S[2:]))

=======
Suggestion 7

def main():
    S = input()
    print(min(S.count('0'),S.count('1'))*2)

main()

=======
Suggestion 8

def main():
    s = list(input())
    print(min(s.count('0'), s.count('1')) * 2)

=======
Suggestion 9

def main():
    S = input()
    N = len(S)
    #count red
    red = 0
    for i in range(N):
        if S[i] == '0':
            red += 1
    #count blue
    blue = 0
    for i in range(N):
        if S[i] == '1':
            blue += 1
    #print the result
    print(min(red, blue) * 2)
