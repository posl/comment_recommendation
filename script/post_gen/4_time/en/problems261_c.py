Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    d = {}
    for _ in range(n):
        s = input()
        if s not in d:
            d[s] = 0
        else:
            d[s] += 1
            s += '(' + str(d[s]) + ')'
        print(s)

=======
Suggestion 2

def main():
    n = int(input())
    s = []
    for i in range(n):
        s.append(input())
    d = {}
    for i in range(n):
        if s[i] in d:
            d[s[i]] += 1
            s[i] += '(' + str(d[s[i]]) + ')'
        else:
            d[s[i]] = 0
    for i in range(n):
        print(s[i])

=======
Suggestion 3

def main():
    n = int(input())
    s = []
    for i in range(n):
        s.append(input())
    for i in range(n):
        if s.count(s[i]) == 1:
            print(s[i])
        else:
            print(s[i]+'('+str(s[:i].count(s[i]))+')')

=======
Suggestion 4

def main():
    n = int(input())
    s = []
    for i in range(n):
        s.append(input())
    for i in range(n):
        if s.count(s[i]) == 1:
            print(s[i])
        else:
            print(s[i] + "(" + str(s[:i].count(s[i])) + ")")

=======
Suggestion 5

def main():
    N = int(input())
    S = []
    for i in range(N):
        S.append(input())

    for i in range(N):
        if S[i] not in S[:i]:
            print(S[i])
        else:
            cnt = S[:i].count(S[i]) + 1
            print(S[i] + '(' + str(cnt) + ')')

=======
Suggestion 6

def main():
  n = int(input())
  s = []
  d = {}
  for i in range(n):
    s.append(input())
  for i in range(n):
    if s[i] in d:
      d[s[i]] += 1
      print(s[i] + "(" + str(d[s[i]]) + ")")
    else:
      d[s[i]] = 0
      print(s[i])
main()

=======
Suggestion 7

def main():
    n = int(input())
    s = []
    for i in range(n):
        s.append(input())
    s2 = []
    for i in range(n):
        if s[i] not in s2:
            s2.append(s[i])
            print(s[i])
        else:
            count = 0
            for j in range(len(s2)):
                if s2[j] == s[i]:
                    count += 1
            print(s[i]+'('+str(count)+')')

=======
Suggestion 8

def problem261_c():
    n = int(input())
    s = []
    for i in range(n):
        s.append(input())
    s_dict = {}
    for i in range(n):
        if s[i] in s_dict:
            s_dict[s[i]] += 1
            s[i] = s[i] + "(" + str(s_dict[s[i]]) + ")"
        else:
            s_dict[s[i]] = 0
    for i in range(n):
        print(s[i])

=======
Suggestion 9

def main():
    n = int(input())
    s = []
    for i in range(n):
        s.append(input())
    s2 = []
    for i in range(n):
        if s[i] in s[0:i]:
            s2.append(s[i]+"("+str(s[0:i].count(s[i]))+")")
        else:
            s2.append(s[i])
    for i in range(n):
        print(s2[i])

=======
Suggestion 10

def main():
    n = int(input())
    s = [input() for _ in range(n)]
    r = []
    for i in range(n):
        c = 0
        for j in range(i):
            if s[j] == s[i]:
                c += 1
        if c == 0:
            r.append(s[i])
        else:
            r.append(s[i] + "(" + str(c) + ")")
    for i in range(n):
        print(r[i])
