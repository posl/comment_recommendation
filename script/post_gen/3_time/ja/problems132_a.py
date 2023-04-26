Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    s = input()
    if len(set(s)) == 2:
        if s.count(s[0]) == 2 and s.count(s[1]) == 2:
            print("Yes")
        else:
            print("No")
    else:
        print("No")

=======
Suggestion 2

def main():
    s = input()
    if len(set(s)) == 2 and s.count(s[0]) == 2:
        print('Yes')
    else:
        print('No')

=======
Suggestion 3

def main():
    S = input()
    if len(set(S)) == 2 and S.count(S[0]) == 2:
        print("Yes")
    else:
        print("No")

=======
Suggestion 4

def main():
    S = input()
    if len(set(S)) == 2:
        if S.count(S[0]) == 2:
            print("Yes")
        else:
            print("No")
    else:
        print("No")
main()

=======
Suggestion 5

def main():
    S = input()
    S_set = set(S)
    if len(S_set) == 2:
        for s in S_set:
            if S.count(s) != 2:
                print("No")
                exit()
        print("Yes")
    else:
        print("No")

=======
Suggestion 6

def main():
    S = input()
    S_set = set(S)
    if len(S_set) == 2:
        for i in S_set:
            if S.count(i) != 2:
                print("No")
                exit()
        print("Yes")
    else:
        print("No")

=======
Suggestion 7

def main():
    s = input()
    print('Yes' if len(set(s)) == 2 and s.count(s[0]) == 2 else 'No')

=======
Suggestion 8

def main():
    S = input()
    if (len(set(S)) == 2) and (S.count(S[0]) == 2):
        print('Yes')
    else:
        print('No')

=======
Suggestion 9

def main():
    s = input()
    if len(s) == len(set(s)):
        print('Yes')
    else:
        print('No')

=======
Suggestion 10

def main():
    #input
    S = input()
    #compute
    S_set = set(S)
    #output
    if len(S_set) == 2:
        print("Yes")
    else:
        print("No")
