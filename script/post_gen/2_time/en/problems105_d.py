Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    S = [0] * (N + 1)
    for i in range(N):
        S[i + 1] = (S[i] + A[i]) % M
    from collections import Counter
    C = Counter(S)
    ans = 0
    for v in C.values():
        ans += v * (v - 1) // 2
    print(ans)

main()

=======
Suggestion 2

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = [0] * (N + 1)
    for i in range(N):
        B[i + 1] = (B[i] + A[i]) % M
    d = {}
    for i in range(N + 1):
        d.setdefault(B[i], 0)
        d[B[i]] += 1
    ans = 0
    for k, v in d.items():
        ans += v * (v - 1) // 2
    print(ans)

=======
Suggestion 3

def main():
    from collections import defaultdict
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    d = defaultdict(int)
    d[0] = 1
    ans = 0
    s = 0
    for i in range(n):
        s += a[i]
        ans += d[s % m]
        d[s % m] += 1
    print(ans)

main()

=======
Suggestion 4

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A = [a % M for a in A]
    A = [0] + A
    for i in range(N):
        A[i+1] = (A[i+1] + A[i]) % M

    from collections import defaultdict
    D = defaultdict(int)
    for a in A:
        D[a] += 1

    ans = 0
    for d in D.values():
        ans += d * (d-1) // 2

    print(ans)

main()

I think the problem is that I am using defaultdict(int) , but I don't know how to use defaultdict(list) .

I tried defaultdict(list) and append() , but it doesn't work.

I have a list of tuples, each tuple has a name and a value. I want to sort the list by the value, and if the value is the same, sort by the name.

I have tried to use the following code:

=======
Suggestion 5

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))

    sum_mod_M = [0] * (N + 1)
    for i in range(N):
        sum_mod_M[i + 1] = (sum_mod_M[i] + A[i]) % M

    ans = 0
    from collections import Counter
    cnt = Counter(sum_mod_M)
    for v in cnt.values():
        ans += v * (v - 1) // 2

    print(ans)

=======
Suggestion 6

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    for i in range(n):
        a[i] %= m
    sum = [0] * (n + 1)
    for i in range(n):
        sum[i + 1] = (sum[i] + a[i]) % m
    sum.sort()
    ans = 0
    cnt = 1
    for i in range(n):
        if sum[i] == sum[i + 1]:
            cnt += 1
        else:
            ans += cnt * (cnt - 1) // 2
            cnt = 1
    ans += cnt * (cnt - 1) // 2
    print(ans)

=======
Suggestion 7

def solve():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A = [a % M for a in A]
    A = [0] + A
    for i in range(N):
        A[i + 1] += A[i]
        A[i + 1] %= M
    from collections import defaultdict
    d = defaultdict(int)
    for a in A:
        d[a] += 1
    ans = 0
    for k, v in d.items():
        ans += (v * (v - 1)) // 2
    print(ans)

=======
Suggestion 8

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    #print(N, M, A)
    S = [0]
    for a in A:
        S.append((S[-1] + a) % M)
    #print(S)
    from collections import defaultdict
    d = defaultdict(int)
    for s in S:
        d[s] += 1
    #print(d)
    ans = 0
    for v in d.values():
        ans += v * (v-1) // 2
    print(ans)

=======
Suggestion 9

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    #print(N, M)
    #print(A)
    #print(sum(A))
    #print(sum(A) % M)
    
    mod = [0] * M
    mod[0] = 1
    
    cnt = 0
    sm = 0
    for i in range(N):
        sm += A[i]
        mod[sm % M] += 1
    
    for m in mod:
        cnt += m * (m - 1) // 2
    
    print(cnt)

=======
Suggestion 10

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))

    # Initialize the array to store the number of candies in each box
    candies = [0] * (N+1)
    for i in range(N):
        candies[i+1] = candies[i] + A[i]

    # Initialize the array to store the number of boxes with each sum of candies
    box = [0] * M
    for i in range(N+1):
        box[candies[i] % M] += 1

    # Calculate the number of pairs
    ans = 0
    for i in range(M):
        ans += box[i]*(box[i]-1)//2

    # Output
    print(ans)
