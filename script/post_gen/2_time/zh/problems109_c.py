Synthesizing 10/10 solutions

=======
Suggestion 1

def shiritori():
    n = int(input())
    words = []
    for i in range(n):
        words.append(input())
    for i in range(n-1):
        if words[i][-1] != words[i+1][0]:
            print('No')
            return
    if len(set(words)) != n:
        print('No')
        return
    print('Yes')

=======
Suggestion 2

def main():
    n = int(input())
    words = []
    for i in range(n):
        words.append(input())

    for i in range(len(words)):
        if i == 0:
            continue
        if words[i] in words[:i]:
            print("No")
            return
        if words[i][0] != words[i-1][-1]:
            print("No")
            return
    print("Yes")

=======
Suggestion 3

def check_shiritori(words):
    for i in range(1, len(words)):
        if words[i] in words[:i]:
            return False
        if words[i][0] != words[i-1][-1]:
            return False
    return True

=======
Suggestion 4

def main():
    N = int(input())
    words = []
    for i in range(N):
        words.append(input())
    for i in range(N):
        if i == 0:
            continue
        if words[i] in words[:i]:
            print("No")
            return
        if words[i][0] != words[i-1][-1]:
            print("No")
            return
    print("Yes")

=======
Suggestion 5

def main():
    n = int(input())
    w = []
    for i in range(n):
        w.append(str(input()))
    if len(w) != len(set(w)):
        print('No')
    else:
        for i in range(n-1):
            if w[i][-1] != w[i+1][0]:
                print('No')
                break
        else:
            print('Yes')

=======
Suggestion 6

def main():
    n = int(input())
    words = []
    for i in range(n):
        words.append(input())
    for i in range(n-1):
        if words[i][-1] != words[i+1][0]:
            print("No")
            return
    for i in range(n-1):
        for j in range(i+1, n):
            if words[i] == words[j]:
                print("No")
                return
    print("Yes")

=======
Suggestion 7

def shiritori():
    n = int(input())
    w = []
    for i in range(n):
        w.append(input())
    for i in range(1, n):
        if w[i-1][-1] != w[i][0]:
            return "No"
        if w.count(w[i]) > 1:
            return "No"
    return "Yes"

print(shiritori())

=======
Suggestion 8

def check_shiritori(words):
    for i in range(len(words)-1):
        if words[i][-1] != words[i+1][0]:
            return False
        if words.count(words[i]) > 1:
            return False
    return True

=======
Suggestion 9

def main():
    n = int(input())
    words = []
    for i in range(n):
        words.append(input())

    for i in range(n):
        if i == 0:
            continue
        if words[i][0] != words[i-1][-1]:
            print("No")
            return
        if words.count(words[i]) > 1:
            print("No")
            return
    print("Yes")

=======
Suggestion 10

def checkShiritori(words):
    if len(words) != len(set(words)):
        return False
    for i in range(len(words)-1):
        if words[i][-1] != words[i+1][0]:
            return False
    return True

n = int(input())
words = [input() for i in range(n)]
