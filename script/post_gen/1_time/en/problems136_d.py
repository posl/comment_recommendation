Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    S = input()
    N = len(S)
    ans = [0] * N
    L = 0
    R = 0
    for i in range(N):
        if S[i] == 'L':
            L += 1
        else:
            R += 1
        if S[i] == 'R' and S[i+1] == 'L':
            ans[i] = (L+1)//2 + R//2
            ans[i+1] = L//2 + (R+1)//2
            L = 0
            R = 0
    print(*ans)

=======
Suggestion 2

def main():
    S = input()
    N = len(S)
    count = [0] * N
    for i in range(N):
        if S[i] == 'R':
            count[i] += 1
        else:
            count[i-1] += 1
    for i in range(N-1, -1, -1):
        if S[i] == 'L':
            count[i] += 1
        else:
            count[i+1] += 1
    print(' '.join(map(str, count)))

=======
Suggestion 3

def main():
    S = input()
    N = len(S)
    ans = [0] * N
    ans[0] = 1
    ans[-1] = 1
    i = 0
    while i < N - 1:
        if S[i] == 'R' and S[i + 1] == 'L':
            j = i + 1
            while j < N - 1 and S[j] == 'L' and S[j + 1] == 'L':
                j += 1
            ans[i] = ans[i] + (j - i + 1) // 2
            ans[i + 1] = ans[i + 1] + (j - i + 1) // 2
            if (j - i + 1) % 2 == 1:
                ans[i + 1] += 1
            i = j
        else:
            i += 1
    i = N - 1
    while i > 0:
        if S[i] == 'L' and S[i - 1] == 'R':
            j = i - 1
            while j > 0 and S[j] == 'R' and S[j - 1] == 'R':
                j -= 1
            ans[i] = ans[i] + (i - j + 1) // 2
            ans[i - 1] = ans[i - 1] + (i - j + 1) // 2
            if (i - j + 1) % 2 == 1:
                ans[i - 1] += 1
            i = j
        else:
            i -= 1
    print(*ans)

=======
Suggestion 4

def main():
    S = input()
    N = len(S)
    count = [0] * N
    count[0] = 1
    count[-1] = 1
    for i in range(1, N - 1):
        if S[i] == 'R':
            count[i] = count[i - 1] + 1
        else:
            count[i] = count[i - 1] - 1
    for i in range(N - 2, 0, -1):
        if S[i] == 'L':
            count[i] = count[i + 1] + 1
        else:
            count[i] = count[i + 1] - 1
    print(*count)

=======
Suggestion 5

def main():
    S = input()
    N = len(S)
    ans = [1] * N
    l = 0
    r = 0
    for i in range(N):
        if S[i] == 'L':
            l = i
        else:
            r = i
        if l != r:
            ans[l] += ans[r]
            ans[r] = 0
    print(*ans)

=======
Suggestion 6

def solve():
    S = input()
    N = len(S)
    ans = [1] * N
    cnt = 0
    for i in range(N - 1):
        if S[i] == "R" and S[i + 1] == "L":
            cnt += 1
            ans[i] += cnt // 2
            ans[i + 1] += cnt // 2
            if cnt % 2:
                ans[i] += 1
            cnt = 0
        elif S[i] == "L" and S[i + 1] == "R":
            cnt = 1
        else:
            cnt += 1
    print(*ans)

=======
Suggestion 7

def main():
    S = input()
    N = len(S)
    ans = [0] * N
    child = 0
    for i in range(N):
        if S[i] == "R":
            child += 1
        else:
            ans[i] = child // 2
            ans[i - 1] = child - ans[i]
            child = 0
    ans[0] = child
    print(" ".join(map(str, ans)))

=======
Suggestion 8

def main():
    S = input()
    L = len(S)
    ans = [0] * L
    R = 0
    L = 0
    for i in range(L):
        if S[i] == 'R':
            R += 1
        else:
            L += 1
            ans[i] = R // 2
            ans[i - 1] = (R + 1) // 2
            R = 0
    ans[0] = R
    ans[-1] = L
    print(*ans)

=======
Suggestion 9

def main():
    S = input()
    L = len(S)
    ans = [0] * L
    i = 0
    while i < L:
        if S[i] == 'R':
            cnt = 0
            while i < L and S[i] == 'R':
                cnt += 1
                i += 1
            if cnt % 2 == 0:
                ans[i-1] += cnt // 2
                ans[i] += cnt // 2
            else:
                ans[i-1] += cnt // 2 + 1
                ans[i] += cnt // 2
        else:
            cnt = 0
            while i < L and S[i] == 'L':
                cnt += 1
                i += 1
            if cnt % 2 == 0:
                ans[i-1] += cnt // 2
                ans[i-2] += cnt // 2
            else:
                ans[i-1] += cnt // 2
                ans[i-2] += cnt // 2 + 1
    print(*ans)

=======
Suggestion 10

def main():
    S = input()
    N = len(S)
    ans = [0] * N
    #Lが現れるときまでのRの数を数える
    cnt = 0
    for i, s in enumerate(S):
        if s == 'R':
            cnt += 1
        else:
            ans[i] += (cnt + 1) // 2
            ans[i - 1] += cnt // 2
            cnt = 0
    #Rが現れるときまでのLの数を数える
    cnt = 0
    for i in range(N - 1, -1, -1):
        if S[i] == 'L':
            cnt += 1
        else:
            ans[i] += (cnt + 1) // 2
            ans[i + 1] += cnt // 2
            cnt = 0
    print(' '.join(map(str, ans)))

main()
