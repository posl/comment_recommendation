Synthesizing 10/10 solutions

=======
Suggestion 1

def permutation(n):
	if n == 0:
		yield []
	else:
		for i in range(n):
			for p in permutation(n-1):
				yield p[:i] + [n-1] + p[i:]

=======
Suggestion 2

def get_permutation_num(permutation):
    permutation_num = 0
    for i in range(0, len(permutation)):
        permutation_num += permutation[i] * (10 ** (len(permutation) - i - 1))
    return permutation_num

=======
Suggestion 3

def permutation(n, start, end):
    if start == end:
        print(n)
    else:
        for i in range(start, end):
            n[start], n[i] = n[i], n[start]
            permutation(n, start + 1, end)
            n[start], n[i] = n[i], n[start]

=======
Suggestion 4

def getRank(p):
    n = len(p)
    rank = 0
    for i in range(n):
        for j in range(i+1,n):
            if p[i] > p[j]:
                rank += 1
    return rank

=======
Suggestion 5

def getNum(a):
    n = len(a)
    if n == 1:
        return 0
    if n == 2:
        return 1 if a[0] > a[1] else 0
    else:
        count = 0
        for i in range(n):
            for j in range(i+1, n):
                if a[i] > a[j]:
                    count += 1
        return count

=======
Suggestion 6

def get_permutations(n):
    if n == 1:
        return [[1]]
    else:
        permutations = []
        for i in range(n):
            for j in get_permutations(n - 1):
                permutations.append(j[:i] + [n] + j[i:])
        return permutations

=======
Suggestion 7

def main():
    n = int(input())
    p = [int(x) for x in input().split()]
    q = [int(x) for x in input().split()]
    print(abs(p.index(1)-q.index(1)))

=======
Suggestion 8

def get_min_permutation(n):
    return [i for i in range(1,n+1)]

=======
Suggestion 9

def main():
    N = int(input())
    P = list(map(int, input().split()))
    Q = list(map(int, input().split()))
    print(abs(P.index(1) - Q.index(1)))

=======
Suggestion 10

def permutation(n):
    if n == 1:
        return [[1]]
    else:
        return [[n] + p for p in permutation(n - 1)] + [p + [n] for p in permutation(n - 1)]
