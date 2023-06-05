Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def swap(a,b):
    temp = a
    a = b
    b = temp
    return a,b

=======
Suggestion 2

def swap(a, b):
    tmp = a
    a = b
    b = tmp
    return a, b

=======
Suggestion 3

def reverse(arr,start,end):
    while start < end:
        arr[start],arr[end] = arr[end],arr[start]
        start += 1
        end -= 1
    return arr

=======
Suggestion 4

def swap(a,b):
    c = a
    a = b
    b = c
    return a,b

=======
Suggestion 5

def swap(p, q, r, s, list):
    list1 = list[0:p]
    list2 = list[p:q]
    list3 = list[q:r]
    list4 = list[r:s]
    list5 = list[s:]
    list2.extend(list4)
    list2.extend(list3)
    list2.extend(list5)
    list1.extend(list2)
    return list1

N, P, Q, R, S = map(int, input().split())
A = list(map(int, input().split()))
B = swap(P-1, Q, R, S+1, A)
print(*B)

=======
Suggestion 6

def main():
    n, p, q, r, s = map(int, input().split())
    a = list(map(int, input().split()))
    b = a[p-1:q] + a[r-1:s]
    b.sort()
    a[p-1:q] = b[:q-p]
    a[r-1:s] = b[q-p:]
    print(*a)

=======
Suggestion 7

def swap(a, b, c, d, e):
    return a[d:e] + a[b:c] + a[a:b] + a[c:d] + a[e:]

=======
Suggestion 8

def swap(a, b):
    return b, a

=======
Suggestion 9

def get_input():
    N, P, Q, R, S = input().split()
    N = int(N)
    P = int(P)
    Q = int(Q)
    R = int(R)
    S = int(S)
    A = input().split()
    A = [int(x) for x in A]
    return N, P, Q, R, S, A
