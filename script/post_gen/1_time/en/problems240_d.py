Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    a = list(map(int, input().split()))
    d = {}
    for i in range(n):
        if a[i] in d:
            d[a[i]] += 1
        else:
            d[a[i]] = 1
    ans = 0
    for i in range(n):
        if a[i] in d:
            ans += 1
            if d[a[i]] == 1:
                del d[a[i]]
            else:
                d[a[i]] -= 1
    print(ans)

=======
Suggestion 2

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = []
    for i in range(n):
        b.append(0)
    for i in range(n):
        b[a[i] - 1] += 1
    for i in range(n):
        print(b[i])

=======
Suggestion 3

def main():
	n = int(input())
	a = list(map(int, input().split()))
	b = [0] * (2 * 10 ** 5 + 1)
	for i in range(n):
		b[a[i]] += 1
	s = 0
	for i in range(2 * 10 ** 5, 1, -1):
		b[i - 1] += b[i] // 2
		s += b[i] % 2
		b[i] = 0
		print(s)
main()

=======
Suggestion 4

def main():
    N = int(input())
    a = list(map(int, input().split()))
    ans = [0] * N
    ans[0] = 1
    for i in range(1, N):
        if a[i] == a[i-1]:
            ans[i] = ans[i-1]
        else:
            ans[i] = ans[i-1] + 1
    print(*ans, sep='\n')

=======
Suggestion 5

def main():
    n = int(input())
    a = list(map(int, input().split()))
    cnt = {}
    for i in a:
        cnt[i] = cnt.get(i, 0) + 1
    ans = 0
    for k, v in cnt.items():
        ans = max(ans, v)
    print(ans)

=======
Suggestion 6

def solve():
    n = int(input())
    a = [int(i) for i in input().split()]
    b = [0] * n
    b[0] = a[0]
    for i in range(1, n):
        b[i] = b[i-1] ^ a[i]
    for i in range(n):
        print(b[i])

=======
Suggestion 7

def main():
    n = int(input())
    a = list(map(int, input().split()))
    d = {}
    for i in range(n):
        d[i] = 0
    d[0] = 1
    for i in range(n):
        d[a[i]-1] += 1
    for i in range(n):
        print(d[i])

=======
Suggestion 8

def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = []
    for i in range(n):
        a_i = a[i]
        if a_i % 2 == 0:
            ans.append(1)
        else:
            ans.append(0)
    print('\n'.join(map(str, ans)))

=======
Suggestion 9

def solve():
    n = int(input())
    a = [int(x) for x in input().split()]
    ans = [0]*n
    d = {}
    for i in range(n):
        if a[i] in d:
            ans[i] = ans[d[a[i]]] + 1
        d[a[i]] = i
    print(*ans, sep='\n')

=======
Suggestion 10

def check_balls(balls):
    if len(balls) < 2:
        return balls
    else:
        if balls[-1] == balls[-2]:
            balls = balls[:-2]
            return check_balls(balls)
        else:
            return balls

n = int(input())
balls = []
for i in range(n):
    balls.append(int(input()))
    balls = check_balls(balls)
    print(len(balls))
