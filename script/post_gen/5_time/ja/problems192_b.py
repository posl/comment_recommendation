Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def is_hard_to_read(s):
    if s[0::2].isupper() and s[1::2].islower():
        return True
    else:
        return False

=======
Suggestion 2

def main():
    s = input()
    for i in range(len(s)):
        if i%2 == 0:
            if s[i].isupper():
                print("No")
                return
        else:
            if s[i].islower():
                print("No")
                return
    print("Yes")
    return

=======
Suggestion 3

def main():
    s = input()
    odd = s[::2]
    even = s[1::2]
    if odd.islower() and even.isupper():
        print('Yes')
    else:
        print('No')

=======
Suggestion 4

def check(s):
    for i in range(len(s)):
        if i % 2 == 0:
            if s[i].islower():
                continue
            else:
                return False
        else:
            if s[i].isupper():
                continue
            else:
                return False
    return True

=======
Suggestion 5

def solve():
    s = input()
    odd = ''
    even = ''
    for i in range(len(s)):
        if i % 2 == 0:
            odd += s[i]
        else:
            even += s[i]
    if odd.islower() and even.isupper():
        print('Yes')
    else:
        print('No')
solve()

=======
Suggestion 6

def main():
    s = input()
    if s[0::2].islower() and s[1::2].isupper():
        print('Yes')
    else:
        print('No')

=======
Suggestion 7

def judge(s):
    for i in range(len(s)):
        if i % 2 == 0:
            if s[i].islower() == False:
                return False
        else:
            if s[i].isupper() == False:
                return False
    return True

s = input()

=======
Suggestion 8

def main():
    s = input()
    if s[0::2].islower() and s[1::2].isupper():
        print("Yes")
    else:
        print("No")

=======
Suggestion 9

def main():
    s = input()
    ans = 'Yes'
    for i in range(len(s)):
        if i % 2 == 0:
            if s[i].islower() == False:
                ans = 'No'
                break
        else:
            if s[i].isupper() == False:
                ans = 'No'
                break
    print(ans)
