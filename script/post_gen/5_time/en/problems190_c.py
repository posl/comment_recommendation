Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, M = map(int, input().split())
    A = []
    B = []
    for i in range(M):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    K = int(input())
    C = []
    D = []
    for i in range(K):
        c, d = map(int, input().split())
        C.append(c)
        D.append(d)

    ans = 0
    for i in range(2**K):
        dish = [0]*N
        for j in range(K):
            if (i>>j)&1:
                dish[C[j]-1] += 1
            else:
                dish[D[j]-1] += 1
        count = 0
        for k in range(M):
            if dish[A[k]-1] > 0 and dish[B[k]-1] > 0:
                count += 1
        ans = max(ans, count)
    print(ans)

=======
Suggestion 2

def solve():
    N, M = map(int, input().split())
    AB = [tuple(map(int, input().split())) for _ in range(M)]
    K = int(input())
    CD = [tuple(map(int, input().split())) for _ in range(K)]
    ans = 0
    for i in range(2 ** K):
        balls = [0] * N
        for j in range(K):
            if (i >> j) & 1:
                balls[CD[j][0] - 1] += 1
            else:
                balls[CD[j][1] - 1] += 1
        cnt = 0
        for a, b in AB:
            if balls[a - 1] and balls[b - 1]:
                cnt += 1
        ans = max(ans, cnt)
    print(ans)

=======
Suggestion 3

def solve():
    N, M = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(M)]
    K = int(input())
    CD = [list(map(int, input().split())) for _ in range(K)]

    ans = 0
    for i in range(2 ** K):
        cnt = 0
        balls = [0] * (N + 1)
        for j in range(K):
            if (i >> j) & 1:
                balls[CD[j][0]] += 1
            else:
                balls[CD[j][1]] += 1
        for a, b in AB:
            if balls[a] > 0 and balls[b] > 0:
                cnt += 1
        ans = max(ans, cnt)
    print(ans)

=======
Suggestion 4

def solve():
    N, M = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(M)]
    K = int(input())
    CD = [list(map(int, input().split())) for _ in range(K)]

    ans = 0
    for i in range(2**K):
        tmp = [0]*(N+1)
        for j in range(K):
            if (i>>j)&1:
                tmp[CD[j][0]] += 1
            else:
                tmp[CD[j][1]] += 1
        cnt = 0
        for m in range(M):
            if tmp[AB[m][0]] >= 1 and tmp[AB[m][1]] >= 1:
                cnt += 1
        ans = max(ans, cnt)
    print(ans)

=======
Suggestion 5

def main():
    N, M = map(int, input().split())
    A = [0] * M
    B = [0] * M
    for i in range(M):
        A[i], B[i] = map(int, input().split())
    K = int(input())
    C = [0] * K
    D = [0] * K
    for i in range(K):
        C[i], D[i] = map(int, input().split())

    ans = 0
    for i in range(2**K):
        ball = [0] * N
        for j in range(K):
            if ((i >> j) & 1):
                ball[C[j]-1] += 1
            else:
                ball[D[j]-1] += 1
        tmp = 0
        for k in range(M):
            if ball[A[k]-1] > 0 and ball[B[k]-1] > 0:
                tmp += 1
        if tmp > ans:
            ans = tmp

    print(ans)

=======
Suggestion 6

def main():
    n, m = map(int, input().split())
    ab = []
    for i in range(m):
        ab.append(list(map(int, input().split())))
    k = int(input())
    cd = []
    for i in range(k):
        cd.append(list(map(int, input().split())))

    ans = 0
    for i in range(2**k):
        dish = [0 for i in range(n)]
        for j in range(k):
            if (i >> j) & 1:
                dish[cd[j][0]-1] += 1
            else:
                dish[cd[j][1]-1] += 1
        tmp = 0
        for j in range(m):
            if dish[ab[j][0]-1] > 0 and dish[ab[j][1]-1] > 0:
                tmp += 1
        ans = max(ans, tmp)
    print(ans)

=======
Suggestion 7

def get_input():
    N, M = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(M)]
    K = int(input())
    CD = [list(map(int, input().split())) for _ in range(K)]
    return N, M, AB, K, CD

=======
Suggestion 8

def main():
	n, m = map(int, input().split())
	conditions = []
	for _ in range(m):
		a, b = map(int, input().split())
		conditions.append((a, b))
	k = int(input())
	people = []
	for _ in range(k):
		c, d = map(int, input().split())
		people.append((c, d))

	max_count = 0
	for i in range(2**k):
		balls = [0] * (n + 1)
		count = 0
		for j in range(k):
			if i >> j & 1:
				balls[people[j][0]] += 1
			else:
				balls[people[j][1]] += 1
		for condition in conditions:
			if balls[condition[0]] >= 1 and balls[condition[1]] >= 1:
				count += 1
		max_count = max(max_count, count)
	print(max_count)

=======
Suggestion 9

def main():
    N, M = map(int, input().split())
    cond = [tuple(map(int, input().split())) for _ in range(M)]
    K = int(input())
    dish = [tuple(map(int, input().split())) for _ in range(K)]

    ans = 0
    for i in range(2**K):
        dish_on = [False] * N
        for j in range(K):
            if (i >> j) & 1:
                dish_on[dish[j][1]-1] = True
            else:
                dish_on[dish[j][0]-1] = True
        cnt = 0
        for c in cond:
            if dish_on[c[0]-1] and dish_on[c[1]-1]:
                cnt += 1
        if cnt > ans:
            ans = cnt
    print(ans)

=======
Suggestion 10

def count_satisfied_conditions(n, m, a, b, k, c, d):
    max_satisfied_conditions = 0
    for i in range(2 ** k):
        dishes = [0] * n
        for j in range(k):
            if (i >> j) & 1:
                dishes[c[j] - 1] += 1
            else:
                dishes[d[j] - 1] += 1
        satisfied_conditions = 0
        for j in range(m):
            if dishes[a[j] - 1] and dishes[b[j] - 1]:
                satisfied_conditions += 1
        max_satisfied_conditions = max(max_satisfied_conditions, satisfied_conditions)
    return max_satisfied_conditions
