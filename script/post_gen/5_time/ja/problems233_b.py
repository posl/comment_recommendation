Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def reverseString(s, start, end):
    if start < 0 or end >= len(s):
        return -1

    for i in range((end - start + 1) // 2):
        s[start + i], s[end - i] = s[end - i], s[start + i]

    return s

=======
Suggestion 2

def main():
    l, r = map(int, input().split())
    s = input()
    s = list(s)
    s[l-1:r] = s[l-1:r][::-1]
    print("".join(s))

=======
Suggestion 3

def main():
    L, R = map(int, input().split())
    S = input()
    print(S[:L-1] + S[L-1:R][::-1] + S[R:])

=======
Suggestion 4

def main():
    l, r = map(int, input().split())
    s = input()
    print(s[:l-1] + s[l-1:r][::-1] + s[r:])

=======
Suggestion 5

def reverseString(s, l, r):
    s = list(s)
    for i in range(r - l + 1):
        s[l + i - 1] = s[r - i - 1]
    return "".join(s)

=======
Suggestion 6

def reverse_s(s):
    return s[::-1]

=======
Suggestion 7

def reverse_string(s, start, end):
    return s[:start-1] + s[start-1:end][::-1] + s[end:]

=======
Suggestion 8

def reverse_string(s, l, r):
    l -= 1
    r -= 1
    return s[:l] + s[l:r+1][::-1] + s[r+1:]

l, r = map(int, input().split())
s = input()
print(reverse_string(s, l, r))
