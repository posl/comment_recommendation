Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n,k = map(int,input().split())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    # print(n,k,a,b)
    print('Yes' if len(set(a) & set(b)) > 0 else 'No')

=======
Suggestion 2

def main():
    n,k=map(int,input().split())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    c=[]
    for i in b:
        c.append(a[i-1])
    c.sort()
    for i in range(k):
        a.remove(c[i])
    if a[-1]>c[-1]:
        print("Yes")
    else:
        print("No")

=======
Suggestion 3

def main():
    N,K = map(int,input().split())
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))

    for i in range(K):
        if B[i] in A:
            print("Yes")
            exit()

    print("No")

=======
Suggestion 4

def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    for i in range(k):
        for j in range(n):
            if a[j] == b[i]:
                a[j] = 0

    if max(a) == 0:
        print("No")
    else:
        print("Yes")

=======
Suggestion 5

def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    for i in range(n):
        for j in range(k):
            if i == b[j] - 1:
                a[i] = 0

    if max(a) == 0:
        print('No')
    else:
        print('Yes')

main()

=======
Suggestion 6

def solve():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    # 1~n
    # 1~k
    # 1~n
    # 1~n
    # 1~k
    # 1~n

    for i in range(k):
        a[b[i]-1] = 0

    print('Yes' if max(a) > 0 else 'No')

=======
Suggestion 7

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    max_A = max(A)
    max_B = max(B)

    if max_A > max_B:
        print('Yes')
    else:
        print('No')

=======
Suggestion 8

def main():
    n,k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    for i in range(k):
        a[b[i]-1] = 0

    if max(a) == 0:
        print("No")
    else:
        print("Yes")

=======
Suggestion 9

def main():
    N,K = map(int,input().split())
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))
    Amax = max(A)
    if Amax in B:
        print("No")
    else:
        print("Yes")

=======
Suggestion 10

def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    #print(n, k)
    #print(a)
    #print(b)

    for i in range(k):
        a[b[i] - 1] = 0

    #print(a)

    if max(a) == 0:
        print("No")
    else:
        print("Yes")
