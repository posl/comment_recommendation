Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    S = input()
    for i in range(len(S)):
        if (i+1)%2==1 and S[i] not in ('R','U','D'):
            print('No')
            return
        elif (i+1)%2==0 and S[i] not in ('L','U','D'):
            print('No')
            return
    print('Yes')

=======
Suggestion 2

def main():
    # S = input()
    S = "rdululdururlrdulrlr"
    S_odd = S[::2]
    S_even = S[1::2]
    # print(S_odd)
    # print(S_even)
    if S_odd.count("R") == 0 and S_odd.count("L") == 0 and S_even.count("U") == 0 and S_even.count("D") == 0:
        print("Yes")
    else:
        print("No")

=======
Suggestion 3

def main():
    s = input()
    for i in range(len(s)):
        if i % 2 == 0:
            if s[i] == 'L':
                print('No')
                return
        else:
            if s[i] == 'R':
                print('No')
                return
    print('Yes')

=======
Suggestion 4

def main():
    s = input()
    if len(s) == 1:
        if s == 'L' or s == 'U' or s == 'D':
            print('No')
        else:
            print('Yes')
    else:
        for i in range(len(s)):
            if i % 2 == 0:
                if s[i] == 'L':
                    print('No')
                    break
            else:
                if s[i] == 'R':
                    print('No')
                    break
        else:
            print('Yes')

=======
Suggestion 5

def main():
    # S = "RUDLUDR"
    # S = "DULL"
    # S = "uuuuuuuuuuuuu"
    # S = "ULURU"
    # S = "rdululdururlrdulrlr"
    S = input()
    result = "Yes"
    for i in range(len(S)):
        if i % 2 == 0:
            if S[i] == "L":
                result = "No"
                break
        else:
            if S[i] == "R":
                result = "No"
                break
    print(result)

=======
Suggestion 6

def main():
    s = input()
    for i in range(len(s)):
        if i % 2 == 0:
            if s[i] == "L":
                print("No")
                return
        else:
            if s[i] == "R":
                print("No")
                return
    print("Yes")

=======
Suggestion 7

def main():
    S = input()
    odd = S[::2]
    even = S[1::2]
    if 'L' in odd or 'R' in even:
        print('No')
    else:
        print('Yes')

=======
Suggestion 8

def check(s):
    for i in range(len(s)):
        if i % 2 == 0 and s[i] == 'L':
            return False
        elif i % 2 == 1 and s[i] == 'R':
            return False
    return True

s = input()

=======
Suggestion 9

def main():
    s = input()
    if len(s) == 1:
        print("Yes")
        return
    for i in range(0, len(s)):
        if i % 2 == 0:
            if s[i] == "L":
                print("No")
                return
        else:
            if s[i] == "R":
                print("No")
                return
    print("Yes")

=======
Suggestion 10

def main():
    S = input()
    i = 1
    for s in S:
        if i % 2 == 0:
            if s == 'L':
                pass
            elif s == 'U':
                pass
            elif s == 'D':
                pass
            else:
                print('No')
                exit()
        else:
            if s == 'R':
                pass
            elif s == 'U':
                pass
            elif s == 'D':
                pass
            else:
                print('No')
                exit()
        i += 1
    print('Yes')
