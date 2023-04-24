Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

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
Suggestion 2

def main():
    S, T = map(int, input().split())
    count = 0
    for a in range(S+1):
        for b in range(S+1):
            for c in range(S+1):
                if a+b+c <= S and a*b*c <= T:
                    count += 1
    print(count)

=======
Suggestion 3

def main():
    S, T = map(int, input().split())
    ans = 0
    for a in range(S+1):
        for b in range(S+1-a):
            c = S - a - b
            if a * b * c <= T:
                ans += 1
    print(ans)
    return

=======
Suggestion 4

def main():
    S, T = map(int, input().split())
    count = 0
    for a in range(S + 1):
        for b in range(S + 1 - a):
            c = S - a - b
            if a * b * c <= T:
                count += 1
    print(count)

=======
Suggestion 5

def main():
    S, T = map(int, input().split())
    cnt = 0
    for a in range(S+1):
        for b in range(S-a+1):
            for c in range(S-a-b+1):
                if a*b*c <= T:
                    cnt += 1
    print(cnt)

=======
Suggestion 6

def main():
    S, T = map(int, input().split())
    print(sum(1 for a in range(S+1) for b in range(S+1) for c in range(S+1) if a+b+c <= S and a*b*c <= T))
