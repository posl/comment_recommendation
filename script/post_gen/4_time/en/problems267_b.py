Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    s = input()
    if s[0] == '0':
        if s[1] == '1':
            if s[2] == '0':
                if s[3] == '1':
                    if s[4] == '0':
                        if s[5] == '1':
                            if s[6] == '0':
                                if s[7] == '1':
                                    if s[8] == '0':
                                        if s[9] == '1':
                                            print("Yes")
                                            return
    print("No")

=======
Suggestion 2

def main():
    s = input()
    if s[0] == '0':
        print('No')
    elif s[1] == '0' and s[2] == '0':
        print('No')
    elif s[3] == '0' and s[4] == '0':
        print('No')
    elif s[5] == '0' and s[6] == '0':
        print('No')
    elif s[7] == '0' and s[8] == '0':
        print('No')
    elif s[9] == '0':
        print('No')
    else:
        print('Yes')

=======
Suggestion 3

def main():
    s = input()
    if s[0] == '0' and s[3] == '0' and s[5] == '0' and s[7] == '0' and s[9] == '0':
        print("Yes")
    else:
        print("No")

=======
Suggestion 4

def main():
    pins = input()
    if pins[0] == '0':
        if pins[1] == '0' or pins[5] == '0':
            print('No')
        else:
            print('Yes')
    elif pins[9] == '0':
        if pins[8] == '0' or pins[4] == '0':
            print('No')
        else:
            print('Yes')
    elif pins[1] == '0':
        if pins[2] == '0' or pins[6] == '0':
            print('No')
        else:
            print('Yes')
    elif pins[8] == '0':
        if pins[7] == '0' or pins[3] == '0':
            print('No')
        else:
            print('Yes')
    else:
        print('No')

=======
Suggestion 5

def check_split(pins):
    if pins[0] == '0':
        if pins[1] == '1' and pins[2] == '1' and pins[3] == '1':
            return True
        elif pins[2] == '1' and pins[3] == '1' and pins[4] == '1':
            return True
        elif pins[3] == '1' and pins[4] == '1' and pins[5] == '1':
            return True
        elif pins[4] == '1' and pins[5] == '1' and pins[6] == '1':
            return True
        elif pins[5] == '1' and pins[6] == '1' and pins[7] == '1':
            return True
        elif pins[6] == '1' and pins[7] == '1' and pins[8] == '1':
            return True
        elif pins[7] == '1' and pins[8] == '1' and pins[9] == '1':
            return True
        else:
            return False
    else:
        return False

=======
Suggestion 6

def main():
    S = input()
    if S[0] == '0':
        print('No')
    else:
        if S[1] == '1' and S[2] == '1':
            print('No')
        elif S[3] == '1' and S[4] == '1':
            print('No')
        elif S[5] == '1' and S[6] == '1':
            print('No')
        elif S[7] == '1' and S[8] == '1':
            print('No')
        elif S[9] == '1' and S[0] == '1':
            print('No')
        else:
            print('Yes')

=======
Suggestion 7

def main():
    s = input()
    if s[0] == '0':
        print('No')
    else:
        if s[1] == '0' or s[2] == '0':
            print('No')
        else:
            if s[3] == '0' or s[4] == '0' or s[5] == '0':
                print('No')
            else:
                if s[6] == '0' or s[7] == '0' or s[8] == '0' or s[9] == '0':
                    print('No')
                else:
                    print('Yes')

=======
Suggestion 8

def main():
    S = input()
    if S[0] == '0':
        if S[1] == '0':
            print('No')
        else:
            if S[4] == '0' or S[5] == '0':
                print('Yes')
            else:
                print('No')
    else:
        if S[4] == '0':
            if S[5] == '0':
                print('No')
            else:
                print('Yes')
        else:
            if S[1] == '0' or S[2] == '0':
                print('Yes')
            else:
                print('No')

=======
Suggestion 9

def is_split(pins):
    if pins[0] == '0':
        return False
    else:
        left = False
        right = False
        for i in range(1, 5):
            if pins[i] == '1':
                left = True
        for i in range(6, 10):
            if pins[i] == '1':
                right = True
        return left and right

=======
Suggestion 10

def solve():
    print("Yes" if input()[0] == "0" and input().count("1") >= 2 else "No")

solve()
