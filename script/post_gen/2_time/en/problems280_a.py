Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    H, W = map(int, input().split())
    S = [input() for _ in range(H)]
    ans = 0
    for i in range(H):
        for j in range(W):
            if S[i][j] == '#':
                ans += 1
    print(ans)

=======
Suggestion 2

def main():
    h, w = map(int, input().split())
    s = [input() for _ in range(h)]
    ans = 0
    for i in range(h):
        for j in range(w):
            if s[i][j] == "#":
                ans += 1
    print(ans)

=======
Suggestion 3

def main():
    H, W = map(int, input().split())
    grid = []
    for i in range(H):
        grid.append(input())
    count = 0
    for i in range(H):
        for j in range(W):
            if grid[i][j] == "#":
                count += 1
    print(count)

=======
Suggestion 4

def main():
    H, W = map(int, input().split())
    S = [input() for _ in range(H)]
    ans = 0
    for i in range(H):
        ans += S[i].count('#')
    print(ans)

=======
Suggestion 5

def main():
    H, W = map(int, input().split())
    ans = 0
    for i in range(H):
        ans += input().count('#')
    print(ans)

=======
Suggestion 6

def main():
    h,w = map(int, input().split())
    s = []
    for i in range(h):
        s.append(input())
    cnt = 0
    for i in range(h):
        for j in range(w):
            if s[i][j] == '#':
                cnt += 1
    print(cnt)

=======
Suggestion 7

def main():
    #input
    H, W = map(int, input().split())
    S = [input() for _ in range(H)]
    #solve
    ans = 0
    for i in range(H):
        for j in range(W):
            if S[i][j] == '#':
                ans += 1
    #output
    print(ans)

=======
Suggestion 8

def main():
    #input
    H, W = map(int, input().split())
    S = [input() for _ in range(H)]

    #count
    count = 0
    for i in range(H):
        for j in range(W):
            if S[i][j] == '#':
                count += 1

    #output
    print(count)

=======
Suggestion 9

def main():
    h, w = map(int, input().split())
    s = [input() for _ in range(h)]

    #print(h, w, s)

    count = 0
    for i in range(h):
        for j in range(w):
            if s[i][j] == '#':
                count += 1

    print(count)

=======
Suggestion 10

def main():
    #Read input data
    H, W = map(int, input().split())
    S = [input() for i in range(H)]

    #Count the number of squares with pieces
    count = 0
    for i in range(H):
        count += S[i].count("#")

    #Print the number of squares with pieces
    print(count)
