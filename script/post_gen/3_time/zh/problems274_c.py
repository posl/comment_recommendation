Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = [0] * (2 * n + 1)
    for i in range(n):
        ans[a[i]] = i + 1
    for i in range(2 * n - 1, 0, -1):
        ans[i // 2] = min(ans[i // 2], ans[i] + 1)
    for i in range(1, 2 * n + 1):
        print(ans[i])

=======
Suggestion 2

def get_distance(n, a):
    a.insert(0, 0)
    b = [0] * (2 * n + 1)
    for i in range(1, n + 1):
        b[i] = 1
    for i in range(1, n):
        b[a[i]] += b[i]
        b[a[i] + 1] += b[i]
    b[2 * n] += b[n]
    for i in range(n + 1, 2 * n):
        b[a[i]] += b[i]
        b[a[i] + 1] += b[i]
    return b

=======
Suggestion 3

def main():
    n = int(input())
    a = [int(i) for i in input().split()]
    a.insert(0, 0)
    b = [0]*(2*n+1)
    for i in range(1, n+1):
        b[a[i]] = i
    for i in range(1, n+1):
        j = b[i]
        ans = 0
        while j > 1:
            j //= 2
            ans += 1
        print(ans)

=======
Suggestion 4

def solve():
    n = int(input())
    a = list(map(int, input().split()))
    ans = [0] * (2 * n + 1)
    for i in range(n):
        ans[a[i]] = i + 1
    for i in range(2 * n - 1, 0, -1):
        if ans[i] > ans[i + 1]:
            ans[i] = ans[i + 1] + 1
    for i in range(1, 2 * n + 1):
        print(ans[i])

=======
Suggestion 5

def main():
    #n = int(input())
    #a = list(map(int, input().split()))
    n = 4
    a = [1,3,5,2]
    #n = 2
    #a = [1,2]
    #n = 3
    #a = [1,3,2]
    #n = 5
    #a = [1,3,5,2,4]
    #n = 6
    #a = [1,3,5,2,4,6]
    #n = 7
    #a = [1,3,5,7,2,4,6]
    #n = 8
    #a = [1,3,5,7,2,4,6,8]
    #n = 9
    #a = [1,3,5,7,9,2,4,6,8]
    #n = 10
    #a = [1,3,5,7,9,2,4,6,8,10]
    #n = 11
    #a = [1,3,5,7,9,11,2,4,6,8,10]
    #n = 12
    #a = [1,3,5,7,9,11,2,4,6,8,10,12]
    #n = 13
    #a = [1,3,5,7,9,11,13,2,4,6,8,10,12]
    #n = 14
    #a = [1,3,5,7,9,11,13,2,4,6,8,10,12,14]
    #n = 15
    #a = [1,3,5,7,9,11,13,15,2,4,6,8,10,12,14]
    #n = 16
    #a = [1,3,5,7,9,11,13,15,2,4,6,8,10,12,14,16]
    #n = 17
    #a = [1,3,5,7,9,11,13,15,17,2

=======
Suggestion 6

def get_distance(n, a):
    # print("n: ", n)
    # print("a: ", a)
    # print("len(a): ", len(a))
    # print("len(a) * 2 + 1: ", len(a) * 2 + 1)

    distance = [0] * (len(a) * 2 + 1)

    # print("distance: ", distance)

    for i in range(n):
        # print("i: ", i)
        # print("a[i]: ", a[i])
        # print("distance[a[i]]: ", distance[a[i]])
        distance[a[i]] = 0
        # print("distance: ", distance)
        # print("a[i] * 2: ", a[i] * 2)
        # print("distance[a[i] * 2]: ", distance[a[i] * 2])
        distance[a[i] * 2] = distance[a[i]] + 1
        # print("distance: ", distance)
        # print("a[i] * 2 + 1: ", a[i] * 2 + 1)
        # print("distance[a[i] * 2 + 1]: ", distance[a[i] * 2 + 1])
        distance[a[i] * 2 + 1] = distance[a[i]] + 1
        # print("distance: ", distance)

    # print("distance: ", distance)
    return distance

=======
Suggestion 7

def distance(N,A):
    #初始化
    distance = [0]*(2*N+1)
    distance[1] = 0
    #计算
    for i in range(1,N+1):
        distance[2*i] = distance[i] + 1
        distance[2*i+1] = distance[i] + 1
    #返回
    return distance

=======
Suggestion 8

def solve():
    n = int(input())
    a = list(map(int, input().split()))
    b = [0]*(2*n+1)
    for i in range(n):
        b[a[i]] = i+1
    for i in range(1, 2*n+1):
        j = i
        while j != 1:
            print(b[j], end=' ')
            j //= 2
        print(0)

=======
Suggestion 9

def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = [0] * (2 * n + 1)
    for i in range(n):
        ans[a[i]] = i + 1
    for i in range(2 * n, 0, -1):
        if ans[i] == 0:
            continue
        if i % 2 == 0:
            ans[i // 2] = ans[i]
        else:
            ans[i // 2] = ans[i] + 1
    for i in range(2 * n + 1):
        print(ans[i])

=======
Suggestion 10

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = [0] * (2 * n + 1)
    for i in range(n):
        b[a[i]] = i + 1
    c = [0] * (2 * n + 1)
    for i in range(2 * n, 0, -1):
        if i * 2 + 1 <= 2 * n:
            c[i] = max(c[i * 2], c[i * 2 + 1]) + 1
        elif i * 2 <= 2 * n:
            c[i] = c[i * 2] + 1
    for i in range(1, 2 * n + 1):
        print(c[1] - c[i])
