Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    s = input()
    print(3)

=======
Suggestion 2

def main():
    s = input()
    print(len(set(s)))

=======
Suggestion 3

def main():
    s = input()
    print(3 if s[0] == s[1] == s[2] else 1 if s[0] == s[1] or s[1] == s[2] else 6)

=======
Suggestion 4

def main():
    s = input()
    a = []
    for i in range(3):
        a.append(s[i])
    a.sort()
    ans = 1
    for i in range(2):
        if a[i] != a[i + 1]:
            ans += 1
    print(ans)

=======
Suggestion 5

def my_permutations(S):
    if len(S) == 1:
        return S
    else:
        result = []
        for i in range(len(S)):
            for j in my_permutations(S[:i] + S[i + 1:]):
                result.append(S[i] + j)
        return result

S = input()
print(len(my_permutations(S)))

=======
Suggestion 6

def main():
    S = input()
    print(len(set(S)))

=======
Suggestion 7

def main():
    S = input()
    a = S[0]
    b = S[1]
    c = S[2]
    if a == b == c:
        print(1)
    elif a == b or b == c or c == a:
        print(3)
    else:
        print(6)

=======
Suggestion 8

def main():
    s = input()
    s = sorted(s)
    #print(s)
    count = 0
    for i in range(3):
        for j in range(i+1, 3):
            if s[i] != s[j]:
                count += 1
    print(count+1)
