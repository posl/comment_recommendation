Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    s = input()
    t = input()
    for i in range(len(s)):
        if s[i] != t[i]:
            print(i+1)
            break

=======
Suggestion 2

def main():
    S = input()
    T = input()
    for i in range(len(S)):
        if S[i] != T[i]:
            print(i+1)
            break

=======
Suggestion 3

def main():
    s = input()
    t = input()
    for i in range(len(s)):
        if s[i] != t[i]:
            print(i+1)
            break
    else:
        print(len(s)+1)

=======
Suggestion 4

def main():
    S = input()
    T = input()
    for i in range(len(S)):
        if S[i] != T[i]:
            print(i+1)
            break
    else:
        print(len(S)+1)

=======
Suggestion 5

def main():
    S = input()
    T = input()
    for i in range(len(S)):
        if S[i] != T[i]:
            print(i+1)
            break
    else:
        print(len(S)+1)

main()

=======
Suggestion 6

def main():
    S = input()
    T = input()
    for i in range(len(S)):
        if S[i] != T[i]:
            print(i+1)
            return 0
    print(len(S)+1)
    return 0

=======
Suggestion 7

def problem280_c():
    S = input()
    T = input()
    for i in range(len(S)):
        if S[i] != T[i]:
            print(i+1)
            return
    print(len(S)+1)
    return

problem280_c()

=======
Suggestion 8

def find_inserted_character_position(s, t):
    if len(s) == len(t):
        return -1
    else:
        for i in range(len(s)):
            if s[i] != t[i]:
                return i + 1
        return len(s) + 1
