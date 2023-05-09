Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    Q = int(input())
    A = []
    for i in range(Q):
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
                print(B[k-1])
        else:
            x = int(query[1])
            k = int(query[2])
            B = [a for a in A if a >= x]
            if len(B) < k:
                print(-1)
            else:
                B.sort()
                print(B[k-1])

=======
Suggestion 2

def main():
    n = int(input())
    a = []
    for i in range(n):
        q = input().split()
        if q[0] == '1':
            a.append(int(q[1]))
        elif q[0] == '2':
            print(sorted(a, reverse=True)[int(q[2])-1])
        else:
            print(sorted(a)[int(q[2])-1])
    return

main()

=======
Suggestion 3

def main():
    n = int(input())
    a = []
    for i in range(n):
        q = input().split()
        if q[0] == '1':
            a.append(int(q[1]))
        elif q[0] == '2':
            x = int(q[1])
            k = int(q[2])
            b = [i for i in a if i <= x]
            if len(b) < k:
                print(-1)
            else:
                print(sorted(b, reverse=True)[k-1])
        elif q[0] == '3':
            x = int(q[1])
            k = int(q[2])
            b = [i for i in a if i >= x]
            if len(b) < k:
                print(-1)
            else:
                print(sorted(b)[k-1])

=======
Suggestion 4

def main():
    q = int(input())
    a = []
    for i in range(q):
        query = input().split()
        if query[0] == "1":
            a.append(int(query[1]))
        elif query[0] == "2":
            x = int(query[1])
            k = int(query[2])
            b = [i for i in a if i <= x]
            if len(b) < k:
                print(-1)
            else:
                print(sorted(b)[-k])
        elif query[0] == "3":
            x = int(query[1])
            k = int(query[2])
            b = [i for i in a if i >= x]
            if len(b) < k:
                print(-1)
            else:
                print(sorted(b)[k-1])

=======
Suggestion 5

def main():
    N = int(input())
    A = []
    for i in range(N):
        query = input().split()
        if query[0] == "1":
            A.append(int(query[1]))
        elif query[0] == "2":
            x = int(query[1])
            k = int(query[2])
            tmp = [a for a in A if a <= x]
            if len(tmp) < k:
                print(-1)
            else:
                print(sorted(tmp)[-k])
        else:
            x = int(query[1])
            k = int(query[2])
            tmp = [a for a in A if a >= x]
            if len(tmp) < k:
                print(-1)
            else:
                print(sorted(tmp)[k-1])

main()

=======
Suggestion 6

def main():
    N = int(input())
    A = []
    for i in range(N):
        query = input().split()
        if query[0] == '1':
            A.append(int(query[1]))
        else:
            x = int(query[1])
            k = int(query[2])
            if query[0] == '2':
                B = [a for a in A if a <= x]
                if len(B) < k:
                    print(-1)
                else:
                    print(sorted(B)[-k])
            else:
                B = [a for a in A if a >= x]
                if len(B) < k:
                    print(-1)
                else:
                    print(sorted(B)[k-1])

=======
Suggestion 7

def main():
    N = int(input())
    for i in range(N):
        query = input().split()
        if query[0] == '1':
            pass
        elif query[0] == '2':
            pass
        elif query[0] == '3':
            pass
        else:
            print('error')
            exit()
    pass

=======
Suggestion 8

def main():
    #input
    n = int(input())
    q = []
    for i in range(n):
        q.append(list(map(int, input().split())))
    
    #process
    a = []
    for i in range(n):
        if q[i][0] == 1:
            a.append(q[i][1])
        elif q[i][0] == 2:
            if len(a) < q[i][2]:
                print(-1)
            else:
                tmp = [x for x in a if x <= q[i][1]]
                tmp.sort(reverse=True)
                print(tmp[q[i][2]-1])
        elif q[i][0] == 3:
            if len(a) < q[i][2]:
                print(-1)
            else:
                tmp = [x for x in a if x >= q[i][1]]
                tmp.sort()
                print(tmp[q[i][2]-1])

=======
Suggestion 9

def main():
    pass

=======
Suggestion 10

def insert(A, x):
    A.append(x)
    return A
