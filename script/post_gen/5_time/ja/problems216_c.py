Synthesizing 10/10 solutions

=======
Suggestion 1

def solve(n):
    result = ""
    while n > 0:
        if n % 2 == 0:
            n = n // 2
            result = "B" + result
        else:
            n = n - 1
            result = "A" + result
    return result

n = int(input())
print(solve(n))

=======
Suggestion 2

def solve(n):
    ans = []
    while n != 0:
        if n % 2 == 0:
            n //= 2
            ans.append('B')
        else:
            n -= 1
            ans.append('A')
    return ans[::-1]


n = int(input())
print(''.join(solve(n)))

=======
Suggestion 3

def main():
    N = int(input())
    ans = ''
    while N > 0:
        if N % 2 == 0:
            N = N // 2
            ans = 'B' + ans
        else:
            N -= 1
            ans = 'A' + ans
    print(ans)

=======
Suggestion 4

def main():
    N = int(input())
    ans = ''
    while N != 0:
        if N % 2 == 0:
            ans = 'B' + ans
            N //= 2
        else:
            ans = 'A' + ans
            N -= 1
    print(ans)

=======
Suggestion 5

def main():
    n = int(input())
    s = ''
    while n > 0:
        if n % 2 == 0:
            s = 'B' + s
            n //= 2
        else:
            s = 'A' + s
            n -= 1
    print(s)

=======
Suggestion 6

def main():
    n = int(input())
    ans = ''
    while n > 0:
        if n % 2 == 0:
            ans += 'B'
            n //= 2
        else:
            ans += 'A'
            n -= 1
    print(ans[::-1])

=======
Suggestion 7

def main():
    N = int(input())
    result = []
    while N > 0:
        if N % 2 == 1:
            N -= 1
            result.append("A")
        else:
            N //= 2
            result.append("B")
    result.reverse()
    print("".join(result))

=======
Suggestion 8

def main():
    N = int(input())
    ans = ""
    while N > 0:
        if N % 2 == 0:
            N = N // 2
            ans += "B"
        else:
            N -= 1
            ans += "A"
    print(ans[::-1])

=======
Suggestion 9

def main():
    N = int(input())
    S = ""
    while N > 0:
        if N % 2 == 0:
            S = "B" + S
            N = N // 2
        else:
            S = "A" + S
            N = N - 1
    print(S)

=======
Suggestion 10

def main():
    N = int(input())
    ans = []
    while N > 0:
        if N % 2 == 1:
            N -= 1
            ans.append('A')
        else:
            N //= 2
            ans.append('B')
    ans.reverse()
    print(''.join(ans))
