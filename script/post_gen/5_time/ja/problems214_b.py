Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    s,t = map(int,input().split())
    ans = 0
    for a in range(s+1):
        for b in range(s+1):
            for c in range(s+1):
                if a+b+c <= s and a*b*c <= t:
                    ans += 1
    print(ans)

=======
Suggestion 2

def main():
    s,t = map(int,input().split())
    count = 0
    for i in range(s+1):
        for j in range(s+1):
            for k in range(s+1):
                if i+j+k <= s and i*j*k <= t:
                    count += 1
    print(count)

=======
Suggestion 3

def main():
    s,t = map(int,input().split())
    ans = 0
    for a in range(0,s+1):
        for b in range(0,s+1):
            for c in range(0,s+1):
                if a+b+c <= s and a*b*c <= t:
                    ans += 1
    print(ans)

=======
Suggestion 4

def main():
    s, t = map(int, input().split())
    ans = 0
    for i in range(s+1):
        for j in range(s+1):
            for k in range(s+1):
                if i + j + k <= s and i * j * k <= t:
                    ans += 1
    print(ans)

=======
Suggestion 5

def problem214_b():
    s,t = input().split()
    s = int(s)
    t = int(t)
    count = 0
    for a in range(s+1):
        for b in range(s+1):
            for c in range(s+1):
                if a+b+c <= s and a*b*c <= t:
                    count += 1
    print(count)
