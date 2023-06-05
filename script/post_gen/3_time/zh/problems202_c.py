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
    count = 0
    for i in range(n):
        count += A.count(B[C[i]-1])
    print(count)

=======
Suggestion 2

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = list(map(int, input().split()))

    #B中的元素作为key，B中元素出现的次数作为value存储在字典中
    B_dict = {}
    for i in range(N):
        if B[i] in B_dict:
            B_dict[B[i]] += 1
        else:
            B_dict[B[i]] = 1

    #C中的元素作为key，C中元素出现的次数作为value存储在字典中
    C_dict = {}
    for i in range(N):
        if C[i] in C_dict:
            C_dict[C[i]] += 1
        else:
            C_dict[C[i]] = 1

    #C中的元素作为key，C中元素出现的次数作为value存储在字典中
    A_dict = {}
    for i in range(N):
        if A[i] in A_dict:
            A_dict[A[i]] += 1
        else:
            A_dict[A[i]] = 1

    #A_dict中的key作为B_dict的key，A_dict中的value乘以B_dict中的value作为最终的value
    #A_dict中的key作为C_dict的key，A_dict中的value乘以C_dict中的value作为最终的value
    #如果A_dict中的key在B_dict和C_dict中都存在，那么最终的value是上面两种情况相加
    result = 0
    for key in A_dict:
        if key in B_dict and key in C_dict:
            result += A_dict[key] * B_dict[key] * C_dict[key]

    print(result)

=======
Suggestion 3

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = list(map(int, input().split()))

    # Bの値をキーとして、出現回数をカウント
    cnt_B = [0] * (N + 1)
    for i in range(N):
        cnt_B[B[C[i] - 1]] += 1

    # Aの値をキーとして、Bの値をカウント
    cnt_A = [0] * (N + 1)
    for i in range(N):
        cnt_A[A[i]] += cnt_B[i + 1]

    # 結果を出力
    print(sum(cnt_A))

=======
Suggestion 4

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = list(map(lambda x: int(x)-1, input().split()))

    ca = [0] * n
    for i in range(n):
        ca[c[i]] += 1

    cb = [0] * n
    for i in range(n):
        cb[b[i]-1] += 1

    ans = 0
    for i in range(n):
        ans += ca[i] * cb[i]

    print(ans)

=======
Suggestion 5

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = list(map(int, input().split()))

    #Cの要素の値-1をインデックスとして、Bの要素の値を格納する配列
    D = [0] * N
    for i in range(N):
        D[C[i] - 1] += 1

    #Aの要素の値-1をインデックスとして、Dの要素の値を格納する配列
    E = [0] * N
    for i in range(N):
        E[A[i] - 1] += D[i]

    ans = 0
    for i in range(N):
        ans += E[B[i] - 1]

    print(ans)

=======
Suggestion 6

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = list(map(int, input().split()))

    B_C = [0] * N
    for i in range(N):
        B_C[C[i]-1] += 1

    A_B_C = [0] * N
    for i in range(N):
        A_B_C[B[i]-1] += B_C[i]

    print(sum(A_B_C))

=======
Suggestion 7

def main():
    n=int(input())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    c=list(map(int,input().split()))
    count=[0]*n
    for i in range(n):
        count[b[c[i]-1]-1]+=1
    ans=0
    for i in range(n):
        ans+=count[a[i]-1]
    print(ans)

=======
Suggestion 8

def solution1(N, A, B, C):
    count = 0
    for i in range(N):
        for j in range(N):
            if A[i] == B[C[j]-1]:
                count += 1
    return count

=======
Suggestion 9

def main():
    n = int(input())
    a = [int(i) for i in input().split()]
    b = [int(i) for i in input().split()]
    c = [int(i) for i in input().split()]
    a_count = [0] * (n + 1)
    for i in a:
        a_count[i] += 1
    c_count = [0] * (n + 1)
    for i in c:
        c_count[i] += 1
    ans = 0
    for i in range(1, n + 1):
        ans += a_count[i] * c_count[i]
    print(ans)

=======
Suggestion 10

def get_num(N, A, B, C):
    count = 0
    for i in range(N):
        for j in range(N):
            if A[i] == B[C[j]-1]:
                count += 1
    return count
