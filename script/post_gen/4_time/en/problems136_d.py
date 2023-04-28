Synthesizing 10/10 solutions (Duplicates hidden)

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
            ans[i] += cnt // 2
            ans[i-1] += (cnt + 1) // 2
            cnt = 0
    cnt = 0
    for i in range(N-1, -1, -1):
        if S[i] == 'L':
            cnt += 1
        else:
            ans[i] += cnt // 2
            ans[i+1] += (cnt + 1) // 2
            cnt = 0
    print(*ans)

=======
Suggestion 2

def main():
    S = input()
    N = len(S)
    ans = [0] * N
    cnt = 0
    for i in range(N):
        if S[i] == 'R':
            cnt += 1
        else:
            ans[i] += cnt // 2
            ans[i-1] += (cnt + 1) // 2
            cnt = 0
    cnt = 0
    for i in range(N-1, -1, -1):
        if S[i] == 'L':
            cnt += 1
        else:
            ans[i] += cnt // 2
            ans[i+1] += (cnt + 1) // 2
            cnt = 0
    print(' '.join(map(str, ans)))

=======
Suggestion 3

def main():
    s = input()
    n = len(s)
    ans = [0] * n
    for i in range(n):
        if s[i] == "R":
            ans[i+1] += 1
        else:
            ans[i] += 1
    print(*ans)

=======
Suggestion 4

def main():
    s = input()
    n = len(s)
    ans = [0 for _ in range(n)]
    r = 0
    l = 0
    for i in range(n):
        if s[i] == 'R':
            r += 1
        else:
            l += 1
        if s[i] == 'R' and s[i+1] == 'L':
            ans[i+1] += r//2 + r%2
            ans[i] += r//2
            r = 0
        elif s[i] == 'L' and s[i+1] == 'R':
            ans[i-1] += l//2
            ans[i] += l//2 + l%2
            l = 0
    print(*ans)

=======
Suggestion 5

def main():
    s = input()
    l = len(s)
    ans = [0] * l
    r = 0
    l = 0
    for i in range(len(s)):
        if s[i] == 'R':
            r += 1
        else:
            l += 1
            ans[i] += l // 2
            ans[i - 1] += l - l // 2
            l = 0
    l = 0
    for i in range(len(s) - 1, -1, -1):
        if s[i] == 'L':
            l += 1
        else:
            ans[i] += l // 2
            ans[i + 1] += l - l // 2
            l = 0
    print(' '.join(map(str, ans)))

=======
Suggestion 6

def main():
    S = input()
    N = len(S)
    result = [0]*N
    R = 0
    L = 0
    for i in range(N):
        if S[i] == 'R':
            R += 1
        else:
            L += 1
        if S[i] == 'R' and S[i+1] == 'L':
            result[i] += R//2
            result[i+1] += (R+1)//2
            R = 0
        if S[i] == 'L' and S[i+1] == 'R':
            result[i-1] += (L+1)//2
            result[i] += L//2
            L = 0
    print(*result)

=======
Suggestion 7

def main():
    s = input()
    n = len(s)
    ans = [0] * n

    i = 0
    while i < n:
        if s[i] == "R":
            j = i + 1
            while j < n and s[j] == "R":
                j += 1
            x = j - i
            if x % 2 == 0:
                ans[j - 1] += x // 2
                ans[j] += x // 2
            else:
                ans[j - 1] += x // 2 + 1
                ans[j] += x // 2
            i = j
        else:
            j = i - 1
            while j >= 0 and s[j] == "L":
                j -= 1
            x = i - j
            if x % 2 == 0:
                ans[j] += x // 2
                ans[j + 1] += x // 2
            else:
                ans[j] += x // 2
                ans[j + 1] += x // 2 + 1
            i = j
    print(" ".join(map(str, ans)))

=======
Suggestion 8

def main():
    s = input()
    result = [0] * len(s)
    r_count = 0
    l_count = 0
    r_index = []
    l_index = []
    for i in range(len(s)):
        if s[i] == 'R':
            r_count += 1
            r_index.append(i)
        else:
            l_count += 1
            l_index.append(i)
    for i in range(len(r_index)):
        if i == len(r_index)-1:
            result[r_index[i]] += r_count // 2 + r_count % 2
            result[r_index[i]+1] += r_count // 2
        else:
            result[r_index[i]] += r_count // 2
            result[r_index[i]+1] += r_count // 2 + r_count % 2
    for i in range(len(l_index)):
        if i == 0:
            result[l_index[i]] += l_count // 2 + l_count % 2
            result[l_index[i]-1] += l_count // 2
        else:
            result[l_index[i]] += l_count // 2
            result[l_index[i]-1] += l_count // 2 + l_count % 2
    print(*result)

=======
Suggestion 9

def main():
    s = input()
    l = len(s)
    ans = [0] * l
    for i in range(1, l):
        if s[i] == "L":
            ans[i - 1] += 1
        else:
            ans[i] += 1
    print(*ans)
