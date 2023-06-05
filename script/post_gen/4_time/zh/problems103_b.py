Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
  s = input()
  t = input()
  if s == t:
    print("Yes")
  else:
    for i in range(len(s)):
      s = s[-1] + s[:-1]
      if s == t:
        print("Yes")
        break
      elif i == len(s) - 1:
        print("No")
        break

=======
Suggestion 2

def main():
    S = input()
    T = input()
    if len(S) != len(T):
        print("No")
    else:
        for i in range(len(S)):
            if S[i:] + S[:i] == T:
                print("Yes")
                break
        else:
            print("No")

=======
Suggestion 3

def main():
    s = input()
    t = input()
    if len(s) != len(t):
        print("No")
    else:
        for i in range(len(s)):
            if s == t:
                print("Yes")
                break
            else:
                s = s[1:] + s[0]
        else:
            print("No")

=======
Suggestion 4

def main():
    s = input()
    t = input()
    s = s + s
    if t in s:
        print("Yes")
    else:
        print("No")

=======
Suggestion 5

def main():
    s = input()
    t = input()
    if s == t:
        print('Yes')
    else:
        print('No')

=======
Suggestion 6

def main():
    s = input()
    t = input()
    if len(s) != len(t):
        print("No")
        return
    for i in range(len(s)):
        if s == t:
            print("Yes")
            return
        s = s[-1] + s[:-1]
    print("No")

=======
Suggestion 7

def main():
    s = input()
    t = input()
    if len(s) != len(t):
        print("No")
        return
    for i in range(0, len(s)):
        if s == t:
            print("Yes")
            return
        s = s[-1] + s[0:-1]
    print("No")

=======
Suggestion 8

def check(s,t):
    if s == t:
        return True
    else:
        return False

=======
Suggestion 9

def main():
    S = input()
    T = input()
    if len(S) != len(T):
        print("No")
    else:
        for i in range(len(S)):
            if S == T:
                print("Yes")
                break
            else:
                S = S[-1] + S[:-1]
        else:
            print("No")

=======
Suggestion 10

def main():
    s = input()
    t = input()
    if t in s+s:
        print("Yes")
    else:
        print("No")
