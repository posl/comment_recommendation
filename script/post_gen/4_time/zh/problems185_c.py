Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def cutbar(m,n,current):
	if current >= n:
		return 0
	elif current < m:
		return 1 + cutbar(m,n,current*2)
	else:
		return 1 + cutbar(m,n,current + m)

print(cu

=======
Suggestion 2

def f(l):
    if l==12:
        return 1
    else:
        return sum([f(l-i) for i in range(1,l-10)])
print(f(int(input())))

=======
Suggestion 3

def main():
    L = int(input())
    print(count(L))

=======
Suggestion 4

def cut(n):
    if n<2:
        return 1
    else:
        return cut(n-1)+n-1

=======
Suggestion 5

def solve(L):
    if L == 12:
        return 1
    ans = 0
    for i in range(1, L-10):
        ans += solve(L-i)
    return ans

=======
Suggestion 6

def main():
    pass

=======
Suggestion 7

def solve():
    L = int(input())
    ans = 0
    for a in range(1, L-10):
        for b in range(1, L-10-a):
            c = L-a-b
            ans += (a+b+c-1)*(a+b+c-2)//2
    print(ans)

=======
Suggestion 8

def f(n):
    if n == 0:
        return 1
    elif n < 0:
        return 0
    else:
        return f(n-1) + f(n-2) + f(n-3) + f(n-4)

L = int(raw_input())
print f(L)
