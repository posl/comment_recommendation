Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    s,t = input().split()
    if s < t:
        print('Yes')
    else:
        print('No')

=======
Suggestion 2

def judge(s,t):
    if len(s) < len(t):
        return "Yes"
    elif len(s) > len(t):
        return "No"
    else:
        for i in range(len(s)):
            if s[i] == t[i]:
                continue
            elif s[i] < t[i]:
                return "Yes"
            else:
                return "No"
        return "No"

=======
Suggestion 3

def main():
    s, t = input().split()
    if s < t:
        print('Yes')
    else:
        print('No')

main()

=======
Suggestion 4

def main():
    s,t = input().split()
    print('Yes' if s<t else 'No')

=======
Suggestion 5

def main():
    S,T = input().split()
    if S < T:
        print("Yes")
    else:
        print("No")

=======
Suggestion 6

def main():
    s,t = input().split()
    if s < t:
        print("Yes")
    else:
        print("No")

=======
Suggestion 7

def main():
    s,t = input().strip().split()
    if s<t:
        print('Yes')
    else:
        print('No')

=======
Suggestion 8

def main():
    s,t = input().split(" ")
    if s < t:
        print("Yes")
    else:
        print("No")
