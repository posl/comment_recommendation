Synthesizing 10/10 solutions

=======
Suggestion 1

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

main()

=======
Suggestion 2

def main():
    N = int(input())
    W = []
    for i in range(N):
        W.append(input())

    for i in range(1,N):
        if W[i-1][-1] != W[i][0] or W[i] in W[:i]:
            print("No")
            return
    print("Yes")

=======
Suggestion 3

def main():
    n = int(input())
    w = [input() for i in range(n)]
    for i in range(1,n):
        if w[i-1][-1] != w[i][0] or w[i] in w[:i]:
            print("No")
            return
    print("Yes")

=======
Suggestion 4

def main():
    N = int(input())
    W = [input() for _ in range(N)]

    if len(W) != len(set(W)):
        print('No')
        return

    for i in range(1, len(W)):
        if W[i][0] != W[i-1][-1]:
            print('No')
            return

    print('Yes')

=======
Suggestion 5

def main():
    n = int(input())
    w = [input() for _ in range(n)]
    if len(set(w)) != n:
        print('No')
        return
    for i in range(1, n):
        if w[i-1][-1] != w[i][0]:
            print('No')
            return
    print('Yes')

=======
Suggestion 6

def main():
    N = int(input())
    W = [input() for _ in range(N)]
    for i in range(N):
        for j in range(i):
            if W[i] == W[j]:
                print('No')
                return
    for i in range(1,N):
        if W[i-1][-1] != W[i][0]:
            print('No')
            return
    print('Yes')

=======
Suggestion 7

def main():
    N = int(input())
    W = [input() for _ in range(N)]

    if len(set(W)) == N:
        for i in range(N-1):
            if W[i][-1] != W[i+1][0]:
                print("No")
                return
        print("Yes")
    else:
        print("No")
        return

=======
Suggestion 8

def main():
    N = int(input())
    W = []
    for i in range(N):
        W.append(input())
    print(W)
    print("Yes" if len(W) == len(set(W)) and all(W[i][0] == W[i-1][-1] for i in range(1, N)) else "No")

=======
Suggestion 9

def main():
    N = int(input())
    W = []
    for i in range(N):
        W.append(input())
    print(W)
    print('Yes') if len(set(W)) == len(W) and all(W[i][0] == W[i-1][-1] for i in range(1, N)) else print('No')

=======
Suggestion 10

def main():
    N = int(input())
    W = [input() for _ in range(N)]
    #print(W)

    for i in range(N):
        for j in range(i+1, N):
            #print(W[i], W[j])
            if W[i] == W[j]:
                print("No")
                return

    for i in range(N-1):
        if W[i][-1] != W[i+1][0]:
            print("No")
            return

    print("Yes")
