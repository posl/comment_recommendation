Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    words = []
    for i in range(n):
        words.append(input())
    for i in range(len(words)-1):
        if words[i][-1] != words[i+1][0]:
            print("No")
            return
    if len(words) != len(set(words)):
        print("No")
        return
    print("Yes")

=======
Suggestion 2

def main():
    n = int(input())
    words = []
    for i in range(0,n):
        words.append(input())
    for i in range(0,n-1):
        if words[i][-1] != words[i+1][0]:
            print("No")
            return
    for i in range(0,n-1):
        if words[i] in words[i+1:]:
            print("No")
            return
    print("Yes")

=======
Suggestion 3

def main():
    n = int(input())
    w = []
    for i in range(n):
        w.append(input())
    for i in range(1,n):
        if w[i] in w[:i]:
            print("No")
            return
        if w[i][0] != w[i-1][-1]:
            print("No")
            return
    print("Yes")
    return

=======
Suggestion 4

def main():
    n = int(input())
    words = []
    for i in range(n):
        words.append(input())
    if len(words) != len(set(words)):
        print("No")
        return
    for i in range(1, n):
        if words[i][0] != words[i - 1][-1]:
            print("No")
            return
    print("Yes")

=======
Suggestion 5

def main():
    n = int(input())
    words = []
    for i in range(n):
        word = input()
        if word in words:
            print('No')
            return
        if i > 0:
            if words[-1][-1] != word[0]:
                print('No')
                return
        words.append(word)
    print('Yes')

=======
Suggestion 6

def shiritori(n, words):
    if len(set(words)) == n and all(words[i][-1] == words[i+1][0] for i in range(n-1)):
        print("Yes")
    else:
        print("No")

=======
Suggestion 7

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
Suggestion 8

def shiritori():
    n = int(input())
    words = []
    for i in range(n):
        words.append(input())
    if len(words) != len(set(words)):
        print("No")
    else:
        for i in range(n-1):
            if words[i][-1] != words[i+1][0]:
                print("No")
                break
        else:
            print("Yes")
shiritori()

=======
Suggestion 9

def main():
    n = int(input())
    words = []
    for _ in range(n):
        words.append(input())
    if len(set(words)) == len(words):
        if len(set([w[0] for w in words])) == len(words):
            print('Yes')
        else:
            print('No')
    else:
        print('No')

=======
Suggestion 10

def shiritori(N):
    words = []
    for i in range(N):
        word = input()
        if word in words:
            return False
        if i > 0 and words[-1][-1] != word[0]:
            return False
        words.append(word)
    return True
