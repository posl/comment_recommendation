Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    s = [0] * (n + 1)
    for i in range(n):
        s[i + 1] = s[i] + a[i]
    d = {}
    for i in range(n + 1):
        t = s[i] % m
        if t in d:
            d[t] += 1
        else:
            d[t] = 1
    ans = 0
    for i in d:
        ans += d[i] * (d[i] - 1) // 2
    print(ans)

=======
Suggestion 2

def solve():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    S = [0] * (N + 1)
    for i in range(N):
        S[i + 1] = (S[i] + A[i]) % M
    from collections import Counter
    C = Counter(S)
    ans = 0
    for k, v in C.items():
        ans += v * (v - 1) // 2
    print(ans)

solve()

=======
Suggestion 3

def readinput():
    n,m=list(map(int,input().split()))
    a=list(map(int,input().split()))
    return n,m,a

=======
Suggestion 4

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A = [0] + A
    for i in range(1, N+1):
        A[i] += A[i-1]
    A = [a % M for a in A]
    A.sort()
    A.append(1)
    ans = 0
    now = 0
    cnt = 0
    for a in A:
        if a == now:
            cnt += 1
        else:
            ans += cnt * (cnt-1) // 2
            now = a
            cnt = 1
    print(ans)

=======
Suggestion 5

def read_ints():
    return list(map(int, input().split()))

N, M = read_ints()
A = read_ints()

S = [0] * (N + 1)
for i in range(N):
    S[i + 1] = (S[i] + A[i]) % M

from collections import Counter
C = Counter(S)

ans = 0
for k, v in C.items():
    ans += v * (v - 1) // 2

print(ans)

=======
Suggestion 6

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    for i in range(N):
        if i == 0:
            A[i] %= M
        else:
            A[i] = (A[i - 1] + A[i]) % M
    A.sort()
    ans = 0
    for i in range(N):
        if A[i] == 0:
            ans += 1
    for i in range(N):
        if i > 0 and A[i - 1] == A[i]:
            ans += 1
    print(ans)

=======
Suggestion 7

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A = [a%M for a in A]
    A = [0] + A
    for i in range(1, N+1):
        A[i] = (A[i-1] + A[i])%M
    from collections import Counter
    c = Counter(A)
    ans = 0
    for k in c:
        ans += c[k]*(c[k]-1)//2
    print(ans)

=======
Suggestion 8

def get_input():
    input_line = input()
    input_line = input_line.split()
    num_boxes = int(input_line[0])
    num_children = int(input_line[1])
    input_line = input()
    input_line = input_line.split()
    candies = [int(i) for i in input_line]
    return num_boxes, num_children, candies

=======
Suggestion 9

def find_pairs(N, M, A):
    sums = [0] * (N + 1)
    for i in range(N):
        sums[i + 1] = sums[i] + A[i]
    sums = [s % M for s in sums]
    sums.sort()
    count = 1
    result = 0
    for i in range(1, N + 1):
        if sums[i] == sums[i - 1]:
            count += 1
        else:
            result += count * (count - 1) // 2
            count = 1
    result += count * (count - 1) // 2
    return result

=======
Suggestion 10

def findPairs(arr, n, m):
    # Create an empty hashmap to store
    # ending value of prefixes.
    mp = {}
    # Initialize count of even
    # and odd sum pairs.
    evenSum = 0
    oddSum = 0
    # Traverse through all prefixes.
    for i in range(n):
        # Find ending index of prefix.
        rem = arr[i] % m
        # If rem == 0, then add 1 to evenSum
        if (rem == 0):
            evenSum += 1
        else:
            oddSum += 1
        # If this sum is seen before,
        # then update count of even
        # and odd sum pairs.
        if rem in mp.keys():
            evenSum += mp[rem]
        else:
            mp[rem] = 0
        mp[rem] += 1
    # Return count of even and odd
    # sum pairs.
    return (evenSum * (evenSum - 1) // 2 + oddSum * (oddSum - 1) // 2 + evenSum)

n, m = map(int, input().split())
arr = list(map(int, input().split()))
print(findPairs(arr, n, m))
