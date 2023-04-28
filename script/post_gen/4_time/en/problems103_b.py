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
        S = S[-1] + S[:-1]
        if S == T:
            print("Yes")
            return
    print("No")
    return

=======
Suggestion 2

def main():
    S = input()
    T = input()
    if S == T:
        print("Yes")
        return
    for i in range(len(S)-1):
        S = S[-1] + S[:-1]
        if S == T:
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
        s = s[-1] + s[:-1]
        if s == t:
            print('Yes')
            return
    print('No')

=======
Suggestion 4

def main():
    S = input()
    T = input()
    if S == T:
        print("Yes")
    else:
        for i in range(len(S) - 1):
            S = S[-1] + S[:-1]
            if S == T:
                print("Yes")
                break
        else:
            print("No")

main()

=======
Suggestion 5

def main():
    s = input()
    t = input()
    if s == t:
        print("Yes")
    else:
        for i in range(len(s) - 1):
            s = s[-1] + s[:-1]
            if s == t:
                print("Yes")
                return
        print("No")

main()

=======
Suggestion 6

def main():
    s = input()
    t = input()
    if s == t:
        print('Yes')
    else:
        for i in range(len(s) - 1):
            s = s[-1] + s[:-1]
            if s == t:
                print('Yes')
                break
        else:
            print('No')

main()

This is my code. I have tried 2 test cases and it worked. But when I tried to submit, it shows WA. Can anyone help me out?

I think you should use the else clause of your for loop to print No, rather than using a for-else construct. The for-else construct will only run if the for loop is not broken out of, but you break out of the loop if you find a match. So, the else clause will never run.

Thanks for the reply. I tried that but it still shows WA. I am not sure what is wrong with my code. Can you please check my code and tell me if there is any error?

I think I see the problem. You are checking if s == t, but you need to check if s == t after each rotation. Try this:

=======
Suggestion 7

def main():
    S = input()
    T = input()
    if S == T:
        print('Yes')
    else:
        for i in range(len(S) - 1):
            S = S[-1] + S[:-1]
            if S == T:
                print('Yes')
                return
        print('No')

=======
Suggestion 8

def main():
    S = input()
    T = input()
    if S == T:
        print('Yes')
    else:
        for i in range(len(S)):
            S = S[-1] + S[:-1]
            if S == T:
                print('Yes')
                return
        print('No')

=======
Suggestion 9

def main():
    S = input()
    T = input()
    if S == T:
        print("Yes")
        return
    for i in range(len(S)-1):
        S = S[-1] + S[0:-1]
        if S == T:
            print("Yes")
            return
    print("No")

=======
Suggestion 10

def main():
    s = input()
    t = input()
    if s == t:
        print("Yes")
    else:
        for i in range(1,len(s)):
            if s[i:] + s[:i] == t:
                print("Yes")
                return
        print("No")
