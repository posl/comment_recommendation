Synthesizing 10/10 solutions

=======
Suggestion 1

def f(n):
    if n == 1:
        return [1]
    else:
        return f(n-1) + [n] + f(n-1)

n = int(input())
print(*f(n))

=======
Suggestion 2

def print_seq(n):
    if n == 1:
        print(1)
        return
    print_seq(n-1)
    print(n)
    print_seq(n-1)

=======
Suggestion 3

def sn(n):
    if n == 1:
        return [1]
    else:
        return sn(n-1) + [n] + sn(n-1)

n = int(input())
print(*sn(n))

=======
Suggestion 4

def s(n):
    if n == 1:
        return [1]
    else:
        a = s(n - 1)
        return a + [n] + a

=======
Suggestion 5

def make_list(n):
    if n == 1:
        return [1]
    else:
        return make_list(n-1) + [n] + make_list(n-1)

=======
Suggestion 6

def s(n):
    if n == 1:
        return [1]
    else:
        return s(n-1) + [n] + s(n-1)

N = int(input())
print(" ".join(map(str, s(N))))

=======
Suggestion 7

def get_S(n):
    if n == 1:
        return [1]
    else:
        return get_S(n-1) + [n] + get_S(n-1)

=======
Suggestion 8

def print_seq(n):
    if n == 1:
        return '1'
    else:
        return print_seq(n-1) + ' ' + str(n) + ' ' + print_seq(n-1)

=======
Suggestion 9

def S(n):
    if n == 1:
        return [1]
    else:
        return S(n-1) + [n] + S(n-1)

N = int(input())
print(*S(N))

=======
Suggestion 10

def seq(n):
    if n == 1:
        return [1]
    else:
        return seq(n-1) + [n] + seq(n-1)
