Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    w = []
    for i in range(n):
        w.append(input())
    for i in range(n-1):
        if w[i][-1] != w[i+1][0]:
            print("No")
            return
        if w[i] in w[i+1:]:
            print("No")
            return
    print("Yes")

=======
Suggestion 2

def shiritori(words):
    if len(words) != len(set(words)):
        return "No"
    for i in range(1,len(words)):
        if words[i][0] != words[i-1][-1]:
            return "No"
    return "Yes"

n = int(input())
words = [input() for i in range(n)]
print(shiritori(words))

=======
Suggestion 3

def main():
    N = int(input())
    W = [input() for i in range(N)]
    for i in range(1, N):
        if W[i] in W[:i] or W[i][0] != W[i-1][-1]:
            print('No')
            return
    print('Yes')

=======
Suggestion 4

def main():
    N = int(input())
    W = []
    for i in range(N):
        W.append(input())
    for i in range(1, N):
        if W[i - 1][-1] != W[i][0]:
            print('No')
            exit()
    if len(set(W)) != len(W):
        print('No')
        exit()
    print('Yes')

=======
Suggestion 5

def main():
    n = int(input())
    words = []
    for i in range(n):
        words.append(input())
    if len(words) != len(set(words)):
        print("No")
    else:
        for i in range(len(words)-1):
            if words[i][-1] != words[i+1][0]:
                print("No")
                break
        else:
            print("Yes")

=======
Suggestion 6

def main():
    N = int(input())
    W = []
    for i in range(N):
        W.append(input())
    for i in range(1, N):
        if W[i] in W[:i] or W[i-1][-1] != W[i][0]:
            print('No')
            exit()
    print('Yes')

=======
Suggestion 7

def solve():
    N = int(input())
    words = []
    for i in range(N):
        words.append(input())
    for i in range(N-1):
        if words[i] == words[i+1]:
            print("No")
            return
    for i in range(N-1):
        if words[i][-1] != words[i+1][0]:
            print("No")
            return
    print("Yes")
    return

=======
Suggestion 8

def main():
    n = int(input())
    w = [input() for _ in range(n)]
    for i in range(1,n):
        if w[i] in w[:i]:
            print('No')
            return
        if w[i][0] != w[i-1][-1]:
            print('No')
            return
    print('Yes')

=======
Suggestion 9

def main():
    n=int(input())
    w=[]
    for i in range(n):
        w.append(input())
    if len(w)!=len(set(w)):
        print("No")
        return
    for i in range(n-1):
        if w[i][-1]!=w[i+1][0]:
            print("No")
            return
    print("Yes")

=======
Suggestion 10

def main():
    n = int(input())
    words = []
    for i in range(n):
        word = input()
        if word in words:
            print("No")
            exit(0)
        if i != 0:
            if word[0] != prev_word[-1]:
                print("No")
                exit(0)
        words.append(word)
        prev_word = word
    print("Yes")
