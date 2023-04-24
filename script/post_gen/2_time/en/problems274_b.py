Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    H, W = map(int, input().split())
    C = []
    for i in range(H):
        C.append(input())
    for i in range(W):
        count = 0
        for j in range(H):
            if C[j][i] == "#":
                count += 1
        print(count, end = " ")
    print()

=======
Suggestion 2

def solve():
    h, w = map(int, input().split())
    a = []
    for i in range(h):
        a.append(input())
    for i in range(w):
        count = 0
        for j in range(h):
            if a[j][i] == '#':
                count += 1
        print(count)

solve()

=======
Suggestion 3

def main():
  H, W = map(int, input().split())
  C = [input() for i in range(H)]
  for i in range(W):
    count = 0
    for j in range(H):
      if C[j][i] == '#':
        count += 1
    print(count, end=' ')

=======
Suggestion 4

def main():
    h,w = map(int, input().split())
    grid = []
    for _ in range(h):
        grid.append(input())
    for i in range(w):
        count = 0
        for j in range(h):
            if grid[j][i] == '#':
                count += 1
        print(count)

=======
Suggestion 5

def main():
    h, w = map(int, input().split())
    c = []
    for i in range(h):
        c.append(input())
    for i in range(w):
        print(sum(c[j][i] == '#' for j in range(h)))

=======
Suggestion 6

def main():
    h, w = map(int, input().split())
    l = []
    for i in range(h):
        l.append(input())
    c = []
    for i in range(w):
        c.append(0)
    for i in range(w):
        for j in range(h):
            if l[j][i] == "#":
                c[i] += 1
    print(*c)

=======
Suggestion 7

def main():
    h,w = map(int,input().split())
    a = [input() for _ in range(h)]
    for i in range(w):
        print(sum([1 for j in range(h) if a[j][i] == '#']))

=======
Suggestion 8

def problem274_b():
    h, w = map(int, input().split())
    c = [list(input()) for _ in range(h)]
    for i in range(h)

=======
Suggestion 9

def main():
    h, w = map(int, input().split())
    matrix = []
    for i in range(h):
        matrix.append(list(input()))
    matrix = list(zip(*matrix))
    for i in range(w):
        matrix[i] = list(matrix[i])
    for i in range(w):
        matrix[i] = matrix[i].count('#')
    print(*matrix)

=======
Suggestion 10

def main():
    # Get input here
    h, w = map(int, input().split())
    c = [input() for i in range(h)]
    
    # Calculate result here
    x = [0] * w
    for i in range(w):
        for j in range(h):
            if c[j][i] == '#':
                x[i] += 1
    
    # Print output here
    print(*x)
    
main()
