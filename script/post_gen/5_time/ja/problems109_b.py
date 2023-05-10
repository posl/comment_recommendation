Synthesizing 10/10 solutions

=======
Suggestion 1

def check(w, words):
    if w in words:
        return False
    if len(words) == 0:
        return True
    if w[0] != words[-1][-1]:
        return False
    return True

n = int(input())
words = []
for i in range(n):
    w = input()
    if not check(w, words):
        print('No')
        exit()
    words.append(w)
print('Yes')

=======
Suggestion 2

def main():
    n = int(input())
    words = []
    for i in range(n):
        words.append(input())
    for i in range(n):
        if i != 0:
            if words[i] in words[:i]:
                print('No')
                exit()
            if words[i][0] != words[i-1][-1]:
                print('No')
                exit()
    print('Yes')

=======
Suggestion 3

def main():
    n = int(input())
    w = [input() for i in range(n)]
    for i in range(n-1):
        if w[i][-1] != w[i+1][0]:
            print('No')
            return
        for j in range(i+1,n):
            if w[i] == w[j]:
                print('No')
                return
    print('Yes')
    return

=======
Suggestion 4

def check_shiritori(words):
    for i in range(len(words)):
        for j in range(i+1,len(words)):
            if words[i] == words[j]:
                return False
    return True

=======
Suggestion 5

def main():
    n = int(input())
    w = [input() for _ in range(n)]
    for i in range(n - 1):
        if w[i][-1] != w[i + 1][0]:
            print('No')
            exit()
        if w.count(w[i]) > 1:
            print('No')
            exit()
    print('Yes')

=======
Suggestion 6

def main():
    n = int(input())
    w_list = []
    for i in range(n):
        w_list.append(input())
    for i in range(n):
        if i != 0:
            if w_list[i] in w_list[0:i]:
                print('No')
                exit()
        if i != n-1:
            if w_list[i][-1] != w_list[i+1][0]:
                print('No')
                exit()
    print('Yes')

=======
Suggestion 7

def main():
    n = int(input())
    words = []
    for i in range(n):
        word = input()
        if word in words:
            print('No')
            return
        else:
            words.append(word)
        if i > 0:
            if word[0] != words[i-1][-1]:
                print('No')
                return
    print('Yes')

main()

=======
Suggestion 8

def main():
    N = int(input())
    W_list = []
    for i in range(N):
        W_list.append(input())

    flag = True
    for i in range(N-1):
        if W_list[i] in W_list[i+1:]:
            flag = False
            break
        if W_list[i][-1] != W_list[i+1][0]:
            flag = False
            break

    if flag:
        print("Yes")
    else:
        print("No")

=======
Suggestion 9

def solve():
    n = int(input())
    words = []
    for i in range(n):
        words.append(input())

    for i in range(n):
        for j in range(i+1, n):
            if words[i] == words[j]:
                print("No")
                return
    for i in range(n-1):
        if words[i][-1] != words[i+1][0]:
            print("No")
            return
    print("Yes")

=======
Suggestion 10

def main():
    n = int(input())
    w = []
    for i in range(n):
        w.append(input())
    for i in range(n-1):
        if w[i][-1] != w[i+1][0]:
            print("No")
            exit()
        if w.count(w[i]) > 1:
            print("No")
            exit()
    print("Yes")
