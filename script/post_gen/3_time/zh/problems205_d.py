Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    pass

=======
Suggestion 2

def main():
    n,q = map(int,input().split())
    a = list(map(int,input().split()))
    k = [int(input()) for _ in range(q)]
    for i in k:
        j = 0
        while i > 0:
            j += 1
            if j not in a:
                i -= 1
        print(j)

=======
Suggestion 3

def main():
    n,q = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    k = []
    for i in range(q):
        k.append(int(input()))
    for i in range(q):
        count = 0
        for j in range(1, 1000000000000000000):
            if j not in a:
                count += 1
                if count == k[i]:
                    print(j)
                    break

=======
Suggestion 4

def main():
    n,q = map(int,input().split())
    a = list(map(int,input().split()))
    k = []
    for i in range(q):
        k.append(int(input()))
    a.sort()
    k.sort()
    count = 0
    for i in range(q):
        while a[count] <= k[i]:
            count += 1
        print(k[i] + count)

=======
Suggestion 5

def solve(n, q, a, k):
    # write your code here
    c = 0
    b = []
    for i in range(1, 10**18):
        if i not in a:
            c += 1
            b.append(i)
        if c == max(k):
            break
    return b[k-1]
    pass

n, q = map(int, input().split())
a = list(map(int, input().split()))
k = []
for i in range(q):
    k.append(int(input()))
print(solve(n, q, a, k))

=======
Suggestion 6

def main():
    num = input()
    num = num.split()
    n = int(num[0])
    q = int(num[1])
    a = input()
    a = a.split()
    a = [int(x) for x in a]
    k = []
    for i in range(q):
        k.append(int(input()))
    a.sort()
    b = []
    for i in range(n-1):
        b.append(a[i+1]-a[i]-1)
    b.insert(0,a[0]-1)
    for i in range(q):
        for j in range(n):
            if k[i] <= b[j]:
                print(a[j]+k[i])
                break
            else:
                k[i] = k[i]-b[j]

=======
Suggestion 7

def solve():
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    k = [int(input()) for _ in range(q)]
    # print(n, q, a, k)
    a.sort()
    # print(a)
    b = [a[0] - 1]
    for i in range(1, n):
        b.append(a[i] - a[i - 1] - 1)
    b.append(10 ** 18 - a[-1])
    # print(b)
    c = [0]
    for i in range(n + 1):
        c.append(c[-1] + b[i])
    # print(c)
    for i in range(q):
        left = 0
        right = n + 1
        while left < right:
            mid = (left + right) // 2
            if c[mid] >= k[i]:
                right = mid
            else:
                left = mid + 1
        print(a[left - 1] + (k[i] - c[left - 1]))

=======
Suggestion 8

def solve(n, q, a, k):
    # Write your code here
    # To print results to the standard output you can use print
    # Example print("Hello world!")
    if n < q:
        return
    index = 0
    for i in range(q):
        while True:
            index += 1
            if index not in a:
                k[i] -= 1
            if k[i] == 0:
                break
    return index

=======
Suggestion 9

def get_kth_num(k, n, a):
    if k > n * (10**18):
        return k - n * (10**18)
    for i in range(1, 10**18):
        if i not in a:
            k -= 1
            if k == 0:
                return i
