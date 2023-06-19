Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    a, b = map(int, input().split())
    c, d = map(int, input().split())
    print(max(a-c, a-d, b-c, b-d))

=======
Suggestion 2

def main():
    a,b = map(int,input().split())
    c,d = map(int,input().split())
    print(b-d)

=======
Suggestion 3

def max_x_y(a,b,c,d):
    max_x_y = 0
    for i in range(a,b+1):
        for j in range(c,d+1):
            if i-j > max_x_y:
                max_x_y = i-j
    return max_x_y

=======
Suggestion 4

def main():
    a, b = map(int, input().split())
    c, d = map(int, input().split())
    print(b - c)

=======
Suggestion 5

def solve(a,b,c,d):
    return max(a*c,a*d,b*c,b*d)
