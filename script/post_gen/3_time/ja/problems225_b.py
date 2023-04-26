Synthesizing 9/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    a = [0] * (N-1)
    b = [0] * (N-1)
    for i in range(N-1):
        a[i], b[i] = map(int, input().split())
    ans = "Yes"
    for i in range(N-1):
        if a.count(a[i]) + a.count(b[i]) != 1:
            ans = "No"
            break
        if b.count(a[i]) + b.count(b[i]) != 1:
            ans = "No"
            break
    print(ans)

=======
Suggestion 2

def main():
    N = int(input())
    a = []
    b = []
    for i in range(N-1):
        a_i, b_i = map(int, input().split())
        a.append(a_i)
        b.append(b_i)
    #print(a)
    #print(b)
    if a.count(a[0]) == N-1:
        print('Yes')
    elif b.count(b[0]) == N-1:
        print('Yes')
    else:
        print('No')

=======
Suggestion 3

def main():
    n = int(input())
    a = [0] * (n-1)
    b = [0] * (n-1)
    for i in range(n-1):
        a[i], b[i] = map(int, input().split())
    ans = "Yes"
    for i in range(n-1):
        if a[i] == 1 or b[i] == 1:
            continue
        else:
            ans = "No"
            break
    print(ans)

=======
Suggestion 4

def main():
    N = int(input())
    a = [0] * (N-1)
    b = [0] * (N-1)
    for i in range(N-1):
        a[i],b[i] = map(int,input().split())
    #print(a)
    #print(b)
    if a.count(a[0]) == N-1:
        print("Yes")
    elif b.count(b[0]) == N-1:
        print("Yes")
    else:
        print("No")

=======
Suggestion 5

def main():
    N = int(input())
    deg = [0] * (N + 1)
    for _ in range(N - 1):
        a, b = map(int, input().split())
        deg[a] += 1
        deg[b] += 1
    if deg.count(1) == 1 and deg.count(N - 1) == 1:
        print("Yes")
    else:
        print("No")

=======
Suggestion 6

def main():
    N = int(input())
    a = []
    b = []
    for i in range(N-1):
        a_i,b_i = map(int,input().split())
        a.append(a_i)
        b.append(b_i)
    #print(a)
    #print(b)
    #print(N)
    d = dict()
    for i in range(N-1):
        if a[i] in d:
            d[a[i]] += 1
        else:
            d[a[i]] = 1
        if b[i] in d:
            d[b[i]] += 1
        else:
            d[b[i]] = 1
    #print(d)
    count = 0
    for k,v in d.items():
        if v == N-1:
            count += 1
    if count == 1:
        print("Yes")
    else:
        print("No")

=======
Suggestion 7

def main():
    N = int(input())
    A = [0] * N
    for i in range(N-1):
        a, b = map(int, input().split())
        A[a-1] += 1
        A[b-1] += 1
    if A.count(1) == 1 and A.count(N-1) == 1:
        print('Yes')
    else:
        print('No')

=======
Suggestion 8

def main():
    N = int(input())
    a = []
    b = []
    for i in range(N-1):
        line = list(map(int, input().split()))
        a.append(line[0])
        b.append(line[1])

    if a.count(a[0]) + b.count(a[0]) == N-1:
        print("Yes")
    else:
        print("No")

=======
Suggestion 9

def main():
    N = int(input())
    if N == 3:
        print("Yes")
        return
    tree = [0]*N
    for i in range(N-1):
        a,b = map(int, input().split())
        tree[a-1] += 1
        tree[b-1] += 1
    if tree.count(1) == 1:
        print("Yes")
    else:
        print("No")
