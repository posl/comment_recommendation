Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n = int(input())
    s = input()
    print(s.replace('na', 'nya'))

=======
Suggestion 2

def main():
    n = int(input())
    s = input()
    print(s.replace("na", "nya"))

=======
Suggestion 3

def main():
    N = int(input())
    S = input()
    print(S.replace('na', 'nya'))

=======
Suggestion 4

def replace_str(s):
    s = s.replace("na", "nya")
    return s

n = int(input())
s = input()

print(replace_str(s))

=======
Suggestion 5

def replace_na(n, s):
    if n < 2:
        return s
    else:
        return replace_na(n-1, s.replace('na'*n, 'nya'*n))

n = int(input())
s = input()

print(replace_na(n, s))
