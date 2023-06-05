Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def replace_nya(s):
    return s.replace('na', 'nya')

=======
Suggestion 2

def solve():
    N = int(input())
    S = input()
    print(S.replace('na', 'nya'))

=======
Suggestion 3

def replace_na(ori_str):
    new_str = ori_str.replace('na', 'nya')
    return new_str

=======
Suggestion 4

def replace_na(s):
    return s.replace('na', 'nya')

=======
Suggestion 5

def replace_na_with_nya(s):
    new_s = s.replace('na', 'nya')
    if new_s == s:
        return new_s
    else:
        return replace_na_with_nya(new_s)

=======
Suggestion 6

def main():
    n = int(input())
    s = input()
    print(s.replace("na", "nya"))

=======
Suggestion 7

def replace_str(s):
    s = list(s)
    for i in range(len(s)-1):
        if s[i] == 'n' and s[i+1] == 'a':
            s[i] = 'n'
            s[i+1] = 'y'
    return ''.join(s)

=======
Suggestion 8

def replace(s):
    if s.startswith('na'):
        return 'nya' + s[2:]
    else:
        return s

=======
Suggestion 9

def replace_na(s):
    #print(s)
    if 'na' in s:
        s = s.replace('na', 'nya')
        s = replace_na(s)
    return s
