Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n, t = map(int, input().split())
    a = list(map(int, input().split()))
    t %= sum(a)
    for i in range(n):
        t -= a[i]
        if t < 0:
            print(i+1, a[i]+t)
            break

=======
Suggestion 2

def main():
    N, T = map(int, input().split())
    A = list(map(int, input().split()))
    #N, T = 3, 281
    #A = [94, 94, 94]

=======
Suggestion 3

def main():
    n, t = map(int, input().split())
    a = list(map(int, input().split()))
    total = sum(a)
    t %= total
    for i in range(n):
        if t < a[i]:
            print(i+1, t)
            break
        t -= a[i]

=======
Suggestion 4

def main():
    N, T = map(int, input().split())
    A = list(map(int, input().split()))
    S = sum(A)
    T %= S
    for i in range(N):
        if T < A[i]:
            print(i+1, T)
            break
        else:
            T -= A[i]

=======
Suggestion 5

def main():
    n, t = map(int, input().split())
    a = list(map(int, input().split()))
    total = sum(a)
    t %= total

    for i in range(n):
        t -= a[i]
        if t < 0:
            print(i+1, a[i]+t)
            return

=======
Suggestion 6

def main():
    N, T = map(int, input().split())
    A = list(map(int, input().split()))
    sumA = sum(A)
    T = T % sumA
    for i in range(N):
        if T < A[i]:
            print(i+1, T)
            break
        T -= A[i]

=======
Suggestion 7

def main():
    N, T = map(int, input().split())
    A = list(map(int, input().split()))
    sum_A = sum(A)
    time = T % sum_A
    for i in range(N):
        if time >= A[i]:
            time -= A[i]
        else:
            print(i+1, time)
            break

=======
Suggestion 8

def main():
    N, T = map(int, input().split())
    A = list(map(int, input().split()))
    #print(N, T)
    #print(A)
    sum_A = sum(A)
    #print(sum_A)
    #print(T % sum_A)
    #print(T // sum_A)
    #print(T // sum_A * sum_A)
    #print(T - T // sum_A * sum_A)
    #print(T - T // sum_A * sum_A)
    #print(sum(A[:2]))
    #print(sum(A[:3]))
    #print(sum(A[:4]))
    #print(sum(A[:5]))
    #print(sum(A[:6]))
    #print(sum(A[:7]))
    #print(sum(A[:8]))
    #print(sum(A[:9]))
    #print(sum(A[:10]))
    #print(sum(A[:11]))
    #print(sum(A[:12]))
    #print(sum(A[:13]))
    #print(sum(A[:14]))
    #print(sum(A[:15]))
    #print(sum(A[:16]))
    #print(sum(A[:17]))
    #print(sum(A[:18]))
    #print(sum(A[:19]))
    #print(sum(A[:20]))
    #print(sum(A[:21]))
    #print(sum(A[:22]))
    #print(sum(A[:23]))
    #print(sum(A[:24]))
    #print(sum(A[:25]))
    #print(sum(A[:26]))
    #print(sum(A[:27]))
    #print(sum(A[:28]))
    #print(sum(A[:29]))
    #print(sum(A[:30]))
    #print(sum(A[:31]))
    #print(sum(A[:32]))
    #print(sum(A[:33]))
    #print(sum(A[:34]))
    #print(sum(A[:35]))
    #print(sum(A[:36]))
    #print(sum(A[:37]))
    #print(sum(A[:38]))
    #print(sum(A[:39]))
    #print(sum(A[:40]))
    #print(sum(A[:41]))
    #print(sum(A[:42]))
    #print(sum(A[:43]))
    #print(sum(A[:44]))
    #print(sum(A[:45]))
    #print(sum(A[:46]))
    #print(sum(A[:47]))
    #print(sum(A[:48]))
    #print(sum(A[:49]))
    #print(sum(A[:50]))
    #print(sum(A

=======
Suggestion 9

def main():
    n, t = map(int, input().split())
    a = list(map(int, input().split()))
    sum_a = sum(a)
    #print(sum_a)
    t = t % sum_a
    #print(t)
    for i in range(n):
        if t - a[i] < 0:
            print(i+1, t)
            break
        else:
            t = t - a[i]

=======
Suggestion 10

def main():
    N, T = map(int, input().split())
    A = list(map(int, input().split()))
    A_sum = sum(A)
    N_loop = T // A_sum
    T_mod = T % A_sum
    for i in range(N):
        if T_mod < A[i]:
            print(i + 1, T_mod)
            break
        else:
            T_mod -= A[i]
