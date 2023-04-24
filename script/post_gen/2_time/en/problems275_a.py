Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N = int(input())
    H = list(map(int, input().split()))
    print(H.index(max(H)) + 1)

=======
Suggestion 2

def main():
    n = int(input())
    h = list(map(int, input().split()))
    print(h.index(max(h)) + 1)

main()

=======
Suggestion 3

def main():
    n = int(input())
    h = list(map(int, input().split()))
    print(h.index(max(h)) + 1)

=======
Suggestion 4

def main():
    N = int(input())
    H = list(map(int, input().split()))
    maxH = max(H)
    for i in range(N):
        if H[i] == maxH:
            print(i+1)
            return

=======
Suggestion 5

def main():
    N = int(input())
    H = [int(x) for x in input().split()]
    maxH = max(H)
    for i in range(N):
        if H[i] == maxH:
            print(i+1)
            break

=======
Suggestion 6

def main():
    N = int(input())
    H = [int(i) for i in input().split()]
    print(H.index(max(H))+1)

=======
Suggestion 7

def main():
    #input
    N = int(input())
    H = list(map(int, input().split()))
    #compute
    ans = H.index(max(H)) + 1
    #output
    print(ans)
