Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    l = -10**18
    r = 10**18
    while l+1<r:
        x = (l+r)//2
        cnt = 0
        for i in range(N):
            if A[i] < 0:
                l2 = -1
                r2 = N
                while l2+1<r2:
                    x2 = (l2+r2)//2
                    if A[i] * A[x2] < x:
                        r2 = x2
                    else:
                        l2 = x2
                cnt += N-r2
            else:
                l2 = -1
                r2 = N
                while l2+1<r2:
                    x2 = (l2+r2)//2
                    if A[i] * A[x2] < x:
                        l2 = x2
                    else:
                        r2 = x2
                cnt += r2
        cnt //= 2
        if cnt < K:
            l = x
        else:
            r = x
    print(l)

=======
Suggestion 2

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    A_plus = []
    A_minus = []
    for i in range(N):
        if A[i] > 0:
            A_plus.append(A[i])
        else:
            A_minus.append(A[i])
    # print(A_plus, A_minus)
    A_plus.reverse()
    num = 0
    if K <= len(A_plus) * len(A_minus):
        for i in range(len(A_plus)):
            for j in range(len(A_minus)):
                num += 1
                if num == K:
                    print(A_plus[i] * A_minus[j])
                    exit()
    else:
        K -= len(A_plus) * len(A_minus)
        for i in range(len(A_plus)):
            for j in range(i + 1, len(A_plus)):
                num += 1
                if num == K:
                    print(A_plus[i] * A_plus[j])
                    exit()
        for i in range(len(A_minus)):
            for j in range(i + 1, len(A_minus)):
                num += 1
                if num == K:
                    print(A_minus[i] * A_minus[j])
                    exit()
        print(0)
        exit()

=======
Suggestion 3

def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    l = 0
    r = 0
    for i in range(n):
        if a[i] < 0:
            l += 1
        else:
            r += 1
    ans = 0
    if l * r >= k:
        for i in range(l):
            for j in range(r):
                ans += 1
                if ans == k:
                    print(a[i] * a[n - 1 - j])
                    exit()
    else:
        for i in range(l):
            for j in range(i + 1, l):
                ans += 1
                if ans == k:
                    print(a[i] * a[j])
                    exit()
        for i in range(r):
            for j in range(i + 1, r):
                ans += 1
                if ans == k:
                    print(a[n - 1 - i] * a[n - 1 - j])
                    exit()
        for i in range(l):
            for j in range(r):
                ans += 1
                if ans == k:
                    print(a[i] * a[n - 1 - j])
                    exit()

=======
Suggestion 4

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    l = 0
    r = 0
    for i in range(N):
        if A[i] < 0:
            l += 1
        elif A[i] > 0:
            r += 1
    if l * r >= K:
        print(A[l] * A[-r])
        return
    else:
        K -= l * r
        if K <= ((l * (l - 1)) / 2) + ((r * (r - 1)) / 2):
            if K <= ((l * (l - 1)) / 2):
                for i in range(l - 1):
                    for j in range(i + 1, l):
                        K -= 1
                        if K == 0:
                            print(A[i] * A[j])
                            return
            else:
                for i in range(r - 1):
                    for j in range(i + 1, r):
                        K -= 1
                        if K == 0:
                            print(A[-j] * A[-i])
                            return
        else:
            K -= ((l * (l - 1)) / 2) + ((r * (r - 1)) / 2)
            for i in range(l):
                for j in range(r):
                    K -= 1
                    if K == 0:
                        print(A[-j] * A[i])
                        return

=======
Suggestion 5

def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    #print(a)
    l = -10**18
    r = 10**18
    while l+1<r:
        x = (l+r)//2
        cnt = 0
        for i in range(n):
            if a[i]<0:
                l2 = -1
                r2 = n
                while l2+1<r2:
                    x2 = (l2+r2)//2
                    if a[i]*a[x2]<x:
                        r2 = x2
                    else:
                        l2 = x2
                cnt += n-r2
            else:
                l2 = -1
                r2 = n
                while l2+1<r2:
                    x2 = (l2+r2)//2
                    if a[i]*a[x2]<x:
                        l2 = x2
                    else:
                        r2 = x2
                cnt += r2
            if a[i]**2<x:
                cnt -= 1
        cnt //= 2
        if cnt<k:
            l = x
        else:
            r = x
    print(l)

=======
Suggestion 6

def solve():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    if A[0] < 0 and A[-1] < 0:
        if K <= ((N*(N-1))//2):
            return A[K-1]
        else:
            return A[0] * A[-1] // A[K-N*(N-1)//2-1]
    elif A[0] < 0 and A[-1] >= 0:
        cnt = 0
        for i in range(N):
            if A[i] < 0:
                cnt += N-i-1
            else:
                break
        if K <= cnt:
            return A[K-1]
        elif K > ((N*(N-1))//2 - cnt):
            return A[0] * A[-1] // A[K-N*(N-1)//2+cnt-1]
        else:
            return A[0] * A[-1] // A[cnt+K-1]
    else:
        if K <= ((N*(N-1))//2):
            return A[K-1]
        else:
            return A[0] * A[-1] // A[K-N*(N-1)//2-1]

print(solve())

=======
Suggestion 7

def main():
    n,k = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    l = -10**18
    r = 10**18
    while (r - l) > 1:
        mid = (l + r) // 2
        cnt = 0
        for i in range(n):
            if a[i] < 0:
                #print('a[i] < 0')
                l = mid
                continue
            #print('a[i] >= 0')
            if a[i] == 0:
                if mid >= 0:
                    cnt += n - i - 1
            else:
                if a[i] * a[-1] <= mid:
                    cnt += n - i - 1
                else:
                    l = mid
                    continue
            #print('cnt = ' + str(cnt))
            low = i + 1
            high = n - 1
            while (high - low) > 1:
                mid2 = (low + high) // 2
                if a[i] * a[mid2] <= mid:
                    low = mid2
                else:
                    high = mid2
            cnt += low - i
            #print('cnt = ' + str(cnt))
        if cnt < k:
            l = mid
        else:
            r = mid
    print(r)

=======
Suggestion 8

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    A = [a for a in A if a < 0]
    B = list(reversed(A))
    C = []
    D = []
    for i in range(len(A)):
        for j in range(i + 1, len(A)):
            C.append(A[i] * A[j])
    for i in range(len(B)):
        for j in range(i + 1, len(B)):
            D.append(B[i] * B[j])
    E = C + D
    E.sort()
    print(E[K - 1])

=======
Suggestion 9

def solve():
    # まずは入力を受け取る
    N, K = map(int, input().split())
    A = list(map(int, input().split()))

    # ここからコードを書く
    A.sort()
    #print(A)
    #print(A[K-1])
    print(A[K-1])

=======
Suggestion 10

def problem155_d():
    N,K = map(int,input().split())
    A = list(map(int,input().split()))
    A.sort()
    print(A)
    print(A[K])
