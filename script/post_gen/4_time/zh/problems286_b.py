Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def replace_na(s):
    return s.replace("na", "nya")

=======
Suggestion 2

def replace_na_by_nya(s):
    return s.replace('na', 'nya')

print(replace_na_by_nya(input()))

=======
Suggestion 3

def replace_na(s):
    return s.replace('na', 'nya')

=======
Suggestion 4

def replace_na(s):
    while 'na' in s:
        s = s.replace('na','nya')
    return s

=======
Suggestion 5

def replacestr(s):
    if "na" not in s:
        return s
    else:
        return replacestr(s.replace("na","nya",1))

=======
Suggestion 6

def replaceNa(s):
    s = s.replace('na', 'nya')
    return s

=======
Suggestion 7

def main():
    n = int(input())
    s = input()
    s = s.replace('na', 'nya')
    print(s)

=======
Suggestion 8

def main():
    N = int(input())
    S = input()
    S = S.replace("na", "nya")
    print(S)
