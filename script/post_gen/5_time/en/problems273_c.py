Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    a = list(map(int, input().split()))
    d = {}
    for i in a:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    for i in range(n):
        print(len(d)-d[a[i]])

=======
Suggestion 2

def main():
    n = int(input())
    a = list(map(int, input().split

=======
Suggestion 3

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    i = 0
    k = 0
    ans = [0] * n
    while i < n:
        j = i
        while j < n and a[i] == a[j]:
            j += 1
        if j == n:
            ans[k] += n - i
            break
        ans[k] += j - i
        i = j
        k += 1
    print('\n'.join(map(str, ans)))
main()

=======
Suggestion 4

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    count = 0
    result = [0] * N
    for i in range(N):
        if i == 0:
            count += 1
        elif A[i] != A[i-1]:
            count += 1
        result[i] = count
    for i in range(N):
        print(result[A[i]-1])

=======
Suggestion 5

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    A.append(-1)
    count = 1
    ans = [0] * N
    for i in range(N):
        if A[i] != A[i+1]:
            ans[count-1] += 1
            count = 1
        else:
            count += 1
    ans[count-1] += 1
    print(*ans, sep='\n')

=======
Suggestion 6

def main():
    N = int(input())
    A = list(map(int,input().split()))
    A.sort()
    ans = [0]*N
    for i in range(N):
        ans[i] = A[i]
    for i in range(N-2,-1,-1):
        if A[i] == A[i+1]:
            ans[i] = ans[i+1]
    for i in range(N):
        if i == 0:
            print(N-ans[i])
        else:
            print(N-ans[i]-i)

=======
Suggestion 7

def solve(N, A):
    B = sorted(A)
    C = [0] * (N + 1)
    for i in range(N):
        if i == 0 or B[i] != B[i-1]:
            C[i+1] = 1
    for i in range(1, N + 1):
        C[i] += C[i-1]
    for i in range(N):
        print(C[B.index(A[i])])

=======
Suggestion 8

def main():
    N = int(input())
    A = list(map(int, input().split()))

    A.sort()
    A.append(0)
    count = 1
    ans = [0 for i in range(N)]
    for i in range(1, N+1):
        if A[i-1] != A[i]:
            ans[count-1] = i - count
            count = i + 1
    print(*ans, sep='\n')

=======
Suggestion 9

def main():
    n = int(input())
    a_list = [int(x) for x in input().split()]
    a_list.sort()
    prev = a_list[0]
    prev_count = 1
    prev_index = 0
    result_list = [0] * n
    for i in range(1, n):
        if a_list[i] == prev:
            prev_count += 1
        else:
            for j in range(prev_index, i):
                result_list[j] = i - prev_index - prev_count
            prev = a_list[i]
            prev_count = 1
            prev_index = i
    for j in range(prev_index, n):
        result_list[j] = n - prev_index - prev_count
    for i in range(n):
        print(result_list[i])

=======
Suggestion 10

def problems273_c():
    n = int(input())
    a = [int(i) for i in input().split()]
    # print(n)
    # print(a)
    a = sorted(a)
    # print(a)
    count = 1
    for i in range(1, n):
        if a[i-1] != a[i]:
            count += 1
    # print(count)
    for i in range(n):
        if a[i] == a[i-1]:
            print(count-1)
        else:
            print(count)

problems273_c()
