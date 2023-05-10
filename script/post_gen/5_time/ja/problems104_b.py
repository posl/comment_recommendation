Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    s = input()
    if s[0] == "A":
        if s[2:-1].count("C") == 1:
            if s[1:].replace("C","").islower():
                print("AC")
                exit()
    print("WA")
main()

=======
Suggestion 2

def main():
    s = input()
    if s[0] == 'A' and s[2:-1].count('C') == 1 and s[1:].replace('C', '').islower() == True:
        print('AC')
    else:
        print('WA')

main()

=======
Suggestion 3

def main():
    s = input()
    if s[0] == "A":
        if s[2:-1].count("C") == 1:
            if s.replace("A", "").replace("C", "").islower():
                print("AC")
                return
    print("WA")

=======
Suggestion 4

def main():
    s = input()
    if s[0] == "A":
        if s[2:-1].count("C") == 1:
            if s[1:].replace("C","").islower():
                print("AC")
                return
    print("WA")

=======
Suggestion 5

def is_ac(s):
    if s[0] != "A":
        return False
    if s[1:].count("C") != 1:
        return False
    for i in range(2, len(s)-1):
        if s[i] == "C":
            return False
    for i in range(len(s)):
        if s[i] == "A" or s[i] == "C":
            continue
        if s[i].isupper():
            return False
    return True

s = input()

=======
Suggestion 6

def main():
    s = input()
    if s[0] == 'A' and s[2:-1].count('C') == 1:
        s = s.replace('A','')
        s = s.replace('C','')
        if s.islower():
            print('AC')
            return
    print('WA')

=======
Suggestion 7

def main():
    s = input()
    if s[0] == 'A' and s[2:-1].count('C') == 1 and s[1:].replace('C', '').islower():
        print('AC')
    else:
        print('WA')

=======
Suggestion 8

def main():
    s = input()
    if s[0] == 'A':
        if s[2:-1].count('C') == 1:
            if s[1:].replace('C', '').islower():
                print('AC')
                return
    print('WA')

=======
Suggestion 9

def main():
    s = input()
    if s[0] == 'A' and s[2:-1].count('C') == 1:
        s = s.replace('A', '').replace('C', '')
        if s.islower():
            print('AC')
            return
    print('WA')
