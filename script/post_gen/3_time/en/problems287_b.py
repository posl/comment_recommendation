Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, M = map(int, input().split())
    S = [input() for _ in range(N)]
    T = [input() for _ in range(M)]
    ans = 0
    for i in range(N):
        for j in range(M):
            if S[i][-3:] == T[j]:
                ans += 1
                break
    print(ans)

=======
Suggestion 2

def main():
    n, m = map(int, input().split())
    s = [input() for _ in range(n)]
    t = [input() for _ in range(m)]
    ans = 0
    for i in range(n):
        for j in range(m):
            if s[i][-3:] == t[j]:
                ans += 1
    print(ans)

=======
Suggestion 3

def main():
    N, M = map(int, input().split())
    S = [input() for i in range(N)]
    T = [input() for i in range(M)]
    ans = 0
    for i in range(N):
        for j in range(M):
            if S[i][3:] == T[j]:
                ans += 1
                break
    print(ans)

=======
Suggestion 4

def solve():
    N, M = map(int, input().split())
    S = [input() for _ in range(N)]
    T = [input() for _ in range(M)]
    ans = 0
    for i in range(N):
        for j in range(M):
            if S[i][-3:] == T[j]:
                ans += 1
                break
    print(ans)

=======
Suggestion 5

def main():
    n, m = map(int, input().split())
    s = [input()[-3:] for i in range(n)]
    t = [input() for i in range(m)]
    ans = 0
    for i in s:
        if i in t:
            ans += 1
    print(ans)

=======
Suggestion 6

def main():
    n, m = [int(i) for i in input().split()]
    s = [input() for i in range(n)]
    t = [input() for i in range(m)]
    ans = 0
    for i in s:
        for j in t:
            if i[-3:] == j:
                ans += 1
                break
    print(ans)

=======
Suggestion 7

def main():
    N, M = map(int, input().split())
    S = [input() for _ in range(N)]
    T = [input() for _ in range(M)]
    print(sum(s[3:] in T for s in S))

=======
Suggestion 8

def main():
    n, m = map(int, input().split())
    s = [input() for i in range(n)]
    t = [input() for i in range(m)]
    for i in range(n):
        for j in range(m):
            if s[i][-3:] == t[j]:
                print(s[i])

main()

I am trying to find the number of strings among S_1, S_2, ..., S_N whose last three characters coincide with one or more of T_1, T_2, ..., T_M.

I am getting the wrong answer for Sample Input 2 and Sample Input 3.

I have tried this code:

n, m = map(int, input().split())
s = [input() for i in range(n)]
t = [input() for i in range(m)]
count = 0
for i in range(n):
    for j in range(m):
        if s[i][-3:] == t[j]:
            count += 1
print(count)

I am getting the correct answer for Sample Input 1.

I am not sure why I am getting the wrong answer for Sample Input 2 and Sample Input 3.

I have tried this code:

n, m = map(int, input().split())
s = [input() for i in range(n)]
t = [input() for i in range(m)]
count = 0
for i in range(n):
    for j in range(m):
        if s[i][-3:] == t[j]:
            count += 1
print(count)

I am getting the correct answer for Sample Input 1.

I am not sure why I am getting the wrong answer for Sample Input 2 and Sample Input 3.

I have tried this code:

n, m = map(int, input().split())
s = [input() for i in range(n)]
t = [input() for i in range(m)]
count = 0
for i in range(n):
    for j in range(m):
        if s[i][-3:] == t[j]:
            count += 1
print(count)

I am getting the correct answer for Sample Input 1.

I am not sure why I am getting the wrong answer for Sample Input 2 and Sample Input 3.

I have tried this code:

n, m = map(int, input().split())
s = [input() for i in range(n)]
t = [input() for i in range

=======
Suggestion 9

def main():
    # Read input
    N, M = [int(x) for x in input().split()]
    S = [input() for i in range(N)]
    T = [input() for i in range(M)]

    # Count number of strings of S that end with a string of T
    count = 0
    for s in S:
        for t in T:
            if s[-3:] == t:
                count += 1
                break

    # Output result
    print(count)

=======
Suggestion 10

def main():
    # Read input data
    N, M = map(int, input().split())
    S = [input() for _ in range(N)]
    T = [input() for _ in range(M)]

    # Count the number of strings among S whose last three characters coincide with one or more of T
    count = 0
    for s in S:
        for t in T:
            if s[-3:] == t:
                count += 1
                break

    # Print the answer
    print(count)
