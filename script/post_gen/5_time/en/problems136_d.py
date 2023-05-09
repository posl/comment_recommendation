Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    s = input()
    n = len(s)
    ans = [0]*n
    l = 0
    r = 0
    for i in range(n):
        if s[i] == 'R':
            r += 1
        else:
            l += 1
        if l > 0 and r > 0:
            if s[i] == 'R':
                ans[i] += l//2
                ans[i-1] += l - l//2
                l = 0
            else:
                ans[i] += r//2
                ans[i-1] += r - r//2
                r = 0
    print(' '.join(map(str, ans)))

=======
Suggestion 2

def main():
    S = input()
    N = len(S)
    result = [0] * N
    i = 0
    while i < N:
        if S[i] == 'R':
            j = i
            while j < N and S[j] == 'R':
                j += 1
            result[j-1] += (j - i) // 2 + (i - j + 1) // 2
            result[j] += (j - i + 1) // 2 + (i - j) // 2
            i = j
        else:
            j = i
            while j < N and S[j] == 'L':
                j += 1
            result[j-1] += (j - i) // 2 + (i - j + 1) // 2
            result[j] += (j - i + 1) // 2 + (i - j) // 2
            i = j
    print(' '.join(map(str, result)))

=======
Suggestion 3

def main():
    s = input()
    n = len(s)
    ans = [0] * n
    for i in range(n):
        if s[i] == 'L':
            if i % 2 == 0:
                ans[i - 1] += 1
            else:
                ans[i + 1] += 1
        else:
            if i % 2 == 0:
                ans[i + 1] += 1
            else:
                ans[i - 1] += 1
    print(*ans)

=======
Suggestion 4

def solve(s):
    n = len(s)
    ans = [0] * n
    for i in range(n):
        if s[i] == 'R':
            if i % 2 == 0:
                ans[i+1] += 1
            else:
                ans[i-1] += 1
        else:
            if i % 2 == 0:
                ans[i-1] += 1
            else:
                ans[i+1] += 1
    return ans

=======
Suggestion 5

def main():
    s = input()
    n = len(s)
    a = [0]*n
    l, r = 0, 0
    for i in range(n):
        if s[i] == 'R':
            r += 1
        else:
            l += 1
            a[i] += l//2
            a[i-1] += (l+1)//2
            l = 0
    l, r = 0, 0
    for i in range(n-1, -1, -1):
        if s[i] == 'L':
            l += 1
        else:
            r += 1
            a[i] += r//2
            a[i+1] += (r+1)//2
            r = 0
    print(*a)

main()

=======
Suggestion 6

def main():
    s = input()
    n = len(s)
    a = [0]*n
    i = 0
    while i < n:
        j = i
        while j < n and s[j] == 'R':
            j += 1
        k = j
        while k < n and s[k] == 'L':
            k += 1
        if (j-i) % 2 == 0:
            a[j-1] += (j-i)//2
            a[j] += (j-i)//2
        else:
            if (j-i) % 2 == 1:
                a[j-1] += (j-i)//2 + 1
                a[j] += (j-i)//2
            else:
                a[j-1] += (j-i)//2
                a[j] += (j-i)//2 + 1
        i = k
    print(*a)

=======
Suggestion 7

def main():
    S = input()
    N = len(S)
    ans = [0 for i in range(N)]
    R = 0
    L = 0
    flag = 0
    for i in range(N):
        if S[i] == "R":
            if flag == 1:
                ans[i-1] = R//2 + L//2 + R%2
                ans[i] = R//2 + L//2 + L%2
                R = 0
                L = 0
                flag = 0
            R += 1
        else:
            L += 1
            flag = 1
    ans[N-1] = R//2 + L//2 + R%2
    ans[0] = R//2 + L//2 + L%2
    print(" ".join(map(str, ans)))

=======
Suggestion 8

def main():
    # input
    s = input()

    # compute

    # output
    print()

=======
Suggestion 9

def main():
    s = input()
    s = s.replace('RL', 'R L')
    s = list(s.split())
    ans = []
    for i in range(len(s)):
        if i == 0:
            ans.append(0)
        elif i == len(s)-1:
            ans.append(0)
        else:
            if len(s[i]) % 2 == 0:
                ans.append(len(s[i])//2)
                ans.append(len(s[i])//2)
            else:
                if s[i][0] == 'R':
                    ans.append(len(s[i])//2)
                    ans.append(len(s[i])//2+1)
                else:
                    ans.append(len(s[i])//2+1)
                    ans.append(len(s[i])//2)
    print(' '.join(map(str, ans)))

=======
Suggestion 10

def main():
    S = input()
    N = len(S)
    A = [0] * N

    #print(S)
    #print(N)
    #print(A)

    #print(S[0])
    #print(S[1])

    #print(S[0] == "R")
    #print(S[1] == "R")

    #print(S[0] == "L")
    #print(S[1] == "L")

    #print(S[0] == "R" and S[1] == "R")
    #print(S[0] == "R" and S[1] == "L")
    #print(S[0] == "L" and S[1] == "R")
    #print(S[0] == "L" and S[1] == "L")

    if S[0] == "R" and S[1] == "R":
        A[0] += 1
    if S[0] == "R" and S[1] == "L":
        A[0] += 1
        A[1] += 1
    if S[0] == "L" and S[1] == "R":
        A[0] += 1
        A[1] += 1
    if S[0] == "L" and S[1] == "L":
        A[1] += 1

    #print(A)

    for i in range(1, N - 1):
        if S[i] == "R" and S[i + 1] == "R":
            A[i] += 1
        if S[i] == "R" and S[i + 1] == "L":
            A[i] += 1
            A[i + 1] += 1
        if S[i] == "L" and S[i + 1] == "R":
            A[i] += 1
            A[i + 1] += 1
        if S[i] == "L" and S[i + 1] == "L":
            A[i + 1] += 1

    #print(A)

    if S[N - 2] == "R" and S[N - 1] == "R":
        A[N - 2] += 1
