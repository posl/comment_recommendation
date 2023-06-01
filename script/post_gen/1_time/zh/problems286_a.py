Synthesizing 10/10 solutions

=======
Suggestion 1

def swap_list(l, p, q, r, s):
    new_list = []
    new_list.extend(l[0:p])
    new_list.extend(l[r:s+1])
    new_list.extend(l[q:r])
    new_list.extend(l[p:q])
    new_list.extend(l[s+1:])
    return new_list

=======
Suggestion 2

def swap(A, P, Q, R, S):
    B = []
    for i in range(0, len(A)):
        if i == P-1:
            for j in range(R-1, S):
                B.append(A[j])
        elif i == R-1:
            for j in range(P-1, Q):
                B.append(A[j])
        else:
            B.append(A[i])
    return B

=======
Suggestion 3

def swap_list(list, p, q, r, s):
    list[p-1:q],list[r-1:s] = list[r-1:s],list[p-1:q]
    return list

N, P, Q, R, S = map(int, input().split())
A = list(map(int, input().split()))
B = swap_list(A, P, Q, R, S)
print(' '.join(str(i) for i in B))

=======
Suggestion 4

def swap_list(list_, start, end):
    list_ = list(list_)
    for i in range(start, (end+start)//2+1):
        list_[i], list_[end+start-i] = list_[end+start-i], list_[i]
    return list_

=======
Suggestion 5

def swap(L, i, j):
    temp = L[i:j+1]
    temp.reverse()
    L[i:j+1] = temp

=======
Suggestion 6

def swap(a, p, q, r, s):
    # 交换p到q和r到s的序列
    b = a[:]
    for i in range(q-p+1):
        b[p+i-1] = a[r+i-1]
    for i in range(s-r+1):
        b[r+i-1] = a[q+i-1]
    return b

=======
Suggestion 7

def swap_list(list, p, q, r, s):
    # 交换A的P项到Q项和R项到S项得到序列B
    list[p:q], list[r:s] = list[r:s], list[p:q]
    return list

=======
Suggestion 8

def main():
    #get N,P,Q,R,S
    line = input()
    line = line.split()
    N = int(line[0])
    P = int(line[1])
    Q = int(line[2])
    R = int(line[3])
    S = int(line[4])
    #get A
    line = input()
    line = line.split()
    A = []
    for i in range(N):
        A.append(int(line[i]))
    #get B
    B = []
    for i in range(N):
        if i < P-1 or i > Q-1:
            B.append(A[i])
        else:
            B.append(A[i+R-Q])
    #print B
    for i in range(N):
        print(B[i], end=" ")

=======
Suggestion 9

def main():
    # 读取输入
    N, P, Q, R, S = map(int, input().split())
    A = list(map(int, input().split()))

    # 交换
    B = A[:P-1] + A[R-1:S] + A[Q-1:R-1] + A[S:]

    # 打印输出
    print(' '.join(map(str, B)))

=======
Suggestion 10

def swap(p,q,r,s):
    for i in range(p-1,q):
        temp = a[i]
        a[i] = a[s-1]
        a[s-1] = temp
        s = s-1
    for i in range(r-1,s):
        temp = a[i]
        a[i] = a[q-1]
        a[q-1] = temp
        q = q+1
    return a

n,p,q,r,s = map(int,input().split())
a = list(map(int,input().split()))
b = swap(p,q,r,s)
print(*b)
