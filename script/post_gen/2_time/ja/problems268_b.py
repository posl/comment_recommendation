Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    s = input()
    t = input()
    if s == t[:len(s)]:
        print("Yes")
    else:
        print("No")

=======
Suggestion 2

def main():
    s = input()
    t = input()
    if s == t[0:len(s)]:
        print("Yes")
    else:
        print("No")

=======
Suggestion 3

def main():
    s = input()
    t = input()
    if t[:len(s)] == s:
        print("Yes")
    else:
        print("No")

=======
Suggestion 4

def main():
    s = input()
    t = input()
    if t.startswith(s):
        print("Yes")
    else:
        print("No")

=======
Suggestion 5

def main():
    S = input()
    T = input()
    if S == T[0:len(S)]:
        print('Yes')
    else:
        print('No')

=======
Suggestion 6

def main():
    s = input()
    t = input()
    if t.startswith(s):
        print('Yes')
    else:
        print('No')

=======
Suggestion 7

def main():
    S = input()
    T = input()
    if T.startswith(S):
        print("Yes")
    else:
        print("No")

=======
Suggestion 8

def solve():
    S = input()
    T = input()
    if T[:len(S)] == S:
        print("Yes")
    else:
        print("No")

=======
Suggestion 9

def solve():
    # === 数値の入力 ===
    #n = int(input())
    #a, b = map(int, input().split())
    #m = [list(map(int,input().split())) for i in range(n)]
    #a = list(map(int,input().split()))
    s = input()
    t = input()
    # === 問題解答 ===
    if s == t[0:len(s)]:
        print("Yes")
    else:
        print("No")
    #for i in range(n):
    #    print(a[i])
    #print(" ".join(map(str, a)))
    #print("".join(map(str, a)))

=======
Suggestion 10

def main():
    s = input()
    t = input()
    if t.startswith(s):
        print('Yes')
    else:
        print('No')
main()
