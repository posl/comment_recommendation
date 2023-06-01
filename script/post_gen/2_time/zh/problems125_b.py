Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def problems125_a():
    a,b,t = map(int,input().split())
    cnt = 0
    for i in range(1,t+1):
        if i%a==0:
            cnt += b
    print(cnt)

=======
Suggestion 2

def problems125_a(a, b, t):
    count = 0
    for i in range(1, t+1):
        if i%a == 0:
            count += 1
    return count*b

=======
Suggestion 3

def main():
    a, b, t = map(int, input().split())
    print(int(t/a)*b)

=======
Suggestion 4

def solve():
    A, B, T = map(int, input().split())
    ans = 0
    for i in range(1, T + 1):
        if i % A == 0:
            ans += B
    print(ans)

=======
Suggestion 5

def main():
	nums = input().split()
	A = int(nums[0])
	B = int(nums[1])
	T = int(nums[2])
	sum = 0
	for i in range(1, T+1):
		if (i % A == 0):
			sum += B
	print(sum)

=======
Suggestion 6

def cookie_maker(a,b,t):
    cookie = 0
    for i in range(1,t+1):
        if i%a == 0:
            cookie += b
    return cookie

=======
Suggestion 7

def solve(a,b,t):
    count=0
    for i in range(1,t+1):
        if i%a==0:
            count+=b
    return count

=======
Suggestion 8

def problems125_a():
    A, B, T = map(int, input().split())
    count = 0
    for i in range(1, T + 1):
        if i % A == 0:
            count += B
    print(count)

=======
Suggestion 9

def main():
    a,b,t = map(int,input().split())
    count = 0
    for i in range(1,t+1):
        if i % a == 0:
            count += b
    print(count)
