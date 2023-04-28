Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    s = input()
    if s[0] != 'A':
        print('WA')
        return
    if s[2:-1].count('C') != 1:
        print('WA')
        return
    for c in s:
        if c == 'A' or c == 'C':
            continue
        if c.isupper():
            print('WA')
            return
    print('AC')

=======
Suggestion 2

def main():
    s = input()
    if s[0] == "A":
        if s[2:-1].count("C") == 1:
            if s[1:].replace("C","").islower():
                print("AC")
                return
    print("WA")

=======
Suggestion 3

def main():
    s = input()
    if s[0] == 'A' and s[2:-1].count('C') == 1:
        for i in range(len(s)):
            if s[i] != 'A' and s[i] != 'C':
                if s[i].isupper():
                    print("WA")
                    exit()
        print("AC")
    else:
        print("WA")

=======
Suggestion 4

def main():
  s = input()
  if s[0] == 'A' and s[2:-1].count('C') == 1 and s[1:].replace('C', '').islower():
    print('AC')
  else:
    print('WA')

=======
Suggestion 5

def main():
    s = input()
    if s[0] == 'A' and s[2:-1].count('C') == 1:
        for i in range(1, len(s)):
            if s[i] == 'C':
                continue
            elif s[i].isupper():
                print('WA')
                return
        print('AC')
    else:
        print('WA')

=======
Suggestion 6

def main():
    s = input()
    if s[0] == "A" and s[2:-1].count("C") == 1:
        for c in s:
            if c == "A" or c == "C":
                continue
            elif c.isupper():
                print("WA")
                exit()
        print("AC")
    else:
        print("WA")

=======
Suggestion 7

def main():
    S = input()
    if S[0] == "A" and S[2:-1].count("C") == 1:
        for c in S:
            if c != "A" and c != "C":
                if c.isupper():
                    print("WA")
                    return
        print("AC")
    else:
        print("WA")

=======
Suggestion 8

def main():
    s = input()
    if s[0] == 'A' and s[2:-1].count('C') == 1 and s[1].islower() and s[-1].islower():
        for i in range(2, len(s)):
            if s[i] != 'C' and not s[i].islower():
                print('WA')
                return
        print('AC')
    else:
        print('WA')

=======
Suggestion 9

def solve(input_string):
    if input_string[0] != 'A':
        return 'WA'
    if input_string[2:-1].count('C') != 1:
        return 'WA'
    if input_string[1] == 'C' or input_string[-1] == 'C':
        return 'WA'
    if input_string[1].isupper() or input_string[-1].isupper():
        return 'WA'
    return 'AC'

=======
Suggestion 10

def main():
    s = input()
    if s[0] == 'A' and s[2:-1].count('C') == 1:
        for i in range(len(s)):
            if s[i].isupper():
                if i == 0 or i == 2 or i == len(s) - 1:
                    continue
                else:
                    print('WA')
                    return
        print('AC')
    else:
        print('WA')
