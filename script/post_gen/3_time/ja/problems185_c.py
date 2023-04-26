Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def comb(n, r):
    r = min(r, n-r)
    if r == 0: return 1
    over = reduce(lambda a, b: a*b, xrange(n, n-r, -1))
    under = reduce(lambda a, b: a*b, xrange(1, r+1))
    return over/under

l = input()
print comb(l-1, 11)

=======
Suggestion 2

def main():
    l = int(input())
    l -= 12
    ans = 1
    for i in range(1, 11):
        ans *= l + i
        ans //= i
    print(ans)

=======
Suggestion 3

def calc_cut(n):
    if n == 12:
        return 1
    else:
        return calc_cut(n-1) + (n-1)

n = int(input())
print(calc_cut(n))

=======
Suggestion 4

def main():
    L = int(input())
    print(solve(L))

=======
Suggestion 5

def main():
    n = int(input())
    print(2**(n-1)-1)

=======
Suggestion 6

def main():
    L = int(input())
    print(L-1)

=======
Suggestion 7

def solve():
    L = int(input())
    print(L-1)

=======
Suggestion 8

def get_input_data():
    l = int(input())
    return l

=======
Suggestion 9

def main():
    print("Hello World!")
