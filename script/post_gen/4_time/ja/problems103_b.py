Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    S = input()
    T = input()
    for i in range(len(S)):
        S = S[-1] + S[:-1]
        if S == T:
            print("Yes")
            exit()
    print("No")

=======
Suggestion 2

def main():
    s = input()
    t = input()
    if s == t:
        print("Yes")
    else:
        for i in range(len(s)):
            s = s[-1] + s[:-1]
            if s == t:
                print("Yes")
                break
        else:
            print("No")

=======
Suggestion 3

def main():
    s = input()
    t = input()
    if s == t:
        print("Yes")
        return
    for i in range(len(s)):
        s = s[-1] + s[:-1]
        if s == t:
            print("Yes")
            return
    print("No")

main()

=======
Suggestion 4

def main():
    S = input()
    T = input()
    if S == T:
        print('Yes')
        return
    for i in range(len(S)-1):
        S = S[-1] + S[:-1]
        if S == T:
            print('Yes')
            return
    print('No')
main()

=======
Suggestion 5

def main():
    S = input()
    T = input()
    if S == T:
        print("Yes")
    else:
        S = S[1:] + S[0]
        if S == T:
            print("Yes")
        else:
            print("No")

=======
Suggestion 6

def rotate(s, n):
    return s[n:] + s[:n]

s = input()
t = input()
for i in range(len(s)):
    if rotate(s, i) == t:
        print('Yes')
        exit()
print('No')

=======
Suggestion 7

def main():
    S = input()
    T = input()
    if S == T:
        print("Yes")
    else:
        print("No")

=======
Suggestion 8

def main():
    # input
    S = input()
    T = input()
    # compute
    result = "No"
    for i in range(len(S)):
        S = S[-1] + S[:-1]
        if S == T:
            result = "Yes"
            break
    # output
    print(result)

=======
Suggestion 9

def solve():
    # ===CODE===
    s = input()
    t = input()
    if t in s + s:
        print("Yes")
    else:
        print("No")

=======
Suggestion 10

def main():
    S = input()
    T = input()
    #print(S, T)
    if S == T:
        print("Yes")
        exit()
    for i in range(len(S)):
        if S[i:] + S[:i] == T:
            print("Yes")
            exit()
    print("No")
