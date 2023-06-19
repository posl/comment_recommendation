Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n = int(input())
    s = input()
    print(s.replace('na', 'nya'))

=======
Suggestion 2

def replace_na(s):
    s = s.replace('na','nya')
    return s

print(replace_na('naan'))
print(replace_na('near'))
print(replace_na('national'))

=======
Suggestion 3

def replace_na(s):
    i = 0
    while i < len(s) - 1:
        if s[i] == 'n' and s[i+1] == 'a':
            s = s[:i] + 'ny' + s[i+2:]
        i += 1
    return s

=======
Suggestion 4

def replace_na(s):
    return s.replace('na','nya')

=======
Suggestion 5

def main():
    n = int(input())
    s = input()
    print(s.replace("na", "nya"))

=======
Suggestion 6

def replace_na(s):
    if len(s) < 3:
        return s
    if s[0] == 'n' and s[1] == 'a':
        return 'nya' + replace_na(s[2:])
    else:
        return s[0] + replace_na(s[1:])

=======
Suggestion 7

def replace_na(s):
    if 'na' not in s:
        return s

    return replace_na(s.replace('na', 'nya', 1))

=======
Suggestion 8

def replace_na(s):
    if len(s) <= 1:
        return s
    elif len(s) == 2 and s == 'na':
        return 'nya'
    else:
        result = ''
        for i in range(len(s)):
            if s[i] == 'n' and i < len(s) - 1 and s[i + 1] == 'a':
                result += 'nya'
            else:
                result += s[i]
        return result
