Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    A = list(map(int, input().split()))
    count = 0
    for i in range(N):
        while A[i] % 2 == 0:
            A[i] = A[i] // 2
            count += 1
        while A[i] % 3 == 0:
            A[i] = A[i] // 3
            count += 1
    if len(set(A)) == 1:
        print(count)
    else:
        print(-1)

=======
Suggestion 2

def main():
    N = int(input())
    A = list(map(int, input().split()))
    count = 0
    while True:
        for i in range(N):
            if A[i] % 2 == 0:
                A[i] = A[i] // 2
            elif A[i] % 3 == 0:
                A[i] = A[i] // 3
            else:
                if i == N - 1 and A[i] == A[0]:
                    print(count)
                    return
                else:
                    print(-1)
                    return
        count += 1

=======
Suggestion 3

def main():
    N = int(input())
    A = list(map(int, input().split()))
    cnt = 0
    for i in range(N):
        while A[i] % 2 == 0:
            A[i] //= 2
            cnt += 1
        while A[i] % 3 == 0:
            A[i] //= 3
            cnt += 1
    if len(set(A)) == 1:
        print(cnt)
    else:
        print(-1)

=======
Suggestion 4

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

=======
Suggestion 5

def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    while True:
        if all([a == A[0] for a in A]):
            break
        for i in range(N):
            if A[i] % 3 == 0:
                A[i] //= 3
                ans += 1
                break
        else:
            for i in range(N):
                if A[i] % 2 == 0:
                    A[i] //= 2
                    ans += 1
                    break
            else:
                ans = -1
                break
    print(ans)

=======
Suggestion 6

def solve():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    while True:
        for i in range(N):
            if A[i] % 2 == 1:
                return ans
            else:
                A[i] = A[i] // 2
        ans += 1

=======
Suggestion 7

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    if A[0] == A[N-1]:
        print(0)
        return
    cnt = 0
    while True:
        cnt += 1
        A[0] *= 2
        A.sort()
        if A[0] == A[N-1]:
            print(cnt)
            return
        if A[0] > A[N-1]:
            print(-1)
            return

=======
Suggestion 8

def main():
    N = int(input())
    A = list(map(int, input().split()))
    # A = [1, 4, 3]
    # N = 3

    # A = [2, 7, 6]
    # N = 3

    # A = [1, 1, 1, 1, 1, 1]
    # N = 6

    A.sort()
    if A[0] != A[N-1]:
        print(-1)
        exit()

    count = 0
    for i in range(N):
        while A[i] % 2 == 0:
            count += 1
            A[i] = A[i] // 2
        while A[i] % 3 == 0:
            count += 1
            A[i] = A[i] // 3

    print(count)

=======
Suggestion 9

def main():
    n = int(input())
    A = list(map(int, input().split()))
    count = 0
    while True:
        if A == [A[0]] * n:
            break
        for i in range(n):
            if A[i] % 2 == 0:
                A[i] = A[i] // 2
                count += 1
            elif A[i] % 3 == 0:
                A[i] = A[i] // 3
                count += 1
            else:
                count = -1
                break
    print(count)

=======
Suggestion 10

def get_input():
    input_line = input()
    input_values = input_line.split()
    return input_values
