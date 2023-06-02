Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    s = input()
    s = list(s)
    s.sort()
    print(''.join(s))

=======
Suggestion 2

def permute(s):
    if len(s) == 1:
        return s
    else:
        res = []
        for i in range(len(s)):
            for j in permute(s[:i]+s[i+1:]):
                res.append(s[i]+j)
        return res

=======
Suggestion 3

def minstr(s):
    s = sorted(s)
    return ''.join(s)

=======
Suggestion 4

def main():
    s = input()
    s = sorted(s)
    print(''.join(s))

=======
Suggestion 5

def main():
    s = input()
    print(''.join(sorted(s)))

=======
Suggestion 6

def solution():
    s = input()
    l = len(s)
    s = list(s)
    s.sort()
    if s[0] == s[-1]:
        print(s[0] * l)
        return
    if l == 2:
        print(s[0] + s[1])
        return
    if s[0] == s[1]:
        print(s[0] + s[2] * (l - 1))
        return
    else:
        print(s[0] + s[1] + s[2] * (l - 2))
        return

solution()

=======
Suggestion 7

def get_permutation(s):
    if len(s) == 1:
        return [s]
    else:
        result = []
        for i in range(len(s)):
            result.extend([s[i] + p for p in get_permutation(s[:i] + s[i+1:])])
        return result

s = input()
permutation_list = get_permutation(s)
print(min(permutation_list))

=======
Suggestion 8

def main():
    S = input()
    S_list = list(S)
    S_list.sort()
    print(''.join(S_list))
