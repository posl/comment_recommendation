Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N = int(input())
    S = [input() for _ in range(N)]
    print(len(set(S)))

=======
Suggestion 2

def main():
    N = int(input())
    S = []
    for i in range(N):
        S.append(input())
    print(len(set(S)))

=======
Suggestion 3

def main():
    N = int(input())
    S = []
    for i in range(N):
        S.append(input())
    S = set(S)
    print(len(S))

=======
Suggestion 4

def main():
    N = int(input())
    s = set()
    for i in range(N):
        s.add(input())
    print(len(s))

=======
Suggestion 5

def main():
    n = int(input())
    s = [input() for _ in range(n)]
    print(len(set(s)))

=======
Suggestion 6

def main():
    #input
    N = int(input())
    Ss = [input() for _ in range(N)]

    #compute
    Ss.sort()
    ans = 1
    for i in range(1,N):
        if Ss[i] != Ss[i-1]:
            ans += 1

    #output
    print(ans)
