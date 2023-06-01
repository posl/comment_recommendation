Synthesizing 10/10 solutions

=======
Suggestion 1

def insert(x, A):
    A.append(x)
    A.sort()

=======
Suggestion 2

def main():
    pass

=======
Suggestion 3

def main():
    n = int(input())
    a = [0] * n
    for i in range(n):
        a[i] = int(input())
    print(a)
    q = int(input())
    for i in range(q):
        query = input().split()
        if query[0] == "1":
            a.append(int(query[1]))
        else:
            x = int(query[1])
            k = int(query[2])
            if query[0] == "2":
                cnt = 0
                for j in range(len(a)):
                    if a[j] <= x:
                        cnt += 1
                        if cnt == k:
                            print(a[j])
                            break
                else:
                    print(-1)
            else:
                cnt = 0
                for j in range(len(a)):
                    if a[j] >= x:
                        cnt += 1
                        if cnt == k:
                            print(a[j])
                            break
                else:
                    print(-1)

=======
Suggestion 4

def main():
    q = int(input())
    a = []
    for i in range(q):
        query = input().split()
        if query[0] == '1':
            a.append(int(query[1]))
        elif query[0] == '2':
            x = int(query[1])
            k = int(query[2])
            b = [i for i in a if i <= x]
            if len(b) < k:
                print(-1)
            else:
                b.sort(reverse=True)
                print(b[k-1])
        elif query[0] == '3':
            x = int(query[1])
            k = int(query[2])
            b = [i for i in a if i >= x]
            if len(b) < k:
                print(-1)
            else:
                b.sort()
                print(b[k-1])
    return 0

=======
Suggestion 5

def insert(x, A):
    A.append(x)
    return A

=======
Suggestion 6

def main():
    print("Hello World!")
    return

=======
Suggestion 7

def insert(A, x):
    A.append(x)
    return A

=======
Suggestion 8

def main():
    n = int(input())
    a = []
    for i in range(n):
        query = input().strip().split()
        if query[0] == '1':
            a.append(int(query[1]))
        elif query[0] == '2':
            x, k = int(query[1]), int(query[2])
            tmp = [i for i in a if i <= x]
            if len(tmp) < k:
                print(-1)
            else:
                print(sorted(tmp)[-k])
        else:
            x, k = int(query[1]), int(query[2])
            tmp = [i for i in a if i >= x]
            if len(tmp) < k:
                print(-1)
            else:
                print(sorted(tmp)[k-1])

main()

=======
Suggestion 9

def main():
    n = int(input())
    a = []
    for _ in range(n):
        query = input().split()
        if query[0] == '1':
            a.append(int(query[1]))
        elif query[0] == '2':
            x = int(query[1])
            k = int(query[2])
            b = sorted(a)
            if x > b[-1]:
                print(-1)
            else:
                c = b.index(x) + k - 1
                if c >= len(b):
                    print(-1)
                else:
                    print(b[c])
        elif query[0] == '3':
            x = int(query[1])
            k = int(query[2])
            b = sorted(a)
            if x < b[0]:
                print(-1)
            else:
                c = b.index(x) - k + 1
                if c < 0:
                    print(-1)
                else:
                    print(b[c])

=======
Suggestion 10

def main():
    q = int(input())
    a = []
    for i in range(q):
        query = list(map(int, input().split()))
        if query[0] == 1:
            a.append(query[1])
        elif query[0] == 2:
            a.sort()
            if query[1] in a:
                print(a[-query[2]])
            else:
                print(-1)
        elif query[0] == 3:
            a.sort()
            if query[1] in a:
                print(a[query[2]-1])
            else:
                print(-1)
        else:
            print("error")
    return 0
