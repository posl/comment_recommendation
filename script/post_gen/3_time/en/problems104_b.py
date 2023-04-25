Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    s = input()
    if s[0] == 'A' and s[2:-1].count('C') == 1 and s[1:].replace('C', '').islower():
        print('AC')
    else:
        print('WA')

=======
Suggestion 2

def main():
    S = input()
    if S[0] != "A":
        print("WA")
        return
    if S[2:-1].count("C") != 1:
        print("WA")
        return
    if S[1:].replace("C", "").islower() == False:
        print("WA")
        return
    print("AC")
    return

=======
Suggestion 3

def main():
    S = input()
    if S[0] != "A":
        print("WA")
        return
    if S[2:-1].count("C") != 1:
        print("WA")
        return
    if S[1:].lower() != S[1:]:
        print("WA")
        return
    if S[2:-1].replace("C", "").lower() != S[2:-1].replace("C", ""):
        print("WA")
        return
    print("AC")

=======
Suggestion 4

def main():
    s = input()
    print('AC' if s[0] == 'A' and s[2:-1].count('C') == 1 and s[1:].replace('C', '').islower() else 'WA')

=======
Suggestion 5

def main():
    S = input()
    if S[0] == "A" and S[2:-1].count("C") == 1 and S[1:].replace("C", "").islower():
        print("AC")
    else:
        print("WA")

=======
Suggestion 6

def main():
    s = input()
    if s[0] == "A":
        if s[2:-1].count("C") == 1:
            if s[1:].replace("C", "").islower():
                print("AC")
                return
    print("WA")
    return

=======
Suggestion 7

def main():
    s = input()
    if s[0] == 'A' and s[2:-1].count('C') == 1:
        s = s.replace('A', '').replace('C', '')
        if s.islower():
            print('AC')
            return
    print('WA')

=======
Suggestion 8

def main():
    S = input()
    if S[0] == 'A':
        if S[2:-1].count('C') == 1:
            if S[1:].replace('C','').islower():
                print('AC')
            else:
                print('WA')
        else:
            print('WA')
    else:
        print('WA')

=======
Suggestion 9

def main():
    # input
    S = input()

    # compute
    if S[0] != 'A':
        print('WA')
        return
    if S[2:-1].count('C') != 1:
        print('WA')
        return
    if S[1:].replace('C', '').islower():
        print('AC')
    else:
        print('WA')
