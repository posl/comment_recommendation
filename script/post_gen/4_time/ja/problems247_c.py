Synthesizing 10/10 solutions

=======
Suggestion 1

def f(n):
    if n == 1:
        return [1]
    else:
        return f(n-1) + [n] + f(n-1)

N = int(input())
print(*f(N))

=======
Suggestion 2

def f(n):
  if n == 1:
    return [1]
  else:
    return f(n-1) + [n] + f(n-1)

n = int(input())
print(*f(n))

=======
Suggestion 3

def func(n):
    if n == 1:
        return [1]
    else:
        a = func(n-1)
        return a + [n] + a

n = int(input())
print(*func(n))

=======
Suggestion 4

def solve(n):
    if n == 1:
        return [1]
    else:
        ans = solve(n-1)
        ans.append(n)
        ans += solve(n-1)
        return ans

=======
Suggestion 5

def main():
    n = int(input())
    if n == 1:
        print(1)
    else:
        result = [1]
        for i in range(1, n):
            result = result + [i+1] + result
        print(*result)

=======
Suggestion 6

def a(n):
    if n == 1:
        return [1]
    else:
        return a(n-1) + [n] + a(n-1)

N = int(input())
print(*a(N))

=======
Suggestion 7

def main():
    N = int(input())
    S = [1]
    for i in range(2,N+1):
        S = S + [i] + S
    print(' '.join(map(str,S)))

=======
Suggestion 8

def main():
    n = int(input())
    result = [1]
    for i in range(1,n):
        result = result + [i+1] + result
    print(*result)

=======
Suggestion 9

def main():
    n = int(input())
    for i in range(1,n+1):
        print(i, end=" ")
        if i == 1:
            continue
        for j in range(i-1,0,-1):
            print(j, end=" ")
        print(i, end=" ")

=======
Suggestion 10

def main():
    n = int(input())
    if n == 1:
        print(1)
        exit()
    else:
        s = [1,2,1]
        for i in range(2,n-1):
            s = s + [i+2] + s
    print(*s)
