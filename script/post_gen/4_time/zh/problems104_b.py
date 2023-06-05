Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    s = input()
    if s[0] == 'A' and s[2:-1].count('C') == 1:
        for i in range(len(s)):
            if s[i] != 'A' and s[i] != 'C':
                if s[i].isupper():
                    print('WA')
                    return
        print('AC')
    else:
        print('WA')
main()

=======
Suggestion 2

def main():
    S = input()
    if S[0] == 'A' and 'C' in S[2:-1] and S[1:].islower():
        print('AC')
    else:
        print('WA')

main()

=======
Suggestion 3

def main():
    s = input()
    if s[0] == 'A':
        if s[2:-1].count('C') == 1:
            if s[1] != 'C' and s[-1] != 'C':
                if s[1:].islower():
                    print('AC')
                    return
    print('WA')

=======
Suggestion 4

def main():
    input_string = input()
    #print(input_string)
    if input_string[0] == "A":
        if input_string[2:-1].count("C") == 1:
            if input_string[2:-1].islower():
                if input_string[-1].islower():
                    print("AC")
                    return
    print("WA")

=======
Suggestion 5

def main():
    s = input()
    if s[0] == "A" and s[2:-1].count("C") == 1 and s[1:].islower():
        print("AC")
    else:
        print("WA")

=======
Suggestion 6

def main():
    s = input()
    if s[0] != 'A':
        print("WA")
        return
    if s[1:].count('C') != 1:
        print("WA")
        return
    if s[1:].replace('C', '').islower():
        print("AC")
    else:
        print("WA")

=======
Suggestion 7

def is_capital_letter(letter):
    return ord(letter) >= ord('A') and ord(letter) <= ord('Z')

=======
Suggestion 8

def main():
    s = input()
    if s[0] == 'A' and s[2:-1].count('C') == 1:
        for i in range(1,len(s)):
            if s[i] == 'C':
                continue
            elif s[i].islower():
                continue
            else:
                print('WA')
                break
        else:
            print('AC')
    else:
        print('WA')

=======
Suggestion 9

def main():
    S = input()
    if S[0] != "A":
        print("WA")
        return
    if S[2:-1].count("C") != 1:
        print("WA")
        return
    for i in S[1:]:
        if i != "C" and i.isupper():
            print("WA")
            return
    print("AC")

=======
Suggestion 10

def main():
    input_str = input()
    if input_str[0] != "A":
        print("WA")
        return
    if input_str[2:-1].count("C") != 1:
        print("WA")
        return
    for i in range(len(input_str)):
        if i == 0 or i == 2 or i == len(input_str) - 1:
            continue
        if input_str[i].isupper():
            print("WA")
            return
    print("AC")
