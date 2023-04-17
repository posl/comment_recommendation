Synthesizing 10/10 solutions

=======

def main():
    n = int(input())
    w = [input() for _ in range(n)]
    for i in range(n-1):
        if w[i] == w[i+1] or w[i][-1] != w[i+1][0]:
            print('No')
            exit()
    print('Yes')

=======

def main():
    N = int(input())
    W = [input() for _ in range(N)]
    if len(set(W)) != N:
        print('No')
        return
    for i in range(1, N):
        if W[i][0] != W[i-1][-1]:
            print('No')
            return
    print('Yes')

=======

def main():
    N = int(input())
    W = [input() for i in range(N)]
    if len(W) != len(set(W)):
        print("No")
        return
    for i in range(N-1):
        if W[i][-1] != W[i+1][0]:
            print("No")
            return
    print("Yes")

main()

=======

def main():
    n = int(input())
    w = [input() for _ in range(n)]
    if len(set(w)) != n:
        print('No')
        return
    for i in range(1, n):
        if w[i - 1][-1] != w[i][0]:
            print('No')
            return
    print('Yes')

=======

def main():
    N = int(input())
    W = [input() for i in range(N)]
    if len(W) != len(set(W)):
        print("No")
        return
    for i in range(1, N):
        if W[i-1][-1] != W[i][0]:
            print("No")
            return
    print("Yes")

=======

def shiritori():
    n = int(input())
    w = []
    for i in range(n):
        w.append(input())
    for i in range(1, n):
        if w[i] in w[:i] or w[i][0] != w[i-1][-1]:
            return 'No'
    return 'Yes'

print(shiritori())

=======

def main():
    n = int(input())
    words = []
    for i in range(n):
        words.append(input())
    if len(set(words)) == len(words):
        for i in range(1, len(words)):
            if words[i][0] != words[i - 1][-1]:
                print("No")
                return
        print("Yes")
    else:
        print("No")
        return

=======

def main():
    N = int(input())
    s = [input() for _ in range(N)]
    if len(s) == len(set(s)):
        for i in range(N-1):
            if s[i][-1] != s[i+1][0]:
                print("No")
                return
        print("Yes")
        return
    print("No")

=======

def shiritori():
    #Read input
    N = int(input())
    W = [input() for i in range(N)]
    
    #Check if the rules of shiritori was observed
    if len(W) != len(set(W)):
        return 'No'
    else:
        for i in range(1, N):
            if W[i][0] != W[i-1][-1]:
                return 'No'
        return 'Yes'

=======

def check_shiritori(n, w):
    # Your code here
    return "Yes"
