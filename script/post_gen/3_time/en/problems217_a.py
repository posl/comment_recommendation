Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    S, T = input().split()
    if S < T:
        print("Yes")
    else:
        print("No")

main()

=======
Suggestion 2

def main():
    S, T = input().split()
    if S < T:
        print("Yes")
    else:
        print("No")

=======
Suggestion 3

def main():
    s, t = input().split()
    if s < t:
        print("Yes")
    else:
        print("No")

=======
Suggestion 4

def main():
    S, T = input().split()
    if S < T:
        print('Yes')
    else:
        print('No')

=======
Suggestion 5

def main():
    s, t = input().split()
    if s < t:
        print('Yes')
    else:
        print('No')

=======
Suggestion 6

def compare(a,b):
    for i in range(len(a)):
        if a[i] == b[i]:
            continue
        else:
            return a[i] < b[i]
    return len(a) < len(b)

=======
Suggestion 7

def lexicographical_order(s,t):
    if s < t:
        return "Yes"
    else:
        return "No"
