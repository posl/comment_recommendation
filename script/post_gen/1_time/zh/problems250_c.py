Synthesizing 10/10 solutions

=======
Suggestion 1

def swap(l, i, j):
    temp = l[i]
    l[i] = l[j]
    l[j] = temp

=======
Suggestion 2

def main():
    n, q = map(int, input().split())
    x = [int(input()) for _ in range(q)]
    a = [i for i in range(1, n+1)]
    for i in range(q):
        a[i], a[i+1] = a[i+1], a[i]
        if a[i] == x[i]:
            a[i], a[i+1] = a[i+1], a[i]
    print(*a)

=======
Suggestion 3

def main():
    n, q = map(int, input().split())
    x = [int(input()) for _ in range(q)]
    num = [i for i in range(1, n+1)]
    for i in range(q):
        #print(num)
        #print(x[i])
        #print(num.index(x[i]))
        num[num.index(x[i])], num[num.index(x[i])+1] = num[num.index(x[i])+1], num[num.index(x[i])]
    print(*num)

=======
Suggestion 4

def swap(arr, i):
    tmp = arr[i]
    arr[i] = arr[i+1]
    arr[i+1] = tmp

=======
Suggestion 5

def swap(a, i, j):
    a[i], a[j] = a[j], a[i]

=======
Suggestion 6

def main():
    n,q = map(int,input().split())
    x = [int(input()) for _ in range(q)]
    a = [i+1 for i in range(n)]
    for i in range(q):
        a[x[i]-1],a[x[i]] = a[x[i]],a[x[i]-1]
    print(' '.join(map(str,a)))

=======
Suggestion 7

def swap(a, b):
    return b, a

=======
Suggestion 8

def main():
    n, q = map(int, input().split())
    x = []
    for i in range(q):
        x.append(int(input()))
    a = list(range(1, n+1))
    for i in range(q-1, -1, -1):
        a[i], a[i+1] = a[i+1], a[i]
        if a[i] == x[i]:
            a[i], a[i+1] = a[i+1], a[i]
    print(*a)

=======
Suggestion 9

def main():
    n,q = map(int,input().split())
    x = []
    for i in range(q):
        x.append(int(input()))
    #print(x)
    #print(n,q)
    l = [i+1 for i in range(n)]
    #print(l)
    for i in range(q):
        #print('i',i)
        #print('x[i]-1',x[i]-1)
        if x[i] != 1:
            l[x[i]-2],l[x[i]-1] = l[x[i]-1],l[x[i]-2]
            #print(l)
        else:
            l[0],l[1] = l[1],l[0]
            #print(l)
    for i in range(n):
        print(l[i],end=' ')
    print('')

=======
Suggestion 10

def swap(x, y):
    tmp = x
    x = y
    y = tmp
    return x, y
