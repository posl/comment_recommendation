Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    ans = 0
    for i in range(N-2):
        for j in range(i+1,N-1):
            for k in range(j+1,N):
                if A[i] != A[j] and A[j] != A[k] and A[i] != A[k]:
                    if A[i] + A[j] > A[k]:
                        ans += 1
                    else:
                        break
    print(ans)

=======
Suggestion 2

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    ans = 0
    for i in range(N):
        for j in range(i+1, N):
            for k in range(j+1, N):
                if A[i] != A[j] and A[j] != A[k] and A[i] != A[k]:
                    ans += 1
    print(ans)
main()

=======
Suggestion 3

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    ans = 0
    for i in range(N-2):
        if A[i] == A[i+1]:
            continue
        for j in range(i+1, N-1):
            if A[j] == A[j+1]:
                continue
            ans += 1
    print(ans)

=======
Suggestion 4

def main():
    n = int(input())
    a = list(map(int, input().split()))
    cnt = [0] * (10**5 + 1)
    for i in range(n):
        cnt[a[i]] += 1
    ans = 0
    for i in range(1, 10**5+1):
        ans += cnt[i] * (cnt[i] - 1) * (cnt[i] - 2) // 6
    for i in range(1, 10**5-1):
        for j in range(i+1, 10**5):
            ans += cnt[i] * cnt[j] * (cnt[j] - 1) // 2
    for i in range(1, 10**5):
        for j in range(i+1, 10**5+1):
            ans += cnt[i] * (cnt[i] - 1) // 2 * cnt[j]
    print(ans)

=======
Suggestion 5

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    count = 0
    for i in range(N):
        for j in range(i+1,N):
            if A[i] == A[j]:
                continue
            for k in range(j+1,N):
                if A[j] == A[k] or A[i] == A[k]:
                    continue
                if A[i] + A[j] > A[k]:
                    count += 1
    print(count)

=======
Suggestion 6

def solve(n, a):
    from collections import Counter
    c = Counter(a)
    ans = 0
    for k, v in c.items():
        ans += v * (v - 1) * (v - 2) // 6
    for i in range(n):
        ans -= c[a[i]] * (c[a[i]] - 1) // 2 * (c[a[i]] - 2) // 3
    return ans

n = int(input())
a = list(map(int, input().split()))
print(solve(n, a))

=======
Suggestion 7

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    a.append(0)
    ans = 0
    cnt = 0
    for i in range(n):
        if a[i] == a[i+1]:
            cnt += 1
        else:
            ans += cnt * (cnt+1) // 2
            cnt = 0
    for i in range(n):
        if a[i] == a[i+1]:
            cnt += 1
        else:
            ans -= cnt * (cnt+1) // 2
            cnt = 0
    print(ans)

=======
Suggestion 8

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    A.append(-1)
    cnt = 0
    tmp = 0
    for i in range(N-1):
        if A[i] == A[i+1]:
            tmp += 1
        else:
            cnt += tmp*(tmp+1)//2
            tmp = 0
    print(cnt)

=======
Suggestion 9

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    #print(A)
    #print(len(A))
    count = 0
    for i in range(N-2):
        for j in range(i+1, N-1):
            for k in range(j+1, N):
                #print(i, j, k)
                if A[i] != A[j] and A[j] != A[k] and A[i] != A[k]:
                    #print("OK")
                    count += 1
    print(count)
