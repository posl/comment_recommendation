Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    S = input()
    r = S.count("R")
    g = S.count("G")
    b = S.count("B")
    ans = r * g * b
    for i in range(N):
        for j in range(i+1, N):
            k = j + (j - i)
            if k < N:
                if S[i] != S[j] and S[i] != S[k] and S[j] != S[k]:
                    ans -= 1
    print(ans)

main()

=======
Suggestion 2

def check(s):
    count = 0
    for i in range(len(s)):
        for j in range(i+1,len(s)):
            k = 2*j-i
            if k < len(s):
                if s[i] != s[j] and s[j] != s[k] and s[k] != s[i]:
                    if j-i != k-j:
                        count += 1
    return count

n = int(input())
s = input()
print(check(s))

=======
Suggestion 3

def solve():
    N = int(input())
    S = input()

    # R, G, B の個数を数える
    R = S.count('R')
    G = S.count('G')
    B = S.count('B')

    # まずは、同じ文字の組を数える
    ans = R * G * B

    # 以下、異なる文字の組を数える
    # i, j, k を全探索する
    for i in range(N):
        for j in range(i + 1, N):
            k = 2 * j - i
            if k >= N:
                continue
            if S[i] != S[j] and S[j] != S[k] and S[k] != S[i]:
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
    ans = r * g * b
    for i in range(n):
        for j in range(i+1, n):
            k = j + (j - i)
            if k < n:
                if s[i] != s[j] and s[i] != s[k] and s[j] != s[k]:
                    ans -= 1
    print(ans)

=======
Suggestion 5

def main():
    N = int(input())
    S = input()
    R = S.count("R")
    G = S.count("G")
    B = S.count("B")
    cnt = 0
    for i in range(N):
        for j in range(i+1, N):
            k = 2*j - i
            if k >= N:
                continue
            if S[i] != S[j] and S[j] != S[k] and S[k] != S[i]:
                cnt += 1
    print(R*G*B - cnt)

=======
Suggestion 6

def main():
    N = int(input())
    S = input()
    count = 0
    for i in range(N):
        for j in range(i+1, N):
            if (2*j-i) < N:
                if S[i] != S[j] and S[j] != S[2*j-i] and S[2*j-i] != S[i]:
                    count += 1
    print(count)

=======
Suggestion 7

def check(s, i, j, k):
  if (s[i] != s[j]) and (s[i] != s[k]) and (s[j] != s[k]):
    if (j - i) != (k - j):
      return True
  return False

n = int(input())
s = input()

r = s.count('R')
g = s.count('G')
b = s.count('B')

result = r * g * b

for i in range(n):
  for j in range(i+1, n):
    k = j + (j - i)
    if k < n:
      if check(s, i, j, k):
        result -= 1

print(result)

=======
Suggestion 8

def solve():
    N = int(input())
    S = input()
    R = S.count("R")
    G = S.count("G")
    B = S.count("B")
    ans = R * G * B
    for i in range(N):
        for j in range(i+1,N):
            k = 2*j - i
            if k >= N:
                continue
            if S[i] != S[j] and S[j] != S[k] and S[k] != S[i]:
                ans -= 1
    print(ans)
solve()

=======
Suggestion 9

def main():
    n = int(input())
    s = input()
    r = s.count('R')
    g = s.count('G')
    b = s.count('B')
    cnt = 0
    for i in range(n):
        for j in range(i+1,n):
            k = 2*j-i
            if k >= n:
                continue
            if s[i] != s[j] and s[j] != s[k] and s[i] != s[k]:
                cnt += 1
    print(r*g*b - cnt)
main()

=======
Suggestion 10

def main():
    n = int(input())
    s = input()

    r = s.count('R')
    g = s.count('G')
    b = s.count('B')

    cnt = 0
    for i in range(n):
        for j in range(i+1, n):
            k = j + (j - i)
            if k < n:
                if s[i] != s[j] and s[j] != s[k] and s[k] != s[i]:
                    cnt += 1

    print(r * g * b - cnt)

main()
