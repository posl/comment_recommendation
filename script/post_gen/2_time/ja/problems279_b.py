Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    S = input()
    T = input()
    if T in S:
        print("Yes")
    else:
        print("No")

=======
Suggestion 2

def main():
    S = input()
    T = input()
    if T in S:
        print('Yes')
    else:
        print('No')

=======
Suggestion 3

def main():
    s = input()
    t = input()
    if t in s:
        print("Yes")
    else:
        print("No")

=======
Suggestion 4

def main():
    s = input()
    t = input()
    if t in s:
        print('Yes')
    else:
        print('No')

=======
Suggestion 5

def main():
    S = input()
    T = input()
    if S == T:
        print('Yes')
    else:
        for i in range(len(S)):
            if S[i] == T[0]:
                if S[i:i+len(T)] == T:
                    print('Yes')
                    return
        print('No')

=======
Suggestion 6

def main():
    # S,T = [input() for i in range(2)]
    S,T = input().split()
    print("Yes" if T in S else "No")
