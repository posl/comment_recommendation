Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    S = []
    for i in range(n):
        S.append(input())
    for i in range(n):
        if S[i] in S[:i]:
            j = S[:i].count(S[i])
            print(S[i] + '(' + str(j + 1) + ')')
        else:
            print(S[i])

=======
Suggestion 2

def main():
    n = int(input())
    filenames = []
    for i in range(n):
        filenames.append(input())
    filenames_set = set()
    for i in range(n):
        if filenames[i] not in filenames_set:
            print(filenames[i])
            filenames_set.add(filenames[i])
        else:
            num = 1
            while True:
                if filenames[i] + '(' + str(num) + ')' not in filenames_set:
                    print(filenames[i] + '(' + str(num) + ')')
                    filenames_set.add(filenames[i] + '(' + str(num) + ')')
                    break
                else:
                    num += 1

=======
Suggestion 3

def main():
    n = int(input())
    file_list = []
    for i in range(n):
        file_list.append(input())
    for i in range(n):
        count = 0
        for j in range(i):
            if file_list[i] == file_list[j]:
                count += 1
        if count == 0:
            print(file_list[i])
        else:
            print(file_list[i] + '(' + str(count) + ')')

=======
Suggestion 4

def main():
    n = int(input())
    s = []
    for i in range(n):
        s.append(input())
    d = {}
    for i in range(n):
        if s[i] in d:
            d[s[i]] += 1
            print(s[i] + "(" + str(d[s[i]] - 1) + ")")
        else:
            d[s[i]] = 1
            print(s[i])

=======
Suggestion 5

def modify_name(s, d):
    if s in d:
        d[s] += 1
        return s + "(" + str(d[s]) + ")"
    else:
        d[s] = 0
        return s

n = int(input())
d = {}
for i in range(n):
    s = input()
    print(modify_name(s, d))

=======
Suggestion 6

def main():
    n = int(input())
    s = []
    for i in range(n):
        s.append(input())
    for i in range(n):
        if s[i] not in s[:i]:
            print(s[i])
        else:
            count = 1
            while s[i] + "(" + str(count) + ")" in s[:i]:
                count += 1
            print(s[i] + "(" + str(count) + ")")

=======
Suggestion 7

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
Suggestion 8

def main():
    n = int(input())
    file_name = {}
    for i in range(n):
        s = input()
        if s in file_name:
            file_name[s] += 1
            print(s+'('+str(file_name[s])+')')
        else:
            file_name[s] = 0
            print(s)

=======
Suggestion 9

def main():
    n = int(input())
    s = []
    for i in range(n):
        s.append(input())
    for i in range(n):
        count = 0
        for j in range(i):
            if s[i] == s[j]:
                count += 1
        if count == 0:
            print(s[i])
        else:
            print(s[i] + '(' + str(count) + ')')
    return 0

=======
Suggestion 10

def main():
    n = int(input())
    s = [input() for _ in range(n)]
    dict = {}
    for i in range(n):
        if s[i] in dict:
            dict[s[i]] += 1
            print(s[i] + '(' + str(dict[s[i]] - 1) + ')')
        else:
            dict[s[i]] = 1
            print(s[i])
