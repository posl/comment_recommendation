Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    K = int(input())
    lunlun = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    for i in range(K-1):
        x = lunlun[i]
        if x % 10 != 0:
            lunlun.append(10 * x + x % 10 - 1)
        lunlun.append(10 * x + x % 10)
        if x % 10 != 9:
            lunlun.append(10 * x + x % 10 + 1)
    print(lunlun[K-1])

=======
Suggestion 2

def solve():
    from collections import deque
    K = int(input())
    Q = deque([1,2,3,4,5,6,7,8,9])
    for i in range(K):
        x = Q.popleft()
        if x%10 != 0:
            Q.append(10*x + x%10 - 1)
        Q.append(10*x + x%10)
        if x%10 != 9:
            Q.append(10*x + x%10 + 1)
    print(x)

solve()

=======
Suggestion 3

def lunlun(n):
    if n < 10:
        return True
    else:
        a = str(n)
        for i in range(len(a)-1):
            if abs(int(a[i]) - int(a[i+1])) > 1:
                return False
        return True

=======
Suggestion 4

def main():
    K = int(input())
    lunlun = [1,2,3,4,5,6,7,8,9]
    for i in range(1, K):
        n = lunlun[i]
        last = n % 10
        if last > 0:
            lunlun.append(n * 10 + last - 1)
        lunlun.append(n * 10 + last)
        if last < 9:
            lunlun.append(n * 10 + last + 1)
    print(lunlun[K - 1])

main()

=======
Suggestion 5

def lunlun(k):
    import sys
    from collections import deque
    q = deque([1, 2, 3, 4, 5, 6, 7, 8, 9])
    for i in range(k):
        x = q.popleft()
        if x % 10 != 0:
            q.append(10 * x + x % 10 - 1)
        q.append(10 * x + x % 10)
        if x % 10 != 9:
            q.append(10 * x + x % 10 + 1)
    print(x)

=======
Suggestion 6

def lunlun(n):
    queue = [1,2,3,4,5,6,7,8,9]
    for i in range(n):
        ret = queue.pop(0)
        if ret%10 != 0:
            queue.append(ret*10 + ret%10 - 1)
        queue.append(ret*10 + ret%10)
        if ret%10 != 9:
            queue.append(ret*10 + ret%10 + 1)
    return ret

n = int(input())
print(lunlun(n))

=======
Suggestion 7

def lunlun(n):
    if n < 10:
        return [n]
    else:
        return [int(str(n)[0]) * 10 ** (len(str(n)) - 1) + i for i in lunlun(n % 10 ** (len(str(n)) - 1)) if abs(int(str(n)[0]) - i) <= 1]

=======
Suggestion 8

def lunlun(n):
    if n < 10:
        return [n]
    else:
        ans = []
        for i in range(10):
            if i == n % 10:
                ans += [int(str(n) + str(i))]
            elif i == n % 10 - 1:
                ans += [int(str(n) + str(i))]
            elif i == n % 10 + 1:
                ans += [int(str(n) + str(i))]
        return ans

n = int(input())
lunlun_list = []
for i in range(10):
    lunlun_list += lunlun(i)
lunlun_list.sort()
print(lunlun_list[n - 1])

from collections import deque

K = int(input())

q = deque(range(1, 10))
for i in range(K):
    a = q.popleft()
    if a % 10 != 0:
        q.append(10 * a + a % 10 - 1)
    q.append(10 * a + a % 10)
    if a % 10 != 9:
        q.append(10 * a + a % 10 + 1)

print(a)

from collections import deque

K = int(input())

q = deque(range(1, 10))
for i in range(K):
    a = q.popleft()
    if a % 10 != 0:
        q.append(10 * a + a % 10 - 1)
    q.append(10 * a + a % 10)
    if a % 10 != 9:
        q.append(10 * a + a % 10 + 1)

print(a)

from collections import deque

K = int(input())

q = deque(range(1, 10))
for i in range(K):
    a = q.popleft()
    if a % 10 != 0:
        q.append(10 * a + a % 10 - 1)
    q.append(10 * a + a % 10)
    if a % 10 != 9:
        q.append(10 * a + a % 10 + 1)

print(a)

from collections import deque

K = int(input())

q = deque(range(1, 10))
for i in range(K):
    a = q.popleft()
    if a % 10 != 0:

=======
Suggestion 9

def lunlun(n):
    if n<10:
        return n
    else:
        a = []
        b = []
        for i in range(1,10):
            a.append(i)
        for j in range(n-1):
            b = []
            for k in a[j]:
                if k==0:
                    b.append(k+1)
                elif k==9:
                    b.append(k-1)
                else:
                    b.append(k+1)
                    b.append(k-1)
        a.append(b)
        return a

=======
Suggestion 10

def lunlun(K):
    if K == 1:
        return 1
    else:
        return lunlun(K-1) + 1

K = int(input())
print(lunlun(K))

In the above code, I made a recursive function to find the K-th smallest lunlun number. But it is too slow to get the answer. I will try to make it faster.
