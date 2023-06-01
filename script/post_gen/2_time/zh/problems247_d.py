Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    print("1", end="")
    for i in range(n-1):
        print(" " + str(i+2) + " 1", end="")
    print()

=======
Suggestion 2

def problem247_c(n):
    if n == 1:
        print(1)
        return
    s = [1]
    for i in range(2,n+1):
        s = s + [i] + s
    print(" ".join(map(str,s)))
    return

=======
Suggestion 3

def s(n):
    if n == 1:
        return [1]
    else:
        a = s(n-1)
        return a + [n] + a

n = int(input())
print(" ".join(map(str, s(n))))

=======
Suggestion 4

def S(n):
    if n == 1:
        return [1]
    else:
        return S(n-1) + [n] + S(n-1)

n = int(input())
print(*S(n))

=======
Suggestion 5

def main():
    n = int(input())
    print(' '.join(map(str, s(n))))

=======
Suggestion 6

def S(n):
    if n==1:
        return [1]
    else:
        x = S(n-1)
        return x + [n] + x

n = int(input())
print(" ".join(map(str, S(n))))

=======
Suggestion 7

def s(n):
    if n == 1:
        return [1]
    else:
        s_n_1 = s(n-1)
        return s_n_1 + [n] + s_n_1

=======
Suggestion 8

def get_s(n):
    if n == 1:
        return [1]
    else:
        return get_s(n-1) + [n] + get_s(n-1)

=======
Suggestion 9

def f(n):
    if n == 1:
        return [1]
    else:
        return f(n-1) + [n] + f(n-1)

n = int(input())
print(*f(n))

=======
Suggestion 10

def recursion(n):
    if n == 1:
        return [1]
    else:
        return recursion(n-1) + [n] + recursion(n-1)
