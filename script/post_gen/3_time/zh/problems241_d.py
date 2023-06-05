Synthesizing 10/10 solutions

=======
Suggestion 1

def insert(A,x):
    A.append(x)
    return A

=======
Suggestion 2

def get_min_k(list, k):
    list.sort(reverse=True)
    return list[k-1]

=======
Suggestion 3

def main():
    n = int(input())
    a = []
    for _ in range(n):
        q = input().split()
        if q[0] == '1':
            a.append(int(q[1]))
        elif q[0] == '2':
            a.sort(reverse=True)
            print(a[int(q[2])-1])
        else:
            a.sort()
            print(a[int(q[2])-1])
    return

=======
Suggestion 4

def main():
    q = int(input())
    a = []
    for i in range(q):
        query = input().split()
        if query[0] == '1':
            x = int(query[1])
            a.append(x)
        elif query[0] == '2':
            x = int(query[1])
            k = int(query[2])
            b = [i for i in a if i <= x]
            if len(b) < k:
                print(-1)
            else:
                b.sort(reverse=True)
                print(b[k-1])
        else:
            x = int(query[1])
            k = int(query[2])
            b = [i for i in a if i >= x]
            if len(b) < k:
                print(-1)
            else:
                b.sort()
                print(b[k-1])

=======
Suggestion 5

def main():
    q = int(input())
    A = []
    for i in range(q):
        query = input().split()
        if query[0] == '1':
            A.append(int(query[1]))
        elif query[0] == '2':
            x = int(query[1])
            k = int(query[2])
            num = 0
            for a in A:
                if a <= x:
                    num += 1
            if num < k:
                print(-1)
            else:
                B = A.copy()
                B.sort(reverse=True)
                print(B[k-1])
        else:
            x = int(query[1])
            k = int(query[2])
            num = 0
            for a in A:
                if a >= x:
                    num += 1
            if num < k:
                print(-1)
            else:
                B = A.copy()
                B.sort()
                print(B[k-1])

=======
Suggestion 6

def main():
    n = int(input())
    a = []
    for i in range(n):
        x = input().split()
        if x[0] == '1':
            a.append(int(x[1]))
        elif x[0] == '2':
            a.sort()
            if len(a) >= int(x[2]):
                print(a[-int(x[2])])
            else:
                print(-1)
        elif x[0] == '3':
            a.sort()
            if len(a) >= int(x[2]):
                print(a[int(x[2])-1])
            else:
                print(-1)

=======
Suggestion 7

def main():
    n = int(input())
    A = []
    for _ in range(n):
        query = input().split()
        if query[0] == '1':
            A.append(int(query[1]))
        elif query[0] == '2':
            x = int(query[1])
            k = int(query[2])
            B = [a for a in A if a <= x]
            if len(B) < k:
                print(-1)
            else:
                B.sort(reverse=True)
                print(B[k - 1])
        elif query[0] == '3':
            x = int(query[1])
            k = int(query[2])
            B = [a for a in A if a >= x]
            if len(B) < k:
                print(-1)
            else:
                B.sort()
                print(B[k - 1])

=======
Suggestion 8

def main():
    q = int(input())
    a = []
    for i in range(q):
        query = list(map(int,input().split()))
        if query[0] == 1:
            a.append(query[1])
        elif query[0] == 2:
            a.sort()
            if len(a) < query[2]:
                print(-1)
            else:
                print(a[-query[2]])
        else:
            a.sort(reverse = True)
            if len(a) < query[2]:
                print(-1)
            else:
                print(a[-query[2]])

=======
Suggestion 9

def main():
    pass

=======
Suggestion 10

def main():
    import sys
    from bisect import bisect_left
    from bisect import bisect_right

    def get_ints(): return map(int, sys.stdin.readline().strip().split())
    def get_list(): return list(map(int, sys.stdin.readline().strip().split()))
    def get_int(): return int(sys.stdin.readline().strip())
    def get_str(): return sys.stdin.readline().strip()

    class BIT:
        def __init__(self, n):
            self.n = n
            self.data = [0] * (n + 1)

        def add(self, i, w):
            x = i
            while x <= self.n:
                self.data[x] += w
                x += x & -x

        def sum(self, i):
            ret, x = 0, i
            while x > 0:
                ret += self.data[x]
                x -= x & -x
            return ret

    class BIT2D:
        def __init__(self, n):
            self.n = n
            self.data = [BIT(n) for _ in range(n + 1)]

        def add(self, i, j, w):
            x = i
            while x <= self.n:
                self.data[x].add(j, w)
                x += x & -x

        def sum(self, i, j):
            ret, x = 0, i
            while x > 0:
                ret += self.data[x].sum(j)
                x -= x & -x
            return ret

    n = get_int()
    a = []
    for _ in range(n):
        t, *args = get_ints()
        if t == 1:
            a.append(args[0])
    a.sort()
    bit = BIT(n)
    for i, v in enumerate(a):
        bit.add(i + 1, v)
    bit2d = BIT2D(n)
    for i, v in enumerate(a):
        bit2d.add(i + 1, bisect_left(a, v), 1)

    q = get_int()
    for _ in range(q):
        t, *args = get_ints()
        if t == 1:
            v = args[0]
            i = bisect_left(a, v)
            a.insert(i, v)
            bit.add(i + 1, v)
            bit
