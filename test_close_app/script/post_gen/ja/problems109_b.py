Synthesizing 10/10 solutions

=======

def main():
    N = int(input())
    W = [input() for _ in range(N)]
    if len(W) != len(set(W)):
        print("No")
        return
    for i in range(N-1):
        if W[i][-1] != W[i+1][0]:
            print("No")
            return
    print("Yes")
    return

=======

def main():
    N = int(input())
    W = [input() for _ in range(N)]
    if len(W) != len(set(W)):
        print('No')
        return
    for i in range(N-1):
        if W[i][-1] != W[i+1][0]:
            print('No')
            return
    print('Yes')

=======

def main():
    n = int(input())
    w = [input() for _ in range(n)]
    if len(w) != len(set(w)):
        print("No")
        return
    for i in range(1, n):
        if w[i-1][-1] != w[i][0]:
            print("No")
            return
    print("Yes")

=======

def main():
    n = int(input())
    w = [input() for i in range(n)]
    if len(w) != len(set(w)):
        print("No")
        return
    for i in range(n-1):
        if w[i][-1] != w[i+1][0]:
            print("No")
            return
    print("Yes")

=======

def main():
    n = int(input())
    w = [input() for _ in range(n)]
    print('Yes' if len(set(w)) == n and all(w[i][0] == w[i-1][-1] for i in range(1, n)) else 'No')

=======

def main():
    N = int(input())
    W = [input() for _ in range(N)]
    if N != len(set(W)):
        print("No")
        return
    for i in range(N-1):
        if W[i][-1] != W[i+1][0]:
            print("No")
            return
    print("Yes")

=======

def main():
    n = int(input())
    words = [input() for _ in range(n)]
    if len(words) != len(set(words)):
        print("No")
        return
    for i in range(n - 1):
        if words[i][-1] != words[i + 1][0]:
            print("No")
            return
    print("Yes")

=======

def main():
    N = int(input())
    W = []
    for i in range(N):
        W.append(input())

    if len(W) != len(set(W)):
        print("No")
        return

    for i in range(N-1):
        if W[i][-1] != W[i+1][0]:
            print("No")
            return

    print("Yes")

=======

def main():
    n = int(input())
    w = []
    for i in range(n):
        w.append(input())

    for i in range(n):
        if w.count(w[i]) > 1:
            print("No")
            return
        if i > 0:
            if w[i-1][-1] != w[i][0]:
                print("No")
                return
    print("Yes")

=======

def main():
    N = int(input())
    W = []
    for i in range(N):
        W.append(input())
    #print(N)
    #print(W)
    for i in range(N):
        if W.count(W[i]) > 1:
            print("No")
            return
        if i != 0:
            if W[i][0] != W[i-1][-1]:
                print("No")
                return
    print("Yes")
