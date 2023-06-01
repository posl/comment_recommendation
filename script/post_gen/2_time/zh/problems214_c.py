Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    s, t = map(int, input().split())
    ans = 0
    for a in range(s+1):
        for b in range(s+1):
            for c in range(s+1):
                if a + b + c <= s and a * b * c <= t:
                    ans += 1
    print(ans)

=======
Suggestion 2

def getNums(s, t):
    count = 0
    for i in range(s+1):
        for j in range(s+1):
            for k in range(s+1):
                if i+j+k <= s and i*j*k <= t:
                    count += 1
    return count

=======
Suggestion 3

def main():
    S, T = map(int, input().split())
    count = 0
    for a in range(S + 1):
        for b in range(S + 1):
            for c in range(S + 1):
                if a + b + c <= S and a * b * c <= T:
                    count += 1
    print(count)

=======
Suggestion 4

def solve(s, t):
    count = 0
    for a in range(s+1):
        for b in range(s+1):
            for c in range(s+1):
                if a+b+c <= s and a*b*c <= t:
                    count += 1
    return count

=======
Suggestion 5

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
Suggestion 6

def solve():
    S, T = map(int, input().split())
    ans = 0
    for a in range(S+1):
        for b in range(S+1):
            for c in range(S+1):
                if a + b + c <= S and a * b * c <= T:
                    ans += 1
    print(ans)

=======
Suggestion 7

def problem214_b():
    s,t = map(int,input().split())
    print(s,t)
    ans = 0
    for a in range(s+1):
        for b in range(s+1):
            for c in range(s+1):
                if a+b+c <= s and a*b*c <= t:
                    ans += 1
    print(ans)

problem214_b()
