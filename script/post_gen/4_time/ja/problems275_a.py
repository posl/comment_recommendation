Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n = int(input())
    h = list(map(int, input().split()))
    print(h.index(max(h)) + 1)

=======
Suggestion 2

def main():
    N = int(input())
    H = list(map(int, input().split()))
    print(H.index(max(H)) + 1)

=======
Suggestion 3

def main():
    N = int(input())
    H = list(map(int,input().split()))
    for i in range(N):
        if H[i] == max(H):
            print(i+1)
            break
