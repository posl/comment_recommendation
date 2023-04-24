Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    s = input()
    t = "o" * (10 ** 5) + "x" * (10 ** 5) + "o" * (10 ** 5)
    if s in t:
        print("Yes")
    else:
        print("No")

=======
Suggestion 2

def main():
    S = input()
    T = "oxx" * 10**5
    if S in T:
        print("Yes")
    else:
        print("No")

=======
Suggestion 3

def main():
    S = input()
    T = "o" + "x" * 10 ** 5
    if S in T:
        print("Yes")
    else:
        print("No")

=======
Suggestion 4

def main():
    s = input()
    t = 'o' + 'x' * 10**5 + 'o' + 'x' * 10**5 + 'o'
    if s in t:
        print('Yes')
    else:
        print('No')

=======
Suggestion 5

def main():
    s = input()
    t = "o" + "x" * 10 ** 5 + "o" + "x" * 10 ** 5
    if s in t:
        print("Yes")
    else:
        print("No")

=======
Suggestion 6

def main():
    S = input()
    T = "o" + "x" * 10 ** 5 + "o"
    if S in T:
        print("Yes")
    else:
        print("No")

=======
Suggestion 7

def main():
    S = input()
    T = "o" + ("x" * 10**5) + "o" + ("x" * 10**5) + "o"
    if S in T:
        print("Yes")
    else:
        print("No")

=======
Suggestion 8

def main():
    s = input()
    t = "o" + "x" * 10**5
    for i in range(len(s)):
        if s[i] == t[i]:
            continue
        else:
            print("No")
            return
    print("Yes")
    return

=======
Suggestion 9

def main():
    S = input()
    T = "oxx" * 10**5
    T = T[:len(S)]
    if S == T:
        print("Yes")
    else:
        print("No")

=======
Suggestion 10

def is_part_of_string(S,T):
    if S in T:
        return True
    else:
        return False
