Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    cnt = 0
    for i in range(N-1):
        for j in range(i+1, N):
            if A[i] * A[j] in A:
                cnt += 1
    print(cnt)

=======
Suggestion 2

def main():
    N = int(input())
    A = list(map(int, input().split()))
    #A = [6, 2, 3]
    #A = [1, 3, 2, 4, 6, 8, 2, 2, 3, 7]
    #A = [2]
    #N = 1
    #N = 10
    #N = 3
    #A = [1, 2, 3]
    #A = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]
    #N = 10
    #A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    #A = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]
    #A = [1, 3, 2, 4, 6, 8, 2, 2, 3, 7]
    #A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    cnt = 0
    #print("A", A)
    for i in range(N):
        for j in range(N):
            for k in range(N):
                #print("i", i, "j", j, "k", k)
                if A[i] == 0 or A[j] == 0:
                    continue
                if A[i] / A[j] == A[k]:
                    #print("A[i]", A[i], "A[j]", A[j], "A[k]", A[k])
                    cnt += 1
    print(cnt)

=======
Suggestion 3

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    ans = 0
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                if a[i] * a[k] == a[j] ** 2:
                    ans += 1
    print(ans)

=======
Suggestion 4

def main():
    n = int(input())
    a = list(map(int, input().split()))

    # 1 <= i, j, k <= n
    # a[i] / a[j] = a[k]
    # a[i] = a[j] * a[k]
    # a[j] = a[i] / a[k]
    # a[k] = a[i] / a[j]
    # 1 <= a[i], a[j], a[k] <= 2 * 10^5
    # 1 <= a[j] * a[k] <= 4 * 10^10
    # 1 <= a[i] / a[k] <= 2 * 10^5
    # 1 <= a[i] / a[j] <= 2 * 10^5
    # 1 <= a[k] <= 2 * 10^5
    # 1 <= a[i] <= 2 * 10^5
    # 1 <= a[j] <= 2 * 10^5
    # 1 <= a[k] <= 2 * 10^5
    # 1 <= a[i] <= 2 * 10^5
    # 1 <= a[j] <= 2 * 10^5
    # 1 <= a[k] <= 2 * 10^5
    # 1 <= a[i] <= 2 * 10^5
    # 1 <= a[j] <= 2 * 10^5
    # 1 <= a[k] <= 2 * 10^5
    # 1 <= a[i] <= 2 * 10^5
    # 1 <= a[j] <= 2 * 10^5
    # 1 <= a[k] <= 2 * 10^5
    # 1 <= a[i] <= 2 * 10^5
    # 1 <= a[j] <= 2 * 10^5
    # 1 <= a[k] <= 2 * 10^5
    # 1 <= a[i] <= 2 * 10^5
    # 1 <= a[j] <= 2 * 10^5
    # 1 <= a[k] <= 2 * 10^5
    # 1 <= a[i

=======
Suggestion 5

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

n = int(input())
a = list(map(int, input().split()))

l = []
r = []

for i in range(n):
    l.append(gcd(a[i], a[0]))
    r.append(gcd(a[i], a[n - 1]))

for i in range(n - 1):
    l[i + 1] = gcd(l[i], l[i + 1])
    r[n - i - 2] = gcd(r[n - i - 1], r[n - i - 2])

ans = 0
for i in range(n):
    if i == 0:
        ans = max(ans, r[1])
    elif i == n - 1:
        ans = max(ans, l[n - 2])
    else:
        ans = max(ans, gcd(l[i - 1], r[i + 1]))

print(ans)

=======
Suggestion 6

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()

    cnt = 0
    for i in range(N):
        for j in range(i+1, N):
            for k in range(j+1, N):
                if A[i]/A[j] == A[k]:
                    cnt += 1
                elif A[i]/A[j] > A[k]:
                    break

    print(cnt)

=======
Suggestion 7

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    count = 0
    for i in range(n):
        for j in range(i+1, n):
            if a[i] / a[j] in a:
                count += 1
    print(count)
main()

=======
Suggestion 8

def main():
    N = int(input())
    A = list(map(int, input().split()))
    dic = {}
    ans = 0
    for i in range(N):
        if A[i] in dic:
            dic[A[i]] += 1
        else:
            dic[A[i]] = 1
    for i in range(N):
        for j in range(N):
            if A[i] == 0:
                continue
            if A[j] == 0:
                continue
            if A[i] == A[j]:
                ans += dic[A[i]] - 1
            else:
                if A[i] > A[j]:
                    if A[i] % A[j] == 0:
                        if A[i] // A[j] in dic:
                            ans += dic[A[i] // A[j]]
                else:
                    if A[j] % A[i] == 0:
                        if A[j] // A[i] in dic:
                            ans += dic[A[j] // A[i]]
    print(ans // 2)

=======
Suggestion 9

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    cnt = 0
    for i in range(N):
        for j in range(i+1, N):
            if A[i] == A[j]:
                cnt += 1
            elif A[j] % A[i] == 0:
                if A[j] // A[i] in A[j+1:]:
                    cnt += 1
    print(cnt)

=======
Suggestion 10

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    A.append(0)
    cnt = 0
    i = 0
    j = 0
    k = 1
    while i < N:
        if A[i] == A[i+1]:
            j += 1
            i += 1
        else:
            cnt += (j+1) * j // 2
            j = 0
            i += 1

    print(cnt)
