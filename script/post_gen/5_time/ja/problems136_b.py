Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def solve():
    n = int(input())
    ans = 0
    for i in range(1, n+1):
        if len(str(i)) % 2 == 1:
            ans += 1
    print(ans)

=======
Suggestion 2

def main():
	n = int(input())
	count = 0
	for i in range(1,n+1):
		if len(str(i)) % 2 == 1:
			count += 1
	print(count)

=======
Suggestion 3

def main():
    n = int(input())
    ans = 0
    for i in range(1, n+1):
        if len(str(i)) % 2 == 1:
            ans += 1
    print(ans)

=======
Suggestion 4

def main():
    N = int(input())
    ans = 0
    for i in range(1,N+1):
        if len(str(i)) % 2 == 1:
            ans += 1
    print(ans)

=======
Suggestion 5

def main():
    n = int(input())
    count = 0
    for i in range(1, n + 1):
        if len(str(i)) % 2 != 0:
            count += 1
    print(count)

=======
Suggestion 6

def main():
    N = int(input())
    c = 0
    for i in range(1,N+1):
        if len(str(i)) % 2 == 1:
            c += 1
    print(c)

=======
Suggestion 7

def main():
    N = int(input())
    count = 0
    for i in range(1, N + 1):
        if len(str(i)) % 2 != 0:
            count += 1
    print(count)

=======
Suggestion 8

def main():
    n = int(input())
    cnt = 0
    for i in range(1, n+1):
        if len(str(i)) % 2 == 1:
            cnt += 1
    print(cnt)

=======
Suggestion 9

def oddDigits(n):
    count = 0
    for i in range(1,n+1):
        if len(str(i))%2 == 1:
            count += 1
    return count

n = int(input())
print(oddDigits(n))
