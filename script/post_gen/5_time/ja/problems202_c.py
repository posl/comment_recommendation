Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = list(map(int, input().split()))

    A.sort()
    B.sort()
    C.sort()

    ans = 0
    a = 0
    c = 0
    for b in range(n):
        while a < n and A[a] < B[b]:
            a += 1
        while c < n and C[c] <= B[b]:
            c += 1
        ans += a * (n - c)

    print(ans)

=======
Suggestion 2

def main():
    n = int(input())
    a_list = list(map(int, input().split()))
    b_list = list(map(int, input().split()))
    c_list = list(map(int, input().split()))

    c_dict = {}
    for c in c_list:
        if c in c_dict:
            c_dict[c] += 1
        else:
            c_dict[c] = 1

    b_dict = {}
    for b in b_list:
        if b in b_dict:
            b_dict[b] += 1
        else:
            b_dict[b] = 1

    a_dict = {}
    for a in a_list:
        if a in a_dict:
            a_dict[a] += 1
        else:
            a_dict[a] = 1

    ans = 0
    for i in range(1, n + 1):
        if i in a_dict and i in b_dict:
            ans += a_dict[i] * b_dict[i] * c_dict[i]

    print(ans)

=======
Suggestion 3

def main():
    n = int(input())
    a = [int(x) for x in input().split()]
    b = [int(x) for x in input().split()]
    c = [int(x) for x in input().split()]
    d = {}
    for i in range(n):
        if b[c[i]-1] in d:
            d[b[c[i]-1]] += 1
        else:
            d[b[c[i]-1]] = 1
    ans = 0
    for i in range(n):
        if a[i] in d:
            ans += d[a[i]]
    print(ans)
main()

=======
Suggestion 4

def solve(n, a, b, c):
    a = [i-1 for i in a]
    b = [i-1 for i in b]
    c = [i-1 for i in c]

    b_count = {}
    for i in range(n):
        if b[i] in b_count:
            b_count[b[i]] += 1
        else:
            b_count[b[i]] = 1

    c_count = {}
    for i in range(n):
        if c[i] in c_count:
            c_count[c[i]] += 1
        else:
            c_count[c[i]] = 1

    ans = 0
    for i in range(n):
        if a[i] in b_count:
            ans += b_count[a[i]] * c_count[i]

    return ans

=======
Suggestion 5

def main():
    N = int(input())
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))
    C = list(map(int,input().split()))
    #print(N,A,B,C)
    #print(A[0])
    #print(B[C[0]-1])
    #print(B[0])
    #print(C[0])
    #print(A[0]==B[C[0]-1])
    #print(A[0]==B[0])
    #print(A[0]==B[C[0]-1])
    #print(A[0]==B[0])
    #print(A[1]==B[C[1]-1])
    #print(A[1]==B[1])
    #print(A[1]==B[C[1]-1])
    #print(A[1]==B[1])
    #print(A[2]==B[C[2]-1])
    #print(A[2]==B[2])
    #print(A[2]==B[C[2]-1])
    #print(A[2]==B[2])
    #print(A[0]==B[C[0]-1])
    #print(A[0]==B[0])
    #print(A[0]==B[C[0]-1])
    #print(A[0]==B[0])
    #print(A[1]==B[C[1]-1])
    #print(A[1]==B[1])
    #print(A[1]==B[C[1]-1])
    #print(A[1]==B[1])
    #print(A[2]==B[C[2]-1])
    #print(A[2]==B[2])
    #print(A[2]==B[C[2]-1])
    #print(A[2]==B[2])
    #print(A[0]==B[C[0]-1])
    #print(A[0]==B[0])
    #print(A[0]==B[C[0]-1])
    #print(A[0]==B[0])
    #print(A[1]==B[C[1]-1])
    #print(A[1]==B[1])
    #print(A[1]==B[C[1]-1])
    #print(A[1]==B[1])
    #print(A[2]==B[C[2]-1])
    #print(A[2]==B[

=======
Suggestion 6

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = [int(i)-1 for i in input().split()]

    count = [0] * n
    for i in range(n):
        count[c[b[i]-1]] += 1

    ans = 0
    for i in range(n):
        ans += count[a[i]-1]

    print(ans)

=======
Suggestion 7

def main():
    n = int(input())
    a = [int(x) for x in input().split()]
    b = [int(x) for x in input().split()]
    c = [int(x) for x in input().split()]
    a.sort()
    b.sort()
    c.sort()
    count = 0
    for i in range(n):
        #print(i)
        #print(a[i])
        #print(b[c[i]-1])
        if a[i] == b[c[i]-1]:
            #print("OK")
            count += 1
    print(count)

=======
Suggestion 8

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = list(map(int, input().split()))

    B_dict = {}
    for i in range(len(B)):
        B_dict[B[i]-1] = i

    C_dict = {}
    for i in range(len(C)):
        if C[i]-1 in B_dict:
            if B_dict[C[i]-1] in C_dict:
                C_dict[B_dict[C[i]-1]] += 1
            else:
                C_dict[B_dict[C[i]-1]] = 1

    count = 0
    for i in range(len(A)):
        if A[i]-1 in C_dict:
            count += C_dict[A[i]-1]

    print(count)

=======
Suggestion 9

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = [int(i) - 1 for i in input().split()]
    #print(n)
    #print(a)
    #print(b)
    #print(c)

    #cについて、bの要素をkeyにして、valueをindexにした辞書を作る
    #c = [0,1,1]の時、{1:0,2:1,2:2}となる
    #c = [1,2,2]の時、{1:0,2:1,2:2}となる
    #c = [2,3,2]の時、{2:0,3:1,2:2}となる
    #この辞書を使って、aとbの組み合わせを数える
    #a = [1,2,2],b = [3,1,2]の時、{1:0,2:1,2:2}となる
    #a = [2,3,2],b = [1,2,2]の時、{1:0,2:1,2:2}となる
    #a = [2,3,2],b = [2,3,2]の時、{2:0,3:1,2:2}となる
    #a = [1,1,1,1],b = [1,1,1,1]の時、{1:0,1:1,1:2,1:3}となる
    #a = [1,1,1,1],b = [1,1,1,1]の時、{1:0,1:1,1:2,1:3}となる
    #a = [1,2,3,4],b = [1,1,1,1]の時、{1:0,1:1,1:2,1:3}となる
    #a = [2,3,3],b = [1,3,3]

=======
Suggestion 10

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = [int(i)-1 for i in input().split()]

    cnt = [0] * n
    for i in c:
        cnt[b[i]] += 1

    ans = 0
    for i in range(n):
        ans += cnt[a[i]]

    print(ans)
