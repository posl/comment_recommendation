Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def solve():
    pass

=======
Suggestion 2

def find_sum_equal_200(n, a):
    m = len(a)
    for i in range(m):
        for j in range(i+1, m):
            if (a[i]+a[j])%200 == 0:
                return True, [i+1], [j+1]
    return False, [], []

=======
Suggestion 3

def main():
    N = int(input())
    A = list(map(int, input().split()))
    for x in range(1, N+1):
        for y in range(1, N+1):
            B = [i for i in range(1, N+1) if i not in range(x+1, N+1)]
            C = [i for i in range(1, N+1) if i not in range(y+1, N+1)]
            if sum([A[i-1] for i in B]) % 200 == sum([A[i-1] for i in C]) % 200:
                print('Yes')
                print(len(B), ' '.join(map(str, B)))
                print(len(C), ' '.join(map(str, C)))
                return
    print('No')

=======
Suggestion 4

def main():
    n = int(input())
    a = [int(x) for x in input().split()]

    # x = 1
    for i in range(n):
        for j in range(i+1, n):
            if (a[i] + a[j]) % 200 == 0:
                print('Yes')
                print(1, i+1)
                print(1, j+1)
                return

    # x = 2
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                if (a[i] + a[j] + a[k]) % 200 == 0:
                    print('Yes')
                    print(2, i+1, j+1)
                    print(1, k+1)
                    return

    # x = 3
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                for l in range(k+1, n):
                    if (a[i] + a[j] + a[k] + a[l]) % 200 == 0:
                        print('Yes')
                        print(3, i+1, j+1, k+1)
                        print(1, l+1)
                        return

    # x = 4
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                for l in range(k+1, n):
                    for m in range(l+1, n):
                        if (a[i] + a[j] + a[k] + a[l] + a[m]) % 200 == 0:
                            print('Yes')
                            print(4, i+1, j+1, k+1, l+1)
                            print(1, m+1)
                            return

    # x = 5
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                for l in range(k+1, n):
                    for m in range(l+1, n):
                        for o in range(m+1, n):
                            if (a[i] + a[j] + a[k] + a[l] + a[m] +

=======
Suggestion 5

def solve():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    A = [0] + A
    d = {}
    for i in range(1, N + 1):
        for j in range(i, N + 1):
            if (A[i] + A[j]) % 200 not in d:
                d[(A[i] + A[j]) % 200] = (i, j)
            else:
                print('Yes')
                print(2, i, j)
                print(2, d[(A[i] + A[j]) % 200][0], d[(A[i] + A[j]) % 200][1])
                return
    print('No')

solve()

=======
Suggestion 6

def main():
    pass

=======
Suggestion 7

def find_two_nums(num_list):
    for i in range(len(num_list)):
        for j in range(len(num_list)):
            if i != j:
                if num_list[i] + num_list[j] == 200:
                    return num_list[i], num_list[j]
    return None, None

=======
Suggestion 8

def find():
    n = int(input())
    a = list(map(int, input().split()))
    a = [0] + a
    d = {}
    for i in range(1, n + 1):
        d[a[i]] = i
    for i in range(1, n + 1):
        for j in range(i + 1, n + 1):
            b = a[i] + a[j]
            if b % 200 in d:
                if d[b % 200] != i and d[b % 200] != j:
                    print('Yes')
                    print('1', i)
                    print('1', d[b % 200])
                    return
    print('No')
    return

find()

=======
Suggestion 9

def main():
    N = int(input())
    A = input().split()
    A = [int(i) for i in A]
    if N == 2:
        if A[0] % 200 == A[1] % 200:
            print('Yes')
            print(1, 1)
            print(1, 2)
        else:
            print('No')
    else:
        print('Yes')
        print(1, 1)
        print(2, 2, 3)
