Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        if a[i] > 10:
            ans += a[i] - 10
    print(ans)

=======
Suggestion 2

def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    for a in A:
        if a > 10:
            ans += a - 10
    print(ans)

=======
Suggestion 3

def main():
    N = int(input())
    A = list(map(int, input().split()))
    count = 0
    for i in range(N):
        if A[i] > 10:
            count += A[i] - 10
    print(count)

=======
Suggestion 4

def main():
    N = int(input())
    A = [int(a) for a in input().split()]
    total = 0
    for a in A:
        if a > 10:
            total += a - 10
    print(total)

=======
Suggestion 5

def main():
    N = int(input())
    A = list(map(int, input().split()))
    total = 0
    for i in range(N):
        if A[i] > 10:
            total += A[i]-10
    print(total)

=======
Suggestion 6

def main():
    N = int(raw_input())
    A = map(int, raw_input().split())
    sum = 0
    for a in A:
        if a > 10:
            sum += a - 10
    print sum

=======
Suggestion 7

def main():
    n = int(input())
    nuts = [int(i) for i in input().split()]
    total = 0
    for i in nuts:
        if i > 10:
            total += i - 10
    print(total)

=======
Suggestion 8

def main():
    N = int(input())
    A = list(map(int, input().split()))
    print(sum([a-10 if a>10 else 0 for a in A]))

=======
Suggestion 9

def nuts(nuts):
    result = 0
    for nut in nuts:
        if nut > 10:
            result += nut - 10
    return result

=======
Suggestion 10

def main():
    N = int(input())
    A = list(map(int, input().split()))
    if N != len(A):
        print("Error: N != len(A)")
        return
    if N < 1 or N > 1000:
        print("Error: N is out of range")
        return
    for a in A:
        if a < 0 or a > 1000:
            print("Error: A is out of range")
            return
    ans = 0
    for a in A:
        if a > 10:
            ans += a - 10
    print(ans)

main()
