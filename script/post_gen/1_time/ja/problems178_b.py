Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    a, b, c, d = map(int, input().split())
    print(max(a * c, a * d, b * c, b * d))

=======
Suggestion 2

def main():
    a,b,c,d = map(int,input().split())
    print(max(a*c,a*d,b*c,b*d))
main()

=======
Suggestion 3

def solve():
    a,b,c,d = map(int, input().split())
    return max(a*c,a*d,b*c,b*d)

print(solve())
