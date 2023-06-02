Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n = int(input())
    h = list(map(int, input().split()))
    print(h.index(max(h))+1)

=======
Suggestion 2

def max_height_bridge():
    n = int(input())
    bridges = list(map(int, input().split()))
    max_height = max(bridges)
    print(bridges.index(max_height)+1)

=======
Suggestion 3

def main():
    n = int(input())
    height = list(map(int, input().split()))
    print(height.index(max(height)) + 1)

=======
Suggestion 4

def main():
    N = int(input())
    H = list(map(int, input().split()))
    max_h = max(H)
    for i in range(N):
        if H[i] == max_h:
            print(i+1)
            break

=======
Suggestion 5

def main():
    num = int(input())
    height = list(map(int, input().split()))
    print(height.index(max(height)) + 1)

=======
Suggestion 6

def main():
    n = int(input())
    h = input().split()
    h = [int(i) for i in h]
    print(h.index(max(h))+1)

=======
Suggestion 7

def main():
    N = int(input())
    H = list(map(int, input().split()))
    print(H.index(max(H))+1)
