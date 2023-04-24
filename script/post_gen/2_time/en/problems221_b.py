Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    S = input()
    T = input()
    if S == T:
        print("Yes")
        return
    for i in range(len(S)-1):
        if S[:i] + S[i+1] + S[i] + S[i+2:] == T:
            print("Yes")
            return
    print("No")
    return

=======
Suggestion 2

def main():
    s = input()
    t = input()
    if s == t:
        print("Yes")
        return
    for i in range(len(s) - 1):
        if s[:i] + s[i + 1] + s[i] + s[i + 2:] == t:
            print("Yes")
            return
    print("No")

=======
Suggestion 3

def main():
    s = input()
    t = input()
    if s == t:
        print('Yes')
        return
    for i in range(len(s) - 1):
        if s[i] == t[i + 1] and s[i + 1] == t[i]:
            print('Yes')
            return
    print('No')
    return

=======
Suggestion 4

def main():
    S = input()
    T = input()
    if S == T:
        print('Yes')
        return
    for i in range(len(S) - 1):
        if S[i] == T[i + 1] and T[i] == S[i + 1]:
            print('Yes')
            return
    print('No')

=======
Suggestion 5

def main():
    S = input()
    T = input()
    if S == T:
        print('Yes')
    else:
        for i in range(len(S)-1):
            if S[i] == T[i+1] and S[i+1] == T[i]:
                print('Yes')
                break
            elif i == len(S)-2:
                print('No')

=======
Suggestion 6

def main():
    S = input()
    T = input()
    if S == T:
        print("Yes")
        return
    for i in range(len(S)-1):
        S2 = S[:i] + S[i+1] + S[i] + S[i+2:]
        if S2 == T:
            print("Yes")
            return
    print("No")

=======
Suggestion 7

def main():
    s = input()
    t = input()
    
    count = 0
    for i in range(len(s)):
        if s[i] != t[i]:
            count += 1
    
    if count == 0 or count == 2:
        print("Yes")
    else:
        print("No")

main()

=======
Suggestion 8

def main():
    s = input()
    t = input()
    
    if s == t:
        print("Yes")
        return
    
    for i in range(len(s) - 1):
        s = s[:i] + s[i+1] + s[i] + s[i+2:]
        if s == t:
            print("Yes")
            return
        s = s[:i] + s[i+1] + s[i] + s[i+2:]
        
    print("No")

=======
Suggestion 9

def main():
    # Read the input
    s = input()
    t = input()
    # Check if the strings are already equal
    if s == t:
        print("Yes")
        return
    # Check if it is possible to make s and t equal by swapping two adjacent characters
    for i in range(len(s) - 1):
        if s[:i] + s[i + 1] + s[i] + s[i + 2:] == t:
            print("Yes")
            return
    print("No")

=======
Suggestion 10

def is_equal(s, t):
    if s == t:
        return True
    else:
        return False
