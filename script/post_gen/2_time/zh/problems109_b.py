Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    words = []
    for i in range(n):
        words.append(input())

    flag = True
    for i in range(n-1):
        if words[i] == words[i+1]:
            flag = False
            break
        if words[i][-1] != words[i+1][0]:
            flag = False
            break

    if flag:
        print("Yes")
    else:
        print("No")

=======
Suggestion 2

def main():
    n = int(input())
    w = [input() for _ in range(n)]
    if len(w) != len(set(w)):
        print('No')
        return
    for i in range(1, n):
        if w[i][0] != w[i-1][-1]:
            print('No')
            return
    print('Yes')

=======
Suggestion 3

def main():
    n = int(input())
    words = []
    for i in range(n):
        words.append(input())
    words_set = set(words)
    if len(words_set) != n:
        print("No")
        return
    for i in range(1, n):
        if words[i-1][-1] != words[i][0]:
            print("No")
            return
    print("Yes")
    return

=======
Suggestion 4

def shiritori():
    n = int(input())
    w = []
    for i in range(n):
        w.append(input())
    flag = True
    for i in range(1,n):
        if w[i] in w[:i] or w[i-1][-1] != w[i][0]:
            flag = False
            break
    if flag:
        print("Yes")
    else:
        print("No")

=======
Suggestion 5

def problems109_b():
    n = int(input())
    w = []
    for i in range(n):
        w.append(input())
    for i in range(n):
        for j in range(i+1,n):
            if w[i] == w[j]:
                print("No")
                return
    for i in range(n-1):
        if w[i][-1] != w[i+1][0]:
            print("No")
            return
    print("Yes")

=======
Suggestion 6

def shiritori():
    n = int(input())
    words = []
    for i in range(n):
        words.append(input())
    # print(words)
    for i in range(n-1):
        if words[i][-1] != words[i+1][0]:
            return 'No'
    for i in range(n):
        for j in range(i+1,n):
            if words[i] == words[j]:
                return 'No'
    return 'Yes'

print(shiritori())

=======
Suggestion 7

def main():
    n = int(input())
    words = []
    for i in range(n):
        word = input()
        words.append(word)

    for i in range(len(words)):
        if i == 0:
            continue
        if words[i] in words[0:i]:
            print("No")
            return
        if words[i][0] != words[i-1][-1]:
            print("No")
            return

    print("Yes")

=======
Suggestion 8

def check_rule(w):
    for i in range(len(w)-1):
        if w[i] == w[i+1]:
            return False
    return True

n = int(input())
w = []
for i in range(n):
    w.append(input())

for i in range(n-1):
    if w[i] in w[i+1:] or w[i][-1] != w[i+1][0]:
        print("No")
        exit()

print("Yes")

=======
Suggestion 9

def check_shiritori():
    n = int(input())
    words = []
    for i in range(n):
        words.append(input())
    for i in range(n-1):
        if words[i] == words[i+1]:
            return "No"
        if words[i][-1] != words[i+1][0]:
            return "No"
    return "Yes"

=======
Suggestion 10

def main():
    n = int(input())
    words = []
    for i in range(n):
        words.append(input())
    flag = True
    for i in range(n-1):
        if words[i][-1] != words[i+1][0]:
            flag = False
            break
        if words[i] in words[i+1:]:
            flag = False
            break
    if flag:
        print("Yes")
    else:
        print("No")
