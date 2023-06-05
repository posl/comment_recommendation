Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    pass

=======
Suggestion 2

def main():
    n = int(input())
    A = []
    for i in range(n):
        query = input().split()
        if query[0] == '1':
            A.append(int(query[1]))
        elif query[0] == '2':
            x = int(query[1])
            k = int(query[2])
            tmp = [a for a in A if a <= x]
            tmp.sort(reverse=True)
            if len(tmp) >= k:
                print(tmp[k-1])
            else:
                print(-1)
        else:
            x = int(query[1])
            k = int(query[2])
            tmp = [a for a in A if a >= x]
            tmp.sort()
            if len(tmp) >= k:
                print(tmp[k-1])
            else:
                print(-1)

=======
Suggestion 3

def insert(x):
    global A
    A.append(x)

=======
Suggestion 4

def get_min(a, x, k):
    if k > 5:
        return -1
    count = 0
    for i in range(len(a)):
        if a[i] >= x:
            count += 1
            if count == k:
                return a[i]
    return -1

=======
Suggestion 5

def main():
    q = int(input())
    a = []
    for i in range(q):
        l = list(map(int, input().split()))
        if l[0] == 1:
            a.append(l[1])
        elif l[0] == 2:
            a.sort()
            if len(a) >= l[2]:
                print(a[-l[2]])
            else:
                print(-1)
        elif l[0] == 3:
            a.sort()
            if len(a) >= l[2]:
                print(a[l[2]-1])
            else:
                print(-1)

main()

=======
Suggestion 6

def insert(x):
    global A
    A.append(x)
    return
