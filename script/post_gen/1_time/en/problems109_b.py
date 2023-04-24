Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    W = [input() for i in range(N)]
    for i in range(N-1):
        if W[i][-1] != W[i+1][0]:
            print("No")
            return
        if W.count(W[i]) > 1:
            print("No")
            return
    print("Yes")
    return

=======
Suggestion 2

def shiritori():
    n = int(input())
    words = []
    for i in range(n):
        words.append(input())
    for i in range(n-1):
        if words[i][-1] != words[i+1][0]:
            print("No")
            return
        if words.count(words[i]) > 1:
            print("No")
            return
    print("Yes")
    return

=======
Suggestion 3

def shiritori():
    n = int(input())
    w = []
    for i in range(n):
        w.append(input())
    for i in range(n-1):
        if w[i][-1] != w[i+1][0]:
            return 'No'
        elif w.count(w[i]) > 1:
            return 'No'
    return 'Yes'

print(shiritori())

=======
Suggestion 4

def solve():
    N = int(input())
    words = []
    for i in range(N):
        words.append(input())
    for i in range(N-1):
        if words[i][-1] != words[i+1][0]:
            return False
    return True

=======
Suggestion 5

def main():
    n = int(input())
    words = []
    for i in range(n):
        words.append(input())
    if len(words) != len(set(words)):
        print("No")
        return
    for i in range(1, len(words)):
        if words[i][0] != words[i-1][-1]:
            print("No")
            return
    print("Yes")

=======
Suggestion 6

def main():
    n = int(input())
    words = []
    for i in range(n):
        word = input()
        if word in words:
            print('No')
            return
        if i != 0 and words[i-1][-1] != word[0]:
            print('No')
            return
        words.append(word)
    print('Yes')

=======
Suggestion 7

def shiritori(n, w):
    for i in range(n-1):
        if w[i] == w[i+1] or w[i][-1] != w[i+1][0]:
            return "No"
    return "Yes"

n = int(input())
w = []
for _ in range(n):
    w.append(input())

print(shiritori(n, w))

=======
Suggestion 8

def main():
    n = int(input())
    words = []
    for i in range(n):
        words.append(input())

    for i in range(n):
        if i != 0:
            if words[i] in words[:i]:
                print("No")
                exit()
        if i != n - 1:
            if words[i][-1] != words[i + 1][0]:
                print("No")
                exit()

    print("Yes")

=======
Suggestion 9

def main():
    n = int(input())
    w = []
    for i in range(n):
        w.append(input())
    for i in range(n-1):
        if w[i] in w[:i]:
            print('No')
            return
        if w[i][-1] != w[i+1][0]:
            print('No')
            return
    print('Yes')
    return

=======
Suggestion 10

def main():
    n = input()
    words = []
    for i in range(int(n)):
        words.append(input())
    result = 'Yes'
    for i in range(len(words)):
        if i == 0:
            continue
        if words[i] in words[:i]:
            result = 'No'
            break
        if words[i][0] != words[i-1][-1]:
            result = 'No'
            break
    print(result)
