Synthesizing 10/10 solutions

=======
Suggestion 1

def check_shiritori(n, words):
    if len(words) != n:
        return False
    if len(set(words)) != n:
        return False
    for i in range(1, n):
        if words[i][0] != words[i - 1][-1]:
            return False
    return True

=======
Suggestion 2

def main():
    n = int(input())
    words = []
    for i in range(n):
        word = input()
        if word in words:
            print("No")
            return
        else:
            words.append(word)
        if i > 0 and words[i-1][-1] != words[i][0]:
            print("No")
            return
    print("Yes")

=======
Suggestion 3

def checkShiritori(words):
    if len(words) == len(set(words)):
        return True
    else:
        return False

=======
Suggestion 4

def main():
    N = int(input())
    W = []
    for i in range(N):
        W.append(input())
    for i in range(1, N):
        if W[i] in W[:i]:
            print("No")
            return
        if W[i][0] != W[i - 1][-1]:
            print("No")
            return
    print("Yes")

=======
Suggestion 5

def check_shiritori(word_list):
    word_dict = {}
    for word in word_list:
        if word in word_dict:
            return False
        else:
            word_dict[word] = 1
    for i in range(len(word_list)-1):
        if word_list[i][-1] != word_list[i+1][0]:
            return False
    return True

=======
Suggestion 6

def check_shiritori(words):
    for i in range(len(words)):
        if i == 0:
            continue
        if words[i][0] != words[i-1][-1]:
            return False
    return True

n = int(input())
words = []
for i in range(n):
    word = input()
    words.append(word)

=======
Suggestion 7

def check_shiritori(words):
    if len(words) == len(set(words)):
        for i in range(0, len(words)-1):
            if words[i][-1] != words[i+1][0]:
                return False
        return True
    else:
        return False

n = int(input())
words = []
for i in range(n):
    words.append(input())

=======
Suggestion 8

def main():
    N = int(input())
    word_list = []
    word_list.append(input())
    for i in range(N-1):
        word_list.append(input())
    for i in range(N-1):
        if word_list[i][-1] != word_list[i+1][0]:
            print('No')
            exit()
        for j in range(i+1,N):
            if word_list[i] == word_list[j]:
                print('No')
                exit()
    print('Yes')

=======
Suggestion 9

def main():
    n = int(input())
    words = []
    for i in range(n):
        word = input()
        if word in words:
            print('No')
            return
        words.append(word)
        if i == 0:
            continue
        if words[i][0] != words[i-1][-1]:
            print('No')
            return
    print('Yes')
    return

=======
Suggestion 10

def main():
    n = int(input())
    w = []
    for i in range(n):
        w.append(input())
    flag = True
    for j in range(n-1):
        if w[j][-1] != w[j+1][0]:
            flag = False
            break
        for k in range(j+1,n):
            if w[j] == w[k]:
                flag = False
                break
    if flag:
        print("Yes")
    else:
        print("No")
