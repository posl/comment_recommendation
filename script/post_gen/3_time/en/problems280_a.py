Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    h,w = map(int,input().split())
    count = 0
    for i in range(h):
        s = input()
        for j in range(w):
            if s[j] == '#':
                count += 1
    print(count)

=======
Suggestion 2

def main():
    h, w = map(int, input().split())
    s = [input() for _ in range(h)]
    print(sum([s[i][j] == "#" for i in range(h) for j in range(w)]))

=======
Suggestion 3

def main():
    H, W = map(int, input().split())

    count = 0
    for i in range(H):
        count += input().count('#')

    print(count)

=======
Suggestion 4

def main():
    H, W = map(int, input().split())
    S = [input() for _ in range(H)]
    print(sum([s.count('#') for s in S]))

=======
Suggestion 5

def main():
    # input
    H, W = map(int, input().split())
    S = [input() for i in range(H)]

    # compute

    # output
    print(S)

=======
Suggestion 6

def main():
    # Get input here
    h, w = map(int, input().split())
    s = [input() for _ in range(h)]

    # Calculate result here
    result = 0
    for i in range(h):
        result += s[i].count('#')

    # Print output here
    print(result)

=======
Suggestion 7

def main():
    # input
    H, W = map(int, input().split())
    S = [input() for _ in range(H)]

    # compute

    # output
    print(sum([s.count("#") for s in S]))

=======
Suggestion 8

def main():
    h, w = map(int, input().split())
    s = [input() for _ in range(h)]
    print(sum([si.count('#') for si in s]))

=======
Suggestion 9

def main():
    H,W = map(int,input().strip().split())
    S = [input() for _ in range(H)]
    print(sum([s.count('#') for s in S]))

=======
Suggestion 10

def solve():
    h, w = map(int, input().split())
    print(sum([input().count('#') for i in range(h)]))
