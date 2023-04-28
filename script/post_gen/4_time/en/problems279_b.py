Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    s = input()
    t = input()
    if t in s:
        print("Yes")
    else:
        print("No")

=======
Suggestion 2

def main():
    S = input()
    T = input()
    if T in S:
        print("Yes")
    else:
        print("No")

=======
Suggestion 3

def main():
    s = input()
    t = input()
    if t in s:
        print('Yes')
    else:
        print('No')

=======
Suggestion 4

def main():
    S = input()
    T = input()
    if T in S:
        print('Yes')
    else:
        print('No')

=======
Suggestion 5

def check_contiguous_substring(s, t):
    if t in s:
        return 'Yes'
    else:
        return 'No'

=======
Suggestion 6

def is_substring(s, t):
    if len(t) > len(s):
        return False
    if s.find(t) >= 0:
        return True
    return False
