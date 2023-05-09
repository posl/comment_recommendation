Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    S, T = map(int, input().split())
    count = 0
    for a in range(S+1):
        for b in range(S+1):
            for c in range(S+1):
                if a + b + c <= S and a * b * c <= T:
                    count += 1
    print(count)

=======
Suggestion 2

def main():
    s, t = map(int, input().split())
    count = 0
    for a in range(s + 1):
        for b in range(s + 1):
            for c in range(s + 1):
                if a + b + c <= s and a * b * c <= t:
                    count += 1
    print(count)

=======
Suggestion 3

def main():
    s, t = map(int, input().split())
    ans = 0
    for a in range(s+1):
        for b in range(s+1):
            for c in range(s+1):
                if a+b+c <= s and a*b*c <= t:
                    ans += 1
    print(ans)


main()

=======
Suggestion 4

def main():
    S, T = map(int, input().split())
    ans = 0
    for a in range(S+1):
        for b in range(S+1):
            for c in range(S+1):
                if a+b+c <= S and a*b*c <= T:
                    ans += 1
    print(ans)

=======
Suggestion 5

def solve(s, t):
    count = 0
    for a in range(s+1):
        for b in range(s+1):
            for c in range(s+1):
                if a+b+c <= s and a*b*c <= t:
                    count += 1
    return count

=======
Suggestion 6

def main():
    S, T = map(int, input().split())
    count = 0
    for i in range(S+1):
        for j in range(S+1):
            for k in range(S+1):
                if i + j + k <= S and i * j * k <= T:
                    count += 1
    print(count)

=======
Suggestion 7

def count_triples(s, t):
    count = 0
    for a in range(s+1):
        for b in range(s+1):
            for c in range(s+1):
                if a + b + c <= s and a * b * c <= t:
                    count += 1
    return count

=======
Suggestion 8

def main():
    s,t = map(int,input().split())
    count = 0
    for i in range(s+1):
        for j in range(s+1-i):
            for k in range(s+1-i-j):
                if i*j*k <= t:
                    count += 1
    print(count)

=======
Suggestion 9

def problem():
    S, T = map(int, input().split())
    ans = 0
    for a in range(S+1):
        for b in range(S+1):
            for c in range(S+1):
                if a+b+c <= S and a*b*c <= T:
                    ans += 1
    print(ans)

problem()

=======
Suggestion 10

def get_input():
    return map(int, input().split())
