Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, K = map(int, input().split())
    S = input()
    happy = 0
    for i in range(N-1):
        if S[i] == S[i+1]:
            happy += 1
    print(min(N-1, happy+2*K))

=======
Suggestion 2

def main():
    N, K = map(int, input().split())
    S = input()
    count = 0
    for i in range(N-1):
        if S[i] == S[i+1]:
            count += 1
    if count > K:
        print(N - 1 - (count - K))
    else:
        print(N - 1)

=======
Suggestion 3

def main():
    N, K = map(int, input().split())
    S = input()
    ans = 0
    for i in range(N-1):
        if S[i] == S[i+1]:
            ans += 1
    ans += min(2*K, ans + 2*K)
    print(min(ans, N-1))

=======
Suggestion 4

def main():
    N, K = map(int, input().split())
    S = input()
    ans = 0
    for i in range(N-1):
        if S[i] == S[i+1]:
            ans += 1
    print(min(ans+2*K, N-1))

=======
Suggestion 5

def main():
    N, K = map(int, input().split())
    S = input()

    count = 0
    for i in range(N-1):
        if S[i] == S[i+1]:
            count += 1

    print(min(N-1, count+2*K))

=======
Suggestion 6

def main():
    n, k = map(int, input().split())
    s = input()
    if n == 1:
        print(0)
        return
    if n == 2:
        if s[0] != s[1]:
            print(1)
        else:
            print(0)
        return
    if s[0] == s[-1]:
        count = 0
        for i in range(1, n):
            if s[i] != s[i-1]:
                count += 1
        print(min(n-1, count+2*k))
    else:
        count = 0
        for i in range(1, n):
            if s[i] != s[i-1]:
                count += 1
        print(min(n-1, count+2*k-1))

=======
Suggestion 7

def countHappyPeople(people):
    happyPeople = 0
    for i in range(len(people)-1):
        if people[i] == people[i+1]:
            happyPeople += 1
    return happyPeople

=======
Suggestion 8

def main():
    N, K = map(int, input().split())
    S = input()
    S = S + "R"
    count = 0
    for i in range(N):
        if S[i] == S[i+1]:
            count += 1
    print(min(N-1, count+2*K))

=======
Suggestion 9

def main():
    N, K = map(int, input().split())
    S = input()
    #print(N, K, S)
    happy = 0
    for n in range(1, N):
        if S[n-1] == S[n]:
            happy += 1
    print(min(N-1, happy+2*K))

=======
Suggestion 10

def main():
    n, k = map(int, input().split())
    s = input()
    s1 = s
    s2 = s[::-1]
    ans = 0
    for i in range(n-1):
        if s1[i] == s1[i+1]:
            ans += 1
        if s2[i] == s2[i+1]:
            ans += 1
    ans += min(ans//2+1, k)
    print(ans)
