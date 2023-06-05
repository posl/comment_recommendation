Synthesizing 10/10 solutions

=======
Suggestion 1

def countTriplets(s):
    # Complete this function
    total = 0
    for i in range(len(s)-2):
        for j in range(i+1,len(s)-1):
            for k in range(j+1,len(s)):
                if s[i] != s[j] and s[i] != s[k] and s[j] != s[k] and j-i != k-j:
                    total += 1
    return total

=======
Suggestion 2

def findNumOfTriplet(s):
    N = len(s)
    ans = 0
    for i in range(N):
        for j in range(i+1,N):
            for k in range(j+1,N):
                if s[i] != s[j] and s[i] != s[k] and s[j] != s[k] and j - i != k - j:
                    ans += 1
    return ans

=======
Suggestion 3

def main():
    n = int(input())
    s = input()
    r = s.count('R')
    g = s.count('G')
    b = s.count('B')
    ans = r * g * b
    for i in range(n):
        for j in range(i+1,n):
            k = 2*j - i
            if k >= n:
                continue
            if s[i] != s[j] and s[j] != s[k] and s[k] != s[i]:
                ans -= 1
    print(ans)

=======
Suggestion 4

def main():
    n = int(input())
    s = input()
    r = s.count('R')
    g = s.count('G')
    b = s.count('B')
    ans = 0
    for i in range(n):
        for j in range(i+1, n):
            k = j + (j - i)
            if k >= n:
                continue
            if s[i] != s[j] and s[j] != s[k] and s[k] != s[i]:
                ans += 1
    print(r * g * b - ans)

=======
Suggestion 5

def solve():
    N = int(input())
    S = input()
    R = S.count("R")
    G = S.count("G")
    B = S.count("B")
    ans = R * G * B
    for d in range(N):
        for i in range(N):
            j = i + d
            k = j + d
            if k >= N:
                break
            if S[i] != S[j] and S[i] != S[k] and S[j] != S[k]:
                ans -= 1
    print(ans)

=======
Suggestion 6

def solve(n,s):
    #print(n,s)
    cnt = 0
    for i in range(0,n):
        for j in range(i+1,n):
            k = j + (j - i)
            if k >= n:
                break
            #print(i,j,k)
            if s[i] != s[j] and s[i] != s[k] and s[j] != s[k]:
                cnt += 1
    return cnt

=======
Suggestion 7

def find_3tuples(string):
    N = len(string)
    count = 0
    for i in range(N-2):
        for j in range(i+1, N-1):
            for k in range(j+1, N):
                if string[i] != string[j] and string[i] != string[k] and string[j] != string[k]:
                    if (j-i) != (k-j):
                        count += 1
    return count

=======
Suggestion 8

def main():
    N = int(input())
    S = input()
    rnum = S.count("R")
    gnum = S.count("G")
    bnum = S.count("B")
    count = 0
    for i in range(N-2):
        for j in range(i+1,N-1):
            if S[i] == S[j]:
                continue
            k = 2*j - i
            if k >= N:
                continue
            if S[i] == S[k] or S[j] == S[k]:
                continue
            count += 1
    print(rnum*gnum*bnum - count)

=======
Suggestion 9

def main():
    n = int(input())
    s = input()
    r = s.count('R')
    g = s.count('G')
    b = s.count('B')
    ans = r * g * b
    for i in range(n):
        for j in range(i + 1, n):
            k = 2 * j - i
            if k < n and s[i] != s[j] and s[j] != s[k] and s[k] != s[i]:
                ans -= 1
    print(ans)

=======
Suggestion 10

def find_rgb(s):
    rgb = []
    for i in range(len(s)):
        if s[i] == 'R':
            rgb.append([i, 0])
        elif s[i] == 'G':
            rgb.append([i, 1])
        else:
            rgb.append([i, 2])
    return rgb
