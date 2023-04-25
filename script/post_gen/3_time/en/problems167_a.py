Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    s = input()
    t = input()
    if s == t[:-1]:
        print("Yes")
    else:
        print("No")

=======
Suggestion 2

def main():
    S = input()
    T = input()
    if S == T[:-1]:
        print("Yes")
    else:
        print("No")

=======
Suggestion 3

def main():
    s = input()
    t = input()
    if t[:-1] == s:
        print("Yes")
    else:
        print("No")

=======
Suggestion 4

def main():
    s = input()
    t = input()
    if t[0:len(s)] == s:
        print("Yes")
    else:
        print("No")

=======
Suggestion 5

def main():
    s = input()
    t = input()
    if t[0:len(s)] == s:
        print('Yes')
    else:
        print('No')

=======
Suggestion 6

def main():
    S = input()
    T = input()
    print("Yes" if S == T[:-1] else "No")

=======
Suggestion 7

def main():
    s = input()
    t = input()
    if s == t[:-1]:
        print("Yes")
    else:
        print("No")

main()

I have a problem with the code above. It is not passing the test case 3. I have tried to debug it but I can’t find any problem with it. Can you help me with it?
