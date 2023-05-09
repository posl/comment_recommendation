Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    s = input()
    count = 0
    for i in range(len(s)-1):
        if s[i] == 'v' and s[i+1] == 'w':
            count += 1
    print(2**count)

=======
Suggestion 2

def main():
    s = input()
    s = s.replace("vv", "v v")
    s = s.replace("ww", "w w")
    s = s.replace("vw", "v w")
    s = s.replace("wv", "w v")
    print(s.count("v") + s.count("w"))

=======
Suggestion 3

def main():
    S = input()
    S = S.replace('ww','w w')
    S = S.replace('vv','v v')
    S = S.replace('wv','w v')
    S = S.replace('vw','v w')
    S = S.replace('vv','v v')
    S = S.replace('ww','w w')
    S = S.replace('wv','w v')
    S = S.replace('vw','v w')
    S = S.replace('vv','v v')
    S = S.replace('ww','w w')
    S = S.replace('wv','w v')
    S = S.replace('vw','v w')
    S = S.replace('vv','v v')
    S = S.replace('ww','w w')
    S = S.replace('wv','w v')
    S = S.replace('vw','v w')
    S = S.replace('vv','v v')
    S = S.replace('ww','w w')
    S = S.replace('wv','w v')
    S = S.replace('vw','v w')
    S = S.replace('vv','v v')
    S = S.replace('ww','w w')
    S = S.replace('wv','w v')
    S = S.replace('vw','v w')
    S = S.replace('vv','v v')
    S = S.replace('ww','w w')
    S = S.replace('wv','w v')
    S = S.replace('vw','v w')
    S = S.replace('vv','v v')
    S = S.replace('ww','w w')
    S = S.replace('wv','w v')
    S = S.replace('vw','v w')
    S = S.replace('vv','v v')
    print(len(S))

=======
Suggestion 4

def main():
    s = input().strip()
    count = 0
    for i in range(len(s)):
        if s[i] == 'w':
            count += i
    print(count)

=======
Suggestion 5

def main():
    S = input()
    print(S.count('vw') + S.count('wv'))

=======
Suggestion 6

def main():
    S = input()
    print(S.count("vw") + S.count("wv"))

=======
Suggestion 7

def main():
    s = input()
    print(s.count('vv'))

=======
Suggestion 8

def main():
    s = input()
    print(s.count('wv'))

=======
Suggestion 9

def main():
    S = input()
    S = S.replace('vw','x')
    print(S.count('v')+S.count('w'))

=======
Suggestion 10

def problem():
    s = input()
    print(s.count('vv'))
