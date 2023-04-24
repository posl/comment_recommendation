Synthesizing 9/10 solutions

=======
Suggestion 1

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    A = [a-1 for a in A]
    #print(N, K)
    #print(A)
    #
    # 1. find cycle
    #
    # 1.1. find cycle length
    cycle = []
    visited = [False for _ in range(N)]
    i = 0
    while not visited[i]:
        visited[i] = True
        cycle.append(i)
        i = A[i]
    cycle.append(i)
    cycle_len = len(cycle) - 1
    #print(cycle)
    #print(cycle_len)
    #
    # 1.2. find cycle start
    cycle_start = cycle.index(i)
    #print(cycle_start)
    #
    # 2. find cycle destination
    #
    # 2.1. find cycle destination by cycle length
    cycle_dest = cycle[(K % cycle_len) + cycle_start]
    #print(cycle_dest)
    #
    # 2.2. find cycle destination by cycle start
    if K >= cycle_start:
        cycle_dest = cycle[(K - cycle_start) % cycle_len + cycle_start]
    #print(cycle_dest)
    #
    # 3. output
    print(cycle_dest + 1)

=======
Suggestion 2

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    visited = [0] * N
    current = 0
    for i in range(K):
        if visited[current]:
            break
        visited[current] = i + 1
        current = A[current] - 1
    else:
        print(current + 1)
        return

    cycle = i + 1 - visited[current]
    K -= visited[current]
    K %= cycle
    for i in range(K):
        current = A[current] - 1
    print(current + 1)

=======
Suggestion 3

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    route = [1]
    next = A[0]
    while True:
        if next == 1:
            break
        else:
            route.append(next)
            next = A[next-1]
    if K < len(route):
        print(route[K])
    else:
        K -= len(route)
        route.pop(0)
        K %= len(route)
        print(route[K])

=======
Suggestion 4

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    A = [a - 1 for a in A]
    #print(A)
    #print(N, K)
    #print(A)
    #print(A[1])
    #print(A[2])
    #print(A[3])
    #print(A[4])
    #print(A[5])
    #print(A[6])
    #print(A[7])
    #print(A[8])
    #print(A[9])
    #print(A[10])
    #print(A[11])
    #print(A[12])
    #print(A[13])
    #print(A[14])
    #print(A[15])
    #print(A[16])
    #print(A[17])
    #print(A[18])
    #print(A[19])
    #print(A[20])
    #print(A[21])
    #print(A[22])
    #print(A[23])
    #print(A[24])
    #print(A[25])
    #print(A[26])
    #print(A[27])
    #print(A[28])
    #print(A[29])
    #print(A[30])
    #print(A[31])
    #print(A[32])
    #print(A[33])
    #print(A[34])
    #print(A[35])
    #print(A[36])
    #print(A[37])
    #print(A[38])
    #print(A[39])
    #print(A[40])
    #print(A[41])
    #print(A[42])
    #print(A[43])
    #print(A[44])
    #print(A[45])
    #print(A[46])
    #print(A[47])
    #print(A[48])
    #print(A[49])
    #print(A[50])
    #print(A[51])
    #print(A[52])
    #print(A[53])
    #print(A[54])
    #print(A[55])
    #print(A[56])
    #print(A[57])
    #print(A[58])
    #print(A[59])
    #print(A[60])
    #print(A[61])
    #print(A[62])
    #print(A[63])
    #print(A

=======
Suggestion 5

def main():
    N, K = [int(x) for x in input().split()]
    A = [int(x) for x in input().split()]
    A.insert(0, 0)
    route = [1]
    current = 1
    for i in range(K):
        current = A[current]
        if current in route:
            break
        route.append(current)
    if len(route) == K:
        print(current)
    else:
        print(route[(K - len(route)) % (len(route) - route.index(current)) + route.index(current)])

=======
Suggestion 6

def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    a = [i - 1 for i in a]
    #print(a)
    #print(n, k)
    #print(a)
    #print(a[0])
    #print(a[a[0]])
    #print(a[a[a[0]]])
    #print(a[a[a[a[0]]]])
    #print(a[a[a[a[a[0]]]]])
    #print(a[a[a[a[a[a[0]]]]]])
    #print(a[a[a[a[a[a[a[0]]]]]]])
    #print(a[a[a[a[a[a[a[a[0]]]]]]]])
    #print(a[a[a[a[a[a[a[a[a[0]]]]]]]]])
    #print(a[a[a[a[a[a[a[a[a[a[0]]]]]]]]]])

=======
Suggestion 7

def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    a.insert(0, 0)
    b = [1]
    c = []
    d = 0
    e = 0
    for i in range(1, n+1):
        b.append(a[b[i-1]])
        if b[i] == b[0]:
            d = i
            e = len(b) - d - 1
            break
    if k <= d:
        print(b[k])
    else:
        print(b[(k - d) % e + d])

=======
Suggestion 8

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    A.insert(0, 0)
    # print(A)
    # print(N, K)
    # print(A)
    # print(A)
    # print(A)

    # 2回目以降のループで、Aを更新していく
    # 1回目のループで、A[1]の値が何回目に出てくるかを調べる
    # 2回目のループで、A[2]の値が何回目に出てくるかを調べる
    # 3回目のループで、A[3]の値が何回目に出てくるかを調べる
    # 4回目のループで、A[4]の値が何回目に出てくるかを調べる
    # ...
    # 1回目のループで、A[1]の値が何回目に出てくるかを調べる
    # 2回目のループで、A[2]の値が何回目に出てくるかを調べる
    # 3回目のループで、A[3]の値が何回目に出てくるかを調べる
    # 4回目のループで、A[4]の値が何回目に出てくるかを調べる
    # ...
    # 1回目のループで、A[1]の値が何回目に出てくるかを調べる
    # 2回目のループで、A[2]の値が何回目に出てくるかを調べる
    # 3回目のループで、A[3]の値が何回目に出てくるかを調べる
    # 4回目のループで、A[4

=======
Suggestion 9

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    # A[i] = i+1 -> A[i]-1 = i
    # 1-index -> 0-index
    A = [i-1 for i in A]
    #print(A)
    #print(N, K)
    #print(A)
    #print(A[0])
    #print(A[A[0]])
    #print(A[A[A[0]]])
    #print(A[A[A[A[0]]]])
    #print(A[A[A[A[A[0]]]]])
    #print(A[A[A[A[A[A[0]]]]]])
    #print(A[A[A[A[A[A[A[0]]]]]]])
    #print(A[A[A[A[A[A[A[A[0]]]]]]]])
    #print(A[A[A[A[A[A[A[A[A[0]]]]]]]]])
    #print(A[A[A[A[A[A[A[A[A[A[0]]]]]]]]]])
