Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    S = input()
    T = input()
    if S == T:
        print("Yes")
    else:
        for i in range(len(S)-1):
            S = S[-1] + S[:-1]
            if S == T:
                print("Yes")
                break
        else:
            print("No")

=======
Suggestion 2

def main():
    S = input()
    T = input()

    for i in range(len(S)):
        S = S[-1] + S[:-1]
        if S == T:
            print('Yes')
            break
    else:
        print('No')

=======
Suggestion 3

def main():
    s = input()
    t = input()
    if s == t:
        print("Yes")
        return
    for i in range(len(s)):
        s = s[-1] + s[:-1]
        if s == t:
            print("Yes")
            return
    print("No")

=======
Suggestion 4

def main():
    s = input()
    t = input()
    if s == t:
        print('Yes')
        return
    for i in range(len(s)-1):
        s = s[-1] + s[:-1]
        if s == t:
            print('Yes')
            return
    print('No')
    return

=======
Suggestion 5

def main():
    S = input()
    T = input()
    if S == T:
        print("Yes")
    else:
        for i in range(len(S)):
            S = S[-1] + S[:-1]
            if S == T:
                print("Yes")
                return
        print("No")

=======
Suggestion 6

def main():
    s = input()
    t = input()

    if s == t:
        print('Yes')
        return

    for i in range(len(s)-1):
        s = s[-1] + s[:-1]
        if s == t:
            print('Yes')
            return

    print('No')

=======
Suggestion 7

def main():
  S = input()
  T = input()
  for i in range(len(S)):
    S = S[1:] + S[0]
    if S == T:
      print("Yes")
      return
  print("No")

=======
Suggestion 8

def main():
    s = input()
    t = input()
    if s == t:
        print("Yes")
    else:
        for i in range(1, len(s)):
            s = s[-1] + s[:-1]
            if s == t:
                print("Yes")
                break
        else:
            print("No")

=======
Suggestion 9

def main():
    S = input()
    T = input()
    if S == T:
        print("Yes")
        return
    for i in range(1, len(S)):
        if T == S[i:] + S[:i]:
            print("Yes")
            return
    print("No")
