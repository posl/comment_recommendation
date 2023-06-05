Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    a = list(map(int, input().split()))
    x = 0
    ans = 0
    for i in range(n):
        x += a[i]
        ans = max(ans, x)
    print(ans)

=======
Suggestion 2

def main():
    num = int(input())
    nums = list(map(int, input().split()))
    max = 0
    sum = 0
    for i in range(num):
        sum += nums[i]
        if sum > max:
            max = sum
    print(max)

=======
Suggestion 3

def solve():
    n = int(input())
    a = list(map(int, input().split()))
    x = 0
    s = 0
    for i in range(n):
        s += a[i]
        x = max(x, s)
    print(x)

=======
Suggestion 4

def solve():
    n = int(raw_input())
    a = map(int, raw_input().split())
    ans = 0
    sum = 0
    for i in range(n):
        sum += a[i]
        ans = max(ans, sum)
    print ans

=======
Suggestion 5

def main():
    n = int(input())
    a = list(map(int, input().split()))
    max = 0
    sum = 0
    for i in range(n):
        sum += a[i]
        if sum > max:
            max = sum
    print(max)

=======
Suggestion 6

def solve():
    n = int(input())
    a = list(map(int,input().split()))
    ans = 0
    b = 0
    for i in range(n):
        b += a[i]
        ans = max(ans,b)
    print(ans)
solve()

=======
Suggestion 7

def main():
	n = int(input())
	a = list(map(int, input().split()))
	
	max = 0
	x = 0
	for i in range(n):
		x += a[i]
		if x > max:
			max = x
	print(max)

=======
Suggestion 8

def main():
    n = int(input())
    a = list(map(int, input().split()))
    c = 0
    d = 0
    for i in range(n):
        c += a[i]
        d = max(d, c)
    print(d)

=======
Suggestion 9

def main():
    n = int(raw_input())
    a = map(int, raw_input().split())
    b = [0] * n
    b[0] = a[0]
    for i in range(1, n):
        b[i] = b[i-1] + a[i]
    print max(b)

=======
Suggestion 10

def read_data():
    n = int(input())
    a = list(map(int, input().split()))
    return n, a
