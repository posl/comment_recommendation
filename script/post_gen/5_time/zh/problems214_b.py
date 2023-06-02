Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    S,T = map(int,input().split())
    cnt = 0
    for a in range(S+1):
        for b in range(S+1):
            for c in range(S+1):
                if a+b+c <= S and a*b*c <= T:
                    cnt += 1
    print(cnt)

=======
Suggestion 2

def main():
    S,T = map(int,input().split())
    cnt = 0
    for a in range(S+1):
        for b in range(S+1):
            for c in range(S+1):
                if a+b+c <= S and a*b*c <= T:
                    cnt += 1
    print(cnt)
main()

=======
Suggestion 3

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
Suggestion 4

def main():
    s, t = map(int, input().split())
    count = 0
    for a in range(s+1):
        for b in range(s+1):
            for c in range(s+1):
                if a + b + c <= s and a * b * c <= t:
                    count += 1
    print(count)

=======
Suggestion 5

def solve(s, t):
    count = 0
    for a in range(s + 1):
        for b in range(s + 1):
            for c in range(s + 1):
                if a + b + c <= s and a * b * c <= t:
                    count += 1
    return count

=======
Suggestion 6

def main():
    #print("请输入两个整数，空格隔开：")
    #s,t = input().split()
    #s,t = 1,0
    #s,t = 2,5
    #s,t = 10,10
    s,t = 30,100
    s,t = int(s),int(t)
    count = 0
    for a in range(s+1):
        for b in range(s+1):
            for c in range(s+1):
                if a+b+c <= s and a*b*c <= t:
                    count += 1
                    #print(a,b,c)
    print(count)

=======
Suggestion 7

def main():
    s, t = map(int, input().split())
    count = 0
    for a in range(0, s + 1):
        for b in range(0, s + 1):
            for c in range(0, s + 1):
                if a + b + c <= s and a * b * c <= t:
                    count += 1
    print(count)
