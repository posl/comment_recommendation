Synthesizing 10/10 solutions

=======
Suggestion 1

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

=======
Suggestion 2

def main():
    n = int(input())
    s = []
    for i in range(n):
        s.append(input())
    for i in range(n):
        if s[i] in s[:i]:
            x = 0
            for j in range(i):
                if s[j] == s[i]:
                    x += 1
            print(s[i] + '(' + str(x) + ')')
        else:
            print(s[i])

=======
Suggestion 3

def main():
    n = int(input())
    files = {}
    for _ in range(n):
        s = input()
        if s in files:
            files[s] += 1
            print(s + '(' + str(files[s]) + ')')
        else:
            files[s] = 0
            print(s)

=======
Suggestion 4

def main():
    n = int(input())
    s = [input() for _ in range(n)]
    d = {}
    for i in range(n):
        if s[i] in d:
            d[s[i]] += 1
            s[i] = s[i] + '(' + str(d[s[i]]) + ')'
        else:
            d[s[i]] = 0
    for i in range(n):
        print(s[i])

=======
Suggestion 5

def main():
    n = int(input())
    file_list = []
    for i in range(n):
        file_list.append(input())
    file_dict = {}
    for i in range(n):
        if file_list[i] not in file_dict:
            file_dict[file_list[i]] = 1
            print(file_list[i])
        else:
            file_dict[file_list[i]] += 1
            print(file_list[i] + '(' + str(file_dict[file_list[i]] - 1) + ')')

=======
Suggestion 6

def main():
    n = int(input())
    s = [input() for _ in range(n)]
    d = {}
    for i in range(n):
        if s[i] not in d:
            d[s[i]] = 1
            print(s[i])
        else:
            d[s[i]] += 1
            print(s[i] + "(" + str(d[s[i]]-1) + ")")

=======
Suggestion 7

def main():
    n = int(input())
    file = []
    for i in range(n):
        file.append(input())
    for i in range(n):
        if file[i] not in file[:i]:
            print(file[i])
        else:
            for j in range(i):
                if file[j] == file[i]:
                    k = file[:i].count(file[i])
                    print(file[i] + "(" + str(k) + ")")
                    break

=======
Suggestion 8

def main():
    n = int(input())
    s = []
    for i in range(n):
        s.append(input())

    for i in range(n):
        if s[i] in s[:i]:
            j = 1
            while s[i]+ '(' + str(j) + ')' in s[:i]:
                j += 1
            s[i] += '(' + str(j) + ')'
    for i in range(n):
        print(s[i])

=======
Suggestion 9

def main():
    n = int(input())
    s = []
    for i in range(n):
        s.append(input())

    for i in range(n):
        if s[i] not in s[:i]:
            print(s[i])
        else:
            j = 1
            while True:
                if s[i] + '(' + str(j) + ')' not in s[:i]:
                    print(s[i] + '(' + str(j) + ')')
                    break
                else:
                    j += 1

=======
Suggestion 10

def main():
    n = int(input())
    s = [input() for i in range(n)]
    d = {}
    for i in range(n):
        if s[i] not in d:
            d[s[i]] = 1
            print(s[i])
        else:
            d[s[i]] += 1
            print(s[i] + "(" + str(d[s[i]] - 1) + ")")
