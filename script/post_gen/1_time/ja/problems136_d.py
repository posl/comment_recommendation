Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    S = input()
    N = len(S)
    ans = [0] * N
    cnt = 0
    for i in range(N):
        if S[i] == 'R':
            cnt += 1
        else:
            ans[i] += (cnt + 1) // 2
            ans[i - 1] += cnt // 2
            cnt = 0
    print(*ans)

=======
Suggestion 2

def main():
    S = input()
    N = len(S)
    L = [0] * N
    R = [0] * N
    for i in range(N):
        if S[i] == 'R':
            R[i] = 1
        else:
            L[i] = 1
    for i in range(N):
        if i == N - 1:
            print(L[i], end = '')
        else:
            print(L[i], end = ' ')
    print()
    for i in range(N - 1):
        if i == N - 2:
            print(R[i], end = '')
        else:
            print(R[i], end = ' ')
    print()
    for i in range(N - 2, -1, -1):
        if i == 0:
            print(L[i], end = '')
        else:
            print(L[i], end = ' ')
    print()
    for i in range(N - 1):
        if i == N - 2:
            print(R[i], end = '')
        else:
            print(R[i], end = ' ')
    print()
    for i in range(N):
        if i == N - 1:
            print(L[i], end = '')
        else:
            print(L[i], end = ' ')
    print()

=======
Suggestion 3

def main():
    s = input()
    n = len(s)
    ans = [0] * n
    cnt = 0
    for i in range(n):
        if s[i] == 'R':
            cnt += 1
        else:
            ans[i] += cnt // 2
            ans[i-1] += (cnt + 1) // 2
            cnt = 0
    cnt = 0
    for i in range(n-1, -1, -1):
        if s[i] == 'L':
            cnt += 1
        else:
            ans[i] += cnt // 2
            ans[i+1] += (cnt + 1) // 2
            cnt = 0
    print(*ans)

=======
Suggestion 4

def main():
    S = input()
    N = len(S)
    ans = [0] * N
    for i in range(N):
        if S[i] == "R":
            ans[i + 1] += 1
        else:
            ans[i - 1] += 1
    for i in range(N):
        if ans[i] % 2 == 1:
            if S[i] == "R":
                ans[i + 1] += 1
            else:
                ans[i - 1] += 1
    for i in range(N):
        print(ans[i] // 2, end = " ")
    print()

=======
Suggestion 5

def main():
    S = input()
    N = len(S)
    ans = [0] * N
    ans[0] = 1
    ans[-1] = 1
    for i in range(1, N - 1):
        if S[i] == 'L':
            ans[i] = ans[i - 1] + 1
        else:
            ans[i] = ans[i - 1] - 1
    for i in range(N - 2, 0, -1):
        if S[i] == 'R':
            ans[i] = ans[i + 1] + 1
        else:
            ans[i] = ans[i + 1] - 1
    print(*ans)

=======
Suggestion 6

def main():
    S = input()
    N = len(S)
    ans = [0] * N
    ans[0] = 1
    ans[N-1] = 1
    for i in range(1,N-1):
        if S[i-1] == "R":
            ans[i] += 1
        else:
            ans[i-1] += 1
    for i in range(N):
        print(ans[i],end=" ")

=======
Suggestion 7

def main():
    s = input()
    n = len(s)
    ans = [0] * n
    ans[0] = 1
    ans[n-1] = 1
    for i in range(1, n-1):
        if s[i] == "R":
            ans[i+1] += 1
        else:
            ans[i-1] += 1
    print(*ans)

=======
Suggestion 8

def main():
    S = input()
    N = len(S)
    ans = [0] * N
    i = 0
    while i < N:
        if S[i] == "R":
            j = i
            while j < N and S[j] == "R":
                j += 1
            if j - i == 1:
                ans[i] = 1
                i += 1
            else:
                ans[j-1] = (j - i) // 2
                ans[j] = (j - i) - ans[j-1]
                i = j + 1
        else:
            j = i
            while j < N and S[j] == "L":
                j += 1
            if j - i == 1:
                ans[i] = 1
                i += 1
            else:
                ans[i-1] = (j - i) // 2
                ans[i] = (j - i) - ans[i-1]
                i = j + 1
    print(*ans)

=======
Suggestion 9

def main():
    s = input()
    n = len(s)
    ans = [0] * n
    ans[0] = 1
    ans[-1] = 1
    for i in range(n):
        if s[i] == 'R':
            ans[i+1] += ans[i]
            ans[i] = 0
        else:
            ans[i-1] += ans[i]
            ans[i] = 0
    print(*ans)

=======
Suggestion 10

def main():
    s = input()
    n = len(s)
    l = [1] * n
    for i in range(n):
        if s[i] == 'L':
            l[i-1] += l[i]
            l[i] = 0
    for i in range(n-1, -1, -1):
        if s[i] == 'R':
            l[i+1] += l[i]
            l[i] = 0
    print(*l)
