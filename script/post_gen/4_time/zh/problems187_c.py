Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    s = []
    for i in range(n):
        s.append(input())
    s = set(s)
    for i in s:
        if i[0] == '!':
            if i[1:] in s:
                print(i[1:])
                return
        elif '!' + i in s:
            print(i)
            return
    print('satisfiable')

=======
Suggestion 2

def main():
    N = int(input())
    S = []
    for i in range(N):
        S.append(input())

    S2 = []
    for i in range(N):
        if S[i][0] == '!':
            S2.append(S[i][1:])
        else:
            S2.append('!' + S[i])

    S2.sort()
    for i in range(N-1):
        if S2[i] == S2[i+1]:
            print(S2[i][1:])
            return

    print('satisfiable')

=======
Suggestion 3

def main():
    n = int(input())
    s = []
    for i in range(n):
        s.append(input())
    s.sort()
    for i in range(n-1):
        if s[i] == s[i+1]:
            print("!".join(s[i]))
            return
    print("satisfiable")

=======
Suggestion 4

def main():
    N = int(input())
    S = []
    for i in range(N):
        S.append(input())
    S.sort()
    for i in range(N):
        if S[i][0] == '!':
            if S[i][1:] in S:
                print(S[i][1:])
                return
        else:
            if '!' + S[i] in S:
                print(S[i])
                return
    print('satisfiable')

=======
Suggestion 5

def isSatisfy(strs):
    #print(strs)
    for i in range(len(strs)):
        if strs[i][0] == '!':
            if strs[i][1:] in strs:
                return strs[i][1:]
        else:
            if '!' + strs[i] in strs:
                return strs[i]
    return 'satisfy'

=======
Suggestion 6

def main():
    N = int(input())
    S = []
    for i in range(N):
        S.append(input())
    S.sort()
    for i in range(N-1):
        if S[i] == S[i+1]:
            print('存在不满足的字符串')
            return
    print('可满足')

=======
Suggestion 7

def main():
    n = int(input())
    s = []
    for i in range(n):
        s.append(input())
    s = set(s)
    for i in s:
        if "!" + i in s:
            print(i)
            exit()
    print("satisfiable")

=======
Suggestion 8

def get_input():
    N = int(input())
    S = []
    for i in range(N):
        S.append(input())
    return N, S

=======
Suggestion 9

def solve():
    n = int(input())
    s = set()
    for i in range(n):
        s.add(input())
    for i in s:
        if "!" + i in s:
            print(i)
            return
    print("satisfiable")
solve()

=======
Suggestion 10

def solve():
    N = int(input())
    S = []
    for i in range(N):
        S.append(input())
    
    S2 = set(S)
    for i in range(N):
        if S[i][0] == '!':
            if S[i][1:] in S2:
                return S[i][1:]
        else:
            if '!'+S[i] in S2:
                return S[i]
    return 'satisfiable'

print(solve())
