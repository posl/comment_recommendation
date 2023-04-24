Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    s = input()
    for i in range(10):
        if str(i) not in s:
            print(i)
            return

=======
Suggestion 2

def main():
    s = input()
    for i in range(10):
        if str(i) not in s:
            print(i)
            break

=======
Suggestion 3

def main():
    S = input()
    for i in range(10):
        if str(i) not in S:
            print(i)
            return

=======
Suggestion 4

def main():
    S = input()
    for i in range(10):
        if str(i) not in S:
            print(i)
            break

=======
Suggestion 5

def main():
    s = input()
    for i in range(10):
        if s.find(str(i)) == -1:
            print(i)
            break

=======
Suggestion 6

def main():
    S = input()
    ans = 0
    for i in range(10):
        if str(i) not in S:
            ans = i
    print(ans)

=======
Suggestion 7

def main():
    S = input()
    for i in range(10):
        if i not in map(int, S):
            print(i)
            break
