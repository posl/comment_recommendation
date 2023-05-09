Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    if N % 4 == 0 or N % 7 == 0 or N % 11 == 0 or N % 15 == 0 or N % 18 == 0 or N % 22 == 0 or N % 26 == 0 or N % 30 == 0 or N % 33 == 0 or N % 37 == 0 or N % 40 == 0:
        print("Yes")
    else:
        print("No")

main()

=======
Suggestion 2

def main():
    n = int(input())
    if n % 4 == 0 or n % 7 == 0 or n % 11 == 0:
        print('Yes')
        return
    for i in range(1, n):
        for j in range(1, n):
            if i * 4 + j * 7 == n:
                print('Yes')
                return
    print('No')

=======
Suggestion 3

def main():
    n = int(input())
    if n % 4 == 0 or n % 7 == 0 or n % 11 == 0:
        print('Yes')
    else:
        for i in range(1, 10):
            for j in range(1, 10):
                if 4*i + 7*j == n:
                    print('Yes')
                    return
        print('No')

=======
Suggestion 4

def main():
    N = int(input())
    if N%4 == 0 or N%7 == 0 or N%11 == 0 or N%15 == 0 or N%18 == 0 or N%22 == 0 or N%26 == 0 or N%30 == 0 or N%34 == 0 or N%38 == 0 or N%42 == 0 or N%46 == 0 or N%50 == 0 or N%54 == 0 or N%58 == 0 or N%62 == 0 or N%66 == 0 or N%70 == 0 or N%74 == 0 or N%78 == 0 or N%82 == 0 or N%86 == 0 or N%90 == 0 or N%94 == 0 or N%98 == 0 or N%102 == 0 or N%106 == 0 or N%110 == 0 or N%114 == 0 or N%118 == 0 or N%122 == 0 or N%126 == 0 or N%130 == 0 or N%134 == 0 or N%138 == 0 or N%142 == 0 or N%146 == 0 or N%150 == 0 or N%154 == 0 or N%158 == 0 or N%162 == 0 or N%166 == 0 or N%170 == 0 or N%174 == 0 or N%178 == 0 or N%182 == 0 or N%186 == 0 or N%190 == 0 or N%194 == 0 or N%198 == 0 or N%202 == 0 or N%206 == 0 or N%210 == 0 or N%214 == 0 or N%218 == 0 or N%222 == 0 or N%226 == 0 or N%230 == 0 or N%234 == 0 or N%238 == 0 or N%242 == 0 or N%246 == 0 or N%250 == 0 or N%254 == 0 or N%258 == 0 or N%262 == 0 or N%266 == 0 or N%270 == 0 or N%274 == 0 or N%278 == 0 or

=======
Suggestion 5

def main():
    N = int(input())
    for i in range(26):
        for j in range(16):
            if 4*i + 7*j == N:
                print('Yes')
                return
    print('No')

=======
Suggestion 6

def answer():
    N = int(input())
    for i in range(N//4+1):
        for j in range(N//7+1):
            if 4*i+7*j == N:
                return 'Yes'
    return 'No'

print(answer())

=======
Suggestion 7

def solve(N):
    for i in range(0, N//4 + 1):
        if (N - 4*i) % 7 == 0:
            return "Yes"
    return "No"

N = int(input())
print(solve(N))

=======
Suggestion 8

def buy_sweets():
    n = int(input())
    if n % 4 == 0 or n % 7 == 0 or n % 11 == 0:
        print("Yes")
        return
    for i in range(1, n // 4 + 1):
        for j in range(1, n // 7 + 1):
            if n - 4 * i - 7 * j == 0:
                print("Yes")
                return
    print("No")

=======
Suggestion 9

def main():
    #N = int(input())
    N = 11
    for i in range(0, N):
        for j in range(0, N):
            if (4*i + 7*j == N):
                print("Yes")
                return
    print("No")

=======
Suggestion 10

def problem105_b(n):
    # print(n)
    if n % 4 == 0 or n % 7 == 0:
        return 'Yes'
    else:
        for i in range(1, n // 4 + 1):
            if (n - i * 4) % 7 == 0:
                return 'Yes'
        return 'No'
