Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    s = input()
    for i in range(len(s)):
        if s.count(s[i]) == 1:
            print(s[i])
            return
    print(-1)

=======
Suggestion 2

def main():
    s = input()
    for i in s:
        if s.count(i) == 1:
            print(i)
            return
    print(-1)

=======
Suggestion 3

def main():
    S = input()
    for s in S:
        if S.count(s) == 1:
            print(s)
            return
    print(-1)

=======
Suggestion 4

def main():
    S = input()
    ans = -1
    for i in S:
        if S.count(i) == 1:
            ans = i
            break
    print(ans)

=======
Suggestion 5

def main():
    S = input()
    for i in range(len(S)):
        if S.count(S[i]) == 1:
            print(S[i])
            return
    print(-1)

=======
Suggestion 6

def main():
    s = input()
    for i in range(0, len(s)):
        if s.count(s[i]) == 1:
            print(s[i])
            return
    print(-1)

=======
Suggestion 7

def main():
    s = input()
    s_set = set(s)
    for i in s_set:
        if s.count(i) == 1:
            print(i)
            exit()
    print(-1)

=======
Suggestion 8

def main():
    S = input()
    count = 0
    for i in range(len(S)):
        for j in range(len(S)):
            if i != j:
                if S[i] == S[j]:
                    count += 1

    if count == 0:
        print(S[0])
    elif count == 1:
        print(S[1])
    else:
        print(-1)

=======
Suggestion 9

def main():
    s = input()
    l = list(s)
    l2 = []
    for i in l:
        if i in l2:
            continue
        else:
            l2.append(i)
    if len(l) == len(l2):
        print("-1")
    else:
        for i in l2:
            if l.count(i) == 1:
                print(i)
                break
