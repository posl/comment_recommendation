Synthesizing 10/10 solutions

=======
Suggestion 1

def solve():
    N = int(input())
    A = [int(x) for x in input().split()]
    max_h = 0
    ans = 0
    for i in range(N):
        if max_h <= A[i]:
            ans += A[i] - max_h
            max_h = A[i]
        else:
            max_h = A[i]
    print(ans)

=======
Suggestion 2

def main():
    N = int(input())
    A = list(map(int,input().split()))
    A.insert(0,0)
    A.append(0)
    s = 0
    for i in range(len(A)-1):
        s += abs(A[i+1]-A[i])
    for i in range(1,len(A)-1):
        print(s+abs(A[i-1]-A[i+1])-abs(A[i-1]-A[i])-abs(A[i]-A[i+1]))

main()

=======
Suggestion 3

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.reverse()
    ans = 0
    for a in A:
        if a >= ans:
            ans += 1
    print(ans)

=======
Suggestion 4

def main():
    n = int(input())
    a = list(map(int, input().split()))

    # 从前往后遍历，如果当前值比前一个值高，那么当前值的凳子高度要比前一个值的凳子高度高1
    # 如果当前值比前一个值低，那么当前值的凳子高度要比前一个值的凳子高度低到能满足条件为止
    ans = 0
    for i in range(1, n):
        if a[i] > a[i-1]:
            ans += a[i] - a[i-1]
        elif a[i] < a[i-1]:
            ans -= a[i-1] - a[i]
            if ans < 0:
                ans = 0

    print(ans)

=======
Suggestion 5

def main():
	n = int(input())
	a = [int(x) for x in input().split()]
	# print(n)
	# print(a)
	ans = 0
	# for i in range(n):
	# 	ans += max(0, a[i] - a[i-1])
	# print(ans)
	for i in range(n-1):
		ans += max(0, a[i] - a[i+1])
	ans += max(0, a[n-1])
	print(ans)

=======
Suggestion 6

def main():
    n = int(input())
    a = list(map(int, input().split()))
    max_height = 0
    for i in range(n):
        if a[i] > max_height + 1:
            print(-1)
            return
        elif a[i] == max_height + 1:
            max_height += 1
    print(n - max_height)

=======
Suggestion 7

def solve():
    N = int(input())
    A = list(map(int, input().split()))
    A = sorted(A)
    for i in range(N):
        if i == 0:
            min_h = A[i]
        else:
            if A[i] - min_h > 1:
                return 1
            else:
                min_h = A[i]
    return 0

print(solve())

=======
Suggestion 8

def main():
    n = int(input())
    a = list(map(int, input().split(" ")))
    ans = 0
    for i in range(n-1, 0, -1):
        if a[i] - a[i-1] >= 2:
            print(-1)
            exit()
        elif a[i] - a[i-1] == 1:
            ans += 1
        else:
            ans += a[i]
    ans += a[0]
    print(ans)

=======
Suggestion 9

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = [0] * n

    for i in range(n-1):
        if a[i] < a[i+1]:
            b[i+1] = b[i] + 1
    for i in range(n-1, 0, -1):
        if a[i] < a[i-1] and b[i-1] <= b[i]:
            b[i-1] = b[i] + 1
    print(sum(b) + n)

=======
Suggestion 10

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.reverse()
    res = 0
    for i in range(N):
        if A[i] > res:
            res = A[i]
        elif A[i] < res:
            res = A[i] - 1
        else:
            pass
    print(res)
main()
