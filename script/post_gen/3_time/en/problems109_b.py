Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    W = [input() for _ in range(N)]
    for i in range(1, N):
        if W[i-1][-1] != W[i][0] or W[i] in W[:i]:
            print('No')
            return
    print('Yes')

=======
Suggestion 2

def main():
    n = int(input())
    w = [input() for _ in range(n)]
    for i in range(1, n):
        if w[i] in w[:i] or w[i-1][-1] != w[i][0]:
            print('No')
            return
    print('Yes')
    return

=======
Suggestion 3

def main():
    N = int(input())
    W = [input() for _ in range(N)]
    if len(set(W)) != N:
        print("No")
        return
    for i in range(N-1):
        if W[i][-1] != W[i+1][0]:
            print("No")
            return
    print("Yes")
    return

main()

=======
Suggestion 4

def main():
    N = int(input())
    W = [input() for _ in range(N)]
    if len(set(W)) != N or any(W[i][0] != W[i-1][-1] for i in range(1, N)):
        print('No')
    else:
        print('Yes')

=======
Suggestion 5

def main():
    N = int(input())
    W = [input() for i in range(N)]
    if len(W) != len(set(W)):
        print('No')
        return
    for i in range(1, N):
        if W[i-1][-1] != W[i][0]:
            print('No')
            return
    print('Yes')

=======
Suggestion 6

def main():
    N = int(input())
    W = []
    for i in range(N):
        W.append(input())
    if len(set(W)) != N:
        print("No")
        return
    for i in range(N-1):
        if W[i][-1] != W[i+1][0]:
            print("No")
            return
    print("Yes")

=======
Suggestion 7

def main():
    n = int(input())
    words = [input() for _ in range(n)]

    if len(set(words)) != len(words):
        print("No")
        return

    for i in range(1, n):
        if words[i][0] != words[i - 1][-1]:
            print("No")
            return

    print("Yes")

=======
Suggestion 8

def main():
    #input
    N = int(input())
    W = [input() for _ in range(N)]

    #compute
    for i in range(1, N):
        if W[i-1][-1] != W[i][0] or W[i] in W[:i]:
            print('No')
            return

    #output
    print('Yes')

=======
Suggestion 9

def main():
    N = int(input())
    W = [input() for _ in range(N)]
    if len(W) != len(set(W)):
        print("No")
        exit()
    for i in range(N - 1):
        if W[i][-1] != W[i + 1][0]:
            print("No")
            exit()
    print("Yes")

=======
Suggestion 10

def shiritori():
    N = int(input())
    W = [input() for _ in range(N)]
    ans = "Yes"
    for i in range(N-1):
        if W[i] != W[i+1] and W[i][-1] != W[i+1][0]:
            ans = "No"
            break
    print(ans)

shiritori()
