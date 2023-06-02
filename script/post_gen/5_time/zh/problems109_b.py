Synthesizing 10/10 solutions

=======
Suggestion 1

def shiritori(n,words):
    flag = True
    for i in range(1,n):
        if words[i] in words[:i]:
            flag = False
            break
        if words[i][0] != words[i-1][-1]:
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
    w = []
    for i in range(n):
        w.append(input())
    w_set = set(w)
    if len(w) != len(w_set):
        print('No')
        return
    for i in range(n-1):
        if w[i][-1] != w[i+1][0]:
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
    #print(words)
    flag = True
    for i in range(n-1):
        if words[i][-1] != words[i+1][0]:
            flag = False
            break
        if words.count(words[i]) > 1:
            flag = False
            break
    if flag:
        print("Yes")
    else:
        print("No")

=======
Suggestion 4

def main():
    n = int(input())
    words = []
    for i in range(n):
        words.append(input())
    if len(set(words)) == len(words):
        for i in range(1,n):
            if words[i][0] != words[i-1][-1]:
                print("No")
                exit()
        print("Yes")
    else:
        print("No")

=======
Suggestion 5

def main():
    n = int(input())
    words = []
    for i in range(n):
        words.append(input())
    for i in range(n):
        for j in range(i+1,n):
            if words[i] == words[j]:
                print('No')
                return
    for i in range(1,n):
        if words[i][0] != words[i-1][-1]:
            print('No')
            return
    print('Yes')

=======
Suggestion 6

def shiritori():
    n = int(input())
    words = []
    for i in range(n):
        word = input()
        if word in words:
            return 'No'
        if i > 0 and words[i-1][-1] != word[0]:
            return 'No'
        words.append(word)
    return 'Yes'

=======
Suggestion 7

def main():
    n = int(input())
    w = []
    for i in range(n):
        w.append(input())
    for i in range(n):
        if i == 0:
            continue
        if w[i] in w[:i]:
            print("No")
            exit()
        if w[i][0] != w[i-1][-1]:
            print("No")
            exit()
    print("Yes")

=======
Suggestion 8

def checkShiritori(words):
    for i in range(len(words)-1):
        if words[i][-1] != words[i+1][0]:
            return False
    return True

n = int(input())
words = []
for i in range(n):
    words.append(input())

=======
Suggestion 9

def problem109b():
    n = int(input())
    words = []
    for i in range(n):
        words.append(input())
    for i in range(1,n):
        if words[i-1][-1] != words[i][0]:
            print("No")
            return
    if len(set(words)) == n:
        print("Yes")
    else:
        print("No")

=======
Suggestion 10

def shiritori():
    n = int(input())
    words = []
    for i in range(n):
        words.append(input())
    for i in range(1, n):
        if words[i] in words[0:i]:
            return 'No'
        if words[i][0] != words[i-1][-1]:
            return 'No'
    return 'Yes'
