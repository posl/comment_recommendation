Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    result = ''
    while N > 0:
        if N % 2 == 0:
            N = N // 2
            result = 'B' + result
        else:
            N -= 1
            result = 'A' + result
    print(result)

=======
Suggestion 2

def solve(n):
    ans = ''
    while n > 0:
        if n % 2 == 0:
            ans += 'B'
            n //= 2
        else:
            ans += 'A'
            n -= 1
    return ans[::-1]
n = int(input())
print(solve(n))

=======
Suggestion 3

def main():
    n = int(input())
    ans = []
    while n > 0:
        if n % 2 == 0:
            ans.append("B")
            n //= 2
        else:
            ans.append("A")
            n -= 1
    ans.reverse()
    print("".join(ans))

=======
Suggestion 4

def main():
    N = int(input())
    ans = ""
    while N != 0:
        if N % 2 == 0:
            N = N // 2
            ans += "B"
        else:
            N -= 1
            ans += "A"
    print(ans[::-1])

=======
Suggestion 5

def solve(n):
    s=""
    while n>0:
        if n%2==0:
            s="B"+s
            n=n//2
        else:
            s="A"+s
            n-=1
    return s

n=int(input())
print(solve(n))

=======
Suggestion 6

def solve(n):
    ans = []
    while n > 0:
        if n % 2 == 0:
            n = n // 2
            ans.append("B")
        else:
            n -= 1
            ans.append("A")
    return "".join(ans[::-1])

=======
Suggestion 7

def main():
    n = int(input())
    ans = ''
    while n > 0:
        if n%2 == 1:
            ans = 'A' + ans
            n -= 1
        else:
            ans = 'B' + ans
            n //= 2
    print(ans)

=======
Suggestion 8

def main():
    n = int(input())
    ans = ""
    while n > 0:
        if n % 2 == 0:
            n //= 2
            ans = "B" + ans
        else:
            n -= 1
            ans = "A" + ans
    print(ans)

=======
Suggestion 9

def main():
    n = int(input())
    result = []
    while n > 0:
        if n % 2 == 0:
            n = n // 2
            result.append('B')
        else:
            n = n - 1
            result.append('A')
    result.reverse()
    print(''.join(result))

=======
Suggestion 10

def getA(n):
    if n==0:
        return ""
    elif n==1:
        return "A"
    elif n%2==0:
        return getA(n//2)+"B"
    else:
        return getA(n-1)+"A"
