Synthesizing 10/10 solutions (Duplicates hidden)

=======

def main():
    s = input()
    if s[0] != 'A':
        print('WA')
        return
    if s[2:-1].count('C') != 1:
        print('WA')
        return
    if s[1:].replace('C', '').islower() == False:
        print('WA')
        return
    print('AC')

=======

def main():
    s = input()
    if s[0] != 'A':
        print('WA')
        return
    if s[2:-1].count('C') != 1:
        print('WA')
        return
    if s[1:].replace('C', '').islower():
        print('AC')
        return
    print('WA')

=======

def main():
    S = input()
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

=======

def main():
    S = input()
    if S[0] == 'A' and S[2:-1].count('C') == 1 and S[1:].replace('C', '').islower():
        print('AC')
    else:
        print('WA')

=======

def main():
    S = input()
    if S[0] == 'A' and S[2:-1].count('C') == 1:
        S = S.replace('A', '')
        S = S.replace('C', '')
        if S.islower():
            print('AC')
            return
    print('WA')

=======

def main():
    # 文字列 S が与えられます。
    s = input()
    # S の先頭の文字は大文字の A である。
    if s[0] != 'A':
        print('WA')
        return
    # S の先頭から 3 文字目と末尾から 2 文字目の間（両端含む）に大文字の C がちょうど 1 個含まれる。
    if s[2:-1].count('C') != 1:
        print('WA')
        return
    # 以上の A, C を除く S のすべての文字は小文字である。
    s = s.replace('A', '').replace('C', '')
    if s.islower() == False:
        print('WA')
        return
    print('AC')

=======

def readinput():
    s=input()
    return s
