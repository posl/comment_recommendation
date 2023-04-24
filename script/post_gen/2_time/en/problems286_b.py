Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def replace_na(s):
    if len(s) < 2:
        return s
    elif s[0:2] == 'na':
        return 'nya' + replace_na(s[2:])
    else:
        return s[0] + replace_na(s[1:])

=======
Suggestion 2

def main():
    n = int(input())
    s = input()
    s = s.replace("na", "nya")
    print(s)

main()

=======
Suggestion 3

def main():
    n = int(input())
    s = input()
    s = s.replace('na', 'nya')
    print(s)

main()

=======
Suggestion 4

def main():
    n = int(input())
    s = input()
    s = s.replace("na", "nya")
    print(s)

=======
Suggestion 5

def main():
    N = int(input())
    S = input()
    print(S.replace('na', 'nya'))

=======
Suggestion 6

def main():
    N = int(input())
    S = input()

    # Replace all contiguous occurrences of na in S with nya.
    S = S.replace("na", "nya")

    print(S)

main()

=======
Suggestion 7

def main():
    # put your code here
    n = int(input())
    s = input()
    print(s.replace("na","nya"))

=======
Suggestion 8

def replace_na(s):
    return s.replace('na', 'nya')
