Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    K, N = map(int, input().split())
    A = list(map(int, input().split()))
    max_dist = 0
    for i in range(N):
        if i == N-1:
            dist = K - A[i] + A[0]
        else:
            dist = A[i+1] - A[i]
        if dist > max_dist:
            max_dist = dist
    print(K - max_dist)

=======
Suggestion 2

def main():
    k, n = map(int, input().split())
    a = list(map(int, input().split()))

    max_distance = 0
    for i in range(n - 1):
        max_distance = max(max_distance, a[i + 1] - a[i])

    max_distance = max(max_distance, k - a[n - 1] + a[0])

    print(k - max_distance)

=======
Suggestion 3

def main():
    K, N = map(int, input().split())
    A = list(map(int, input().split()))
    A.append(A[0] + K)

    max = 0
    for i in range(N):
        if A[i+1] - A[i] > max:
            max = A[i+1] - A[i]

    print(K - max)

=======
Suggestion 4

def main():
    k, n = map(int, input().split())
    a = list(map(int, input().split()))
    a.append(a[0]+k)
    max = 0
    for i in range(n):
        if max < a[i+1] - a[i]:
            max = a[i+1] - a[i]
    print(k-max)

=======
Suggestion 5

def main():
    K, N = map(int, input().split())
    A = list(map(int, input().split()))
    A = A + [K + A[0]]
    max_d = 0
    for i in range(N):
        d = A[i+1] - A[i]
        if d > max_d:
            max_d = d
    print(K - max_d)

=======
Suggestion 6

def main():
  K, N = map(int, input().split())
  A = list(map(int, input().split()))

  max_dist = 0
  for i in range(N):
    if i == 0:
      max_dist = max(max_dist, K - A[i] + A[i+1])
    elif i == N - 1:
      max_dist = max(max_dist, A[i] - A[i-1] + K - A[i])
    else:
      max_dist = max(max_dist, A[i] - A[i-1], K - A[i] + A[i+1])

  print(K - max_dist)

=======
Suggestion 7

def solve(k,n,a):
    distance = []
    for i in range(n):
        if i == n-1:
            distance.append(k-a[i]+a[0])
        else:
            distance.append(a[i+1]-a[i])
    distance.sort()
    distance.pop()
    return sum(distance)
k,n = map(int,input().split())
a = list(map(int,input().split()))
print(solve(k,n,a))

=======
Suggestion 8

def main():
    k, n = map(int, input().split())
    a = list(map(int, input().split()))
    max = 0
    for i in range(n):
        if i == n-1:
            if a[0] - a[i] > max:
                max = a[0] - a[i]
        else:
            if a[i+1] - a[i] > max:
                max = a[i+1] - a[i]
    print(k-max)
main()

=======
Suggestion 9

def main():
    k, n = map(int, input().split())
    a = list(map(int, input().split()))

    a.append(a[0] + k)
    max = 0

    for i in range(n):
        d = a[i + 1] - a[i]
        if d > max:
            max = d

    print(k - max)
