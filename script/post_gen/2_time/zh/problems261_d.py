Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    s = []
    for i in range(n):
        s.append(input())
    d = {}
    for i in range(n):
        if s[i] in d:
            d[s[i]] += 1
            print(s[i] + '(' + str(d[s[i]]) + ')')
        else:
            d[s[i]] = 0
            print(s[i])

=======
Suggestion 2

def main():
    n = int(input())
    files = []
    for i in range(n):
        files.append(input())
    for i in range(n):
        if files.count(files[i]) == 1:
            print(files[i])
        else:
            print(files[i] + "(" + str(files[0:i].count(files[i])) + ")")

=======
Suggestion 3

def main():
    n = int(input())
    files = {}
    for i in range(n):
        file = input()
        if file in files:
            files[file] += 1
            print(file + "(" + str(files[file]) + ")")
        else:
            files[file] = 0
            print(file)

=======
Suggestion 4

def print_new_name(n, names):
    name_dict = {}
    for name in names:
        if name in name_dict:
            name_dict[name] += 1
            print(name + '(' + str(name_dict[name]) + ')')
        else:
            name_dict[name] = 0
            print(name)

=======
Suggestion 5

def main():
    n = int(input())
    d = {}
    for i in range(n):
        s = input()
        if s in d:
            d[s] += 1
            print(s + '(' + str(d[s]) + ')')
        else:
            d[s] = 0
            print(s)

=======
Suggestion 6

def problem261_c():
    n = int(input())
    names = []
    for i in range(n):
        names.append(input())
    for i in range(n):
        if names.count(names[i]) == 1:
            print(names[i])
        else:
            print(names[i]+"("+str(names[0:i].count(names[i]))+")")

=======
Suggestion 7

def main():
    n = int(input())
    file = []
    for i in range(n):
        file.append(input())
    file_set = set(file)
    file_dict = {}
    for i in file_set:
        file_dict[i] = 0
    for i in range(n):
        if file[i] in file_set:
            file_set.remove(file[i])
            file_dict[file[i]] += 1
        if file_dict[file[i]] == 0:
            print(file[i])
        else:
            print(file[i] + "(" + str(file_dict[file[i]]) + ")")

=======
Suggestion 8

def main():
    n = int(input())
    s = []
    for i in range(n):
        s.append(input())
    for i in range(n):
        if i == 0:
            print(s[i])
        elif s[i] in s[:i]:
            print(s[i] + "(" + str(s[:i].count(s[i])) + ")")
        else:
            print(s[i])

=======
Suggestion 9

def main():
    n = int(input())
    s = []
    for i in range(n):
        s.append(input())
    dic = {}
    for i in range(n):
        if s[i] not in dic:
            dic[s[i]] = 1
            print(s[i])
        else:
            dic[s[i]] += 1
            print(s[i] + '(' + str(dic[s[i]]-1) + ')')

=======
Suggestion 10

def main():
    n = int(input())
    s = []
    for i in range(n):
        s.append(input())

    for i in range(n):
        if s[i] in s[0:i]:
            j = 1
            while s[i] + '(' + str(j) + ')' in s[0:i]:
                j += 1
            print(s[i] + '(' + str(j) + ')')
        else:
            print(s[i])
