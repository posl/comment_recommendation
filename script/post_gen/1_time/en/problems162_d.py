Synthesizing 10/10 solutions

=======
Suggestion 1

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
            if k >= n:
                continue
            if s[i] != s[j] and s[j] != s[k] and s[k] != s[i]:
                ans -= 1
    print(ans)

=======
Suggestion 2

def main():
    n = int(input())
    s = input()
    r = s.count('R')
    g = s.count('G')
    b = s.count('B')
    ans = r * g * b
    for i in range(n - 2):
        for j in range(i + 1, n - 1):
            k = 2 * j - i
            if k < n:
                if s[i] != s[j] and s[j] != s[k] and s[k] != s[i]:
                    ans -= 1
    print(ans)

main()

=======
Suggestion 3

def main():
    n = int(input())
    s = input()
    r = s.count('R')
    g = s.count('G')
    b = s.count('B')
    ans = r*g*b
    for i in range(n):
        for j in range(i+1, n):
            k = j + (j-i)
            if k >= n:
                break
            if s[i] != s[j] and s[i] != s[k] and s[j] != s[k]:
                ans -= 1
    print(ans)

=======
Suggestion 4

def main():
    N = int(input())
    S = input()
    R = S.count('R')
    G = S.count('G')
    B = S.count('B')
    ans = R*G*B
    for i in range(N-2):
        for j in range(i+1,N-1):
            if S[i] != S[j]:
                if 2*j-i < N:
                    if S[i] != S[2*j-i] and S[j] != S[2*j-i]:
                        ans -= 1
                if j+i < N and j+i < 2*j-i:
                    if S[i] != S[j+i] and S[j] != S[j+i]:
                        ans -= 1
                if j-i < N and j-i < 2*j-i:
                    if S[i] != S[j-i] and S[j] != S[j-i]:
                        ans -= 1
    print(ans)

main()

=======
Suggestion 5

def main():
    N = int(input())
    S = input()
    R = [0]*(N+1)
    G = [0]*(N+1)
    B = [0]*(N+1)
    for i in range(N):
        if S[i] == 'R':
            R[i+1] = R[i] + 1
            G[i+1] = G[i]
            B[i+1] = B[i]
        if S[i] == 'G':
            R[i+1] = R[i]
            G[i+1] = G[i] + 1
            B[i+1] = B[i]
        if S[i] == 'B':
            R[i+1] = R[i]
            G[i+1] = G[i]
            B[i+1] = B[i] + 1
    ans = 0
    for i in range(N-2):
        for j in range(i+1,N-1):
            if S[i] != S[j]:
                if j - i == (j - i)*2:
                    if S[j - i] != S[j]:
                        ans += 1
                else:
                    ans += 1
    print(ans)

=======
Suggestion 6

def main():
    n = int(input())
    s = input()
    r = s.count('R')
    g = s.count('G')
    b = s.count('B')
    ans = r*g*b

    for i in range(n):
        for j in range(i+1, n):
            k = j + (j-i)
            if k >= n:
                break
            if s[i] != s[j]:
                if s[i] != s[k]:
                    if s[j] != s[k]:
                        ans -= 1

    print(ans)

=======
Suggestion 7

def main():
    n = int(input())
    s = input()
    ans = 0
    for i in range(n-2):
        for j in range(i+1,n-1):
            if s[i] != s[j]:
                for k in range(j+1,n):
                    if s[i] != s[k] and s[j] != s[k] and j-i != k-j:
                        ans += 1
    print(ans)

=======
Suggestion 8

def main():
    N = int(input())
    S = input()
    ans = 0
    for i in range(N):
        for j in range(i+1, N):
            if S[i] == S[j]:
                continue
            for k in range(j+1, N):
                if S[i] == S[k] or S[j] == S[k]:
                    continue
                if j - i == k - j:
                    continue
                ans += 1
    print(ans)

=======
Suggestion 9

def main():
    n = int(input())
    s = input()
    r = s.count('R')
    g = s.count('G')
    b = s.count('B')
    print(r*g*b - sum(s[i] == s[j] == s[k] for i in range(n) for j in range(i+1, n) for k in range(j+1, n) if j-i != k-j))

=======
Suggestion 10

def main():
    N = int(input())
    S = input()

    # print(N)
    # print(S)

    # 1. AとBはR, G, Bのどれか
    # 2. AとBの距離は2以上である
    # 3. AとBは異なる文字である
    # 4. BとCはR, G, Bのどれか
    # 5. BとCの距離は2以上である
    # 6. BとCは異なる文字である
    # 7. AとCはR, G, Bのどれか
    # 8. AとCは異なる文字である
    # 9. BとCは異なる文字である
    # 10. AとBの距離はBとCの距離と異なる
    # 11. AとCの距離はBとCの距離と異なる

    # 1. AとBはR, G, Bのどれか
    # 2. AとBの距離は2以上である
    # 3. AとBは異なる文字である
    # 4. BとCはR, G, Bのどれか
    # 5. BとCの距離は2以上である
    # 6. BとCは異なる文字である
    # 7. AとCはR, G, Bのどれか
    # 8. AとCは異なる文字である
    # 9. BとCは異なる文字である
    # 10. AとBの距離はBとCの距離と異なる
    # 11. AとCの距離はBとCの距離と異なる

    # 1. AとBはR, G, Bのどれか
    # 2. AとB
