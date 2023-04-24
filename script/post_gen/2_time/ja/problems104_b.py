Synthesizing 10/10 solutions (Duplicates hidden)

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
    if s[1:].lower() != s[1:]:
        print('WA')
        return
    if s[2:].lower() != s[2:]:
        print('WA')
        return
    print('AC')

=======
Suggestion 2

def main():
    s = input()
    if s[0] != "A":
        print("WA")
        return
    if s[2:-1].count("C") != 1:
        print("WA")
        return
    if s[1:].replace("C", "").islower():
        print("AC")
    else:
        print("WA")

=======
Suggestion 3

def main():
    S = input()
    if S[0] == 'A' and S[2:-1].count('C') == 1 and S[1:].replace('C', '').islower():
        print('AC')
    else:
        print('WA')

=======
Suggestion 4

def main():
    S = input()
    if S[0] == "A" and S[2:-1].count("C") == 1 and S[1:].replace("C", "").islower():
        print("AC")
    else:
        print("WA")

=======
Suggestion 5

def main():
    s = input()
    if s[0] == 'A' and s[2:-1].count('C') == 1 and s[1:].lower() == s[1:]:
        print('AC')
    else:
        print('WA')

=======
Suggestion 6

def main():
    S = input()
    if len(S) < 4 or len(S) > 10:
        print('WA')
        return

    if S[0] != 'A':
        print('WA')
        return

    if S[2:-1].count('C') != 1:
        print('WA')
        return

    S = S.replace('A', '')
    S = S.replace('C', '')
    if S.islower():
        print('AC')
    else:
        print('WA')

=======
Suggestion 7

def main():
    #入力
    s = input()
    #先頭の文字が'A'かどうか
    if s[0] != 'A':
        print('WA')
        return
    #3文字目と末尾から2文字目の間に'C'がちょうど1個含まれるかどうか
    if s[2:-1].count('C') != 1:
        print('WA')
        return
    #それ以外の文字はすべて小文字であるかどうか
    if s[1:].replace('C', '').islower() == False:
        print('WA')
        return
    print('AC')
    return
