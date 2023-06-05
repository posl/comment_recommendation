Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n,k=map(int,input().split())
    a=list(map(int,input().split()))
    ans=0
    for i in range(n-k):
        if a[i]>=a[i+k]:
            ans+=1
    print(ans)

=======
Suggestion 2

def getMinOpNum(n, k, a):
    minNum = min(a)
    minNumIndex = a.index(minNum)
    if minNumIndex < k-1:
        return minNumIndex + 1 + getMinOpNum(n, k, a[minNumIndex+1:])
    elif minNumIndex > n - k:
        return n - minNumIndex + getMinOpNum(n, k, a[:minNumIndex])
    else:
        return minNumIndex + 1

=======
Suggestion 3

def get_input():
    n,k = [int(x) for x in input().split()]
    a = [int(x) for x in input().split()]
    return n,k,a

=======
Suggestion 4

def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    count = 0
    while True:
        if n <= k:
            count += 1
            break
        else:
            n = n - k + 1
            count += 1
    print(count)

=======
Suggestion 5

def solve():
    pass

=======
Suggestion 6

def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    # print(n, k, a)
    # n, k = 4, 3
    # a = [2, 3, 1, 4]
    # n, k = 3, 3
    # a = [1, 2, 3]
    # n, k = 8, 3
    # a = [7, 3, 1, 8, 4, 6, 2, 5]
    # n, k = 3, 2
    # a = [2, 1, 3]
    # n, k = 5, 3
    # a = [1, 3, 4, 5, 2]
    # n, k = 5, 2
    # a = [5, 3, 4, 1, 2]
    # n, k = 5, 3
    # a = [1, 2, 3, 4, 5]
    # n, k = 5, 3
    # a = [3, 5, 1, 2, 4]
    # n, k = 5, 3
    # a = [5, 3, 4, 1, 2]
    # n, k = 5, 2
    # a = [5, 3, 4, 1, 2]
    # n, k = 5, 3
    # a = [1, 2, 3, 4, 5]
    # n, k = 5, 3
    # a = [1, 2, 3, 4, 5]
    # n, k = 5, 3
    # a = [5, 3, 4, 1, 2]
    # n, k = 5, 3
    # a = [1, 2, 3, 4, 5]
    # n, k = 5, 3
    # a = [5, 3, 4, 1, 2]
    # n, k =

=======
Suggestion 7

def main():
    n,k = map(int,input().split())
    a = [int(x) for x in input().split()]
    print(n,k,a)

=======
Suggestion 8

def main():
    n,k = map(int,input().split())
    a = list(map(int,input().split()))
    if k == 1:
        print(n-1)
    else:
        print((n-2)//(k-1)+1)

=======
Suggestion 9

def min_num(a, b):
    if a <= b:
        return a
    else:
        return b

=======
Suggestion 10

def problems101_c():
    n,k = map(int,input().split())
    a = list(map(int,input().split()))
    print((n-2)//(k-1)+1)
    
# problems101_c()
