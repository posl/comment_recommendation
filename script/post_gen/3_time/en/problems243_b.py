Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    count1 = 0
    count2 = 0
    for i in range(n):
        if a[i] == b[i]:
            count1 += 1
    for i in range(n):
        if a[i] in b:
            count2 += 1
    print(count1)
    print(count2-count1)

=======
Suggestion 2

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A_dict = dict(zip(A, range(N)))
    B_dict = dict(zip(B, range(N)))
    count = 0
    for i in range(N):
        if A_dict[A[i]] == B_dict[A[i]]:
            count += 1
    print(count)
    print(N - count - len(set(A) & set(B)))

=======
Suggestion 3

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    A_dict = {}
    B_dict = {}
    for i in range(N):
        A_dict[A[i]] = i
        B_dict[B[i]] = i

    same = 0
    diff = 0
    for i in range(N):
        if A[i] in B_dict:
            if A_dict[A[i]] == B_dict[A[i]]:
                same += 1
            else:
                diff += 1

    print(same)
    print(diff)

=======
Suggestion 4

def main():
    N = int(input())
    A = [int(x) for x in input().split()]
    B = [int(x) for x in input().split()]
    count_same = 0
    count_diff = 0
    # 1. same position
    for i in range(N):
        if A[i] == B[i]:
            count_same += 1
    # 2. different position
    for i in range(N):
        for j in range(N):
            if i != j and A[i] == B[j]:
                count_diff += 1
    print(count_same)
    print(count_diff)

=======
Suggestion 5

def main():
    n = int(input())
    a = [int(i) for i in input().split()]
    b = [int(i) for i in input().split()]
    print(len(set(a) & set(b)))
    print(len(set(a) & set(b)) - len(set(a) & set(b) & set(zip(a, b))))

=======
Suggestion 6

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A.sort()
    B.sort()
    A_i = 0
    B_i = 0
    same = 0
    diff = 0
    while A_i < N and B_i < N:
        if A[A_i] == B[B_i]:
            same += 1
            A_i += 1
            B_i += 1
        elif A[A_i] < B[B_i]:
            A_i += 1
        else:
            B_i += 1
    A_i = 0
    B_i = 0
    while A_i < N and B_i < N:
        if A[A_i] == B[B_i]:
            A_i += 1
            B_i += 1
        elif A[A_i] < B[B_i]:
            A_i += 1
        else:
            B_i += 1
            diff += 1
    diff += N - A_i
    print(same)
    print(diff)

=======
Suggestion 7

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = [0] * (max(a) + 1)
    d = [0] * (max(b) + 1)
    for i in range(n):
        c[a[i]] += 1
        d[b[i]] += 1
    print(sum([min(c[i], d[i]) for i in range(len(c))]))
    print(sum([min(c[i], d[i]) for i in range(len(c))]) - sum([1 for i in range(n) if a[i] == b[i]]))

main()

=======
Suggestion 8

def main():
	N = int(input())
	A = list(map(int, input().split()))
	B = list(map(int, input().split()))
	
	A_dict = {}
	B_dict = {}
	
	for i in range(N):
		A_dict[A[i]] = i
		B_dict[B[i]] = i
	
	#1.
	same = 0
	for i in range(N):
		if A[i] in B_dict and i == B_dict[A[i]]:
			same += 1
	print(same)
	
	#2.
	diff = 0
	for i in range(N):
		if A[i] in B_dict and i != B_dict[A[i]]:
			diff += 1
	print(diff)

=======
Suggestion 9

def main():
    N = int(input())
    A = [int(x) for x in input().split()]
    B = [int(x) for x in input().split()]
    A.sort()
    B.sort()

    A_index = 0
    B_index = 0
    same_count = 0
    diff_count = 0
    while A_index < N and B_index < N:
        if A[A_index] == B[B_index]:
            same_count += 1
            A_index += 1
            B_index += 1
        elif A[A_index] < B[B_index]:
            A_index += 1
        else:
            B_index += 1

    A_index = 0
    B_index = 0
    while A_index < N and B_index < N:
        if A[A_index] == B[B_index]:
            A_index += 1
            B_index += 1
        elif A[A_index] < B[B_index]:
            A_index += 1
        else:
            B_index += 1
            diff_count += 1

    print(same_count)
    print(diff_count)

=======
Suggestion 10

def solve(N, A, B):
    # A_i = B_i
    same = 0
    for i in range(N):
        if A[i] == B[i]:
            same += 1
    # A_i = B_j, i != j
    diff = 0
    for i in range(N):
        for j in range(N):
            if i != j and A[i] == B[j]:
                diff += 1
    return same, diff
