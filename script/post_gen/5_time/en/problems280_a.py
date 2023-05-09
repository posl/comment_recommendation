Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    h, w = map(int, input().split())
    s = []
    for i in range(h):
        s.append(input())
    count = 0
    for i in range(h):
        for j in range(w):
            if(s[i][j] == '#'):
                count += 1
    print(count)

=======
Suggestion 2

def solve():
    H, W = map(int, input().split())
    S = [input() for _ in range(H)]
    ans = 0
    for i in range(H):
        for j in range(W):
            if S[i][j] == '#':
                ans += 1
    print(ans)

=======
Suggestion 3

def main():
    H, W = map(int, input().split())
    S = []
    for _ in range(H):
        S.append(input())
    count = 0
    for i in range(H):
        for j in range(W):
            if S[i][j] == '#':
                count += 1
    print(count)

=======
Suggestion 4

def main():
    h,w = map(int, input().split())
    s = [input() for _ in range(h)]
    ans = 0
    for i in range(h):
        for j in range(w):
            if s[i][j] == '#':
                ans += 1
    print(ans)

=======
Suggestion 5

def main():
    H, W = map(int, input().split())
    S = list()
    for i in range(H):
        S.append(input())
    count = 0
    for i in range(H):
        for j in range(W):
            if S[i][j] == '#':
                count += 1
    print(count)

=======
Suggestion 6

def main():
    H, W = map(int, input().rstrip().split())
    S = []
    for _ in range(H):
        S.append(input().rstrip())
    count = 0
    for i in range(H):
        for j in range(W):
            if S[i][j] == "#":
                count += 1
    print(count)

=======
Suggestion 7

def main():
    # input
    H, W = map(int, input().split())
    # solve
    ans = 0
    for _ in range(H):
        ans += input().count("#")
    # output
    print(ans)

=======
Suggestion 8

def main():
    # Take input here
    h, w = map(int, input().strip().split())
    s = [input().strip() for _ in range(h)]
    # Compute desired result here
    count = 0
    for i in range(h):
        for j in range(w):
            if s[i][j] == '#':
                count += 1
    # Print result here
    print(count)

=======
Suggestion 9

def main():
    h, w = map(int, input().split())
    print(h, w)

=======
Suggestion 10

def solve(H, W, S):
    return sum([s.count('#') for s in S])
