Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n, k, a = map(int, input().split())
    print((k - 1 + a - 1) % n + 1)

=======
Suggestion 2

def main():
    # 读取输入
    N, K, A = map(int, input().split())
    # 处理
    if K <= N:
        print(K)
    else:
        print(N - (K % N))

=======
Suggestion 3

def main():
    n, k, a = map(int, input().split())

    print((k - a) % n)

=======
Suggestion 4

def main():
    n,k,a = map(int, input().split())
    a = a - 1
    print((k - 1 + a) % n + 1)

=======
Suggestion 5

def problems227_a():
    n,k,a = map(int,input().split())
    print((k-1+a-1)%n+1)

problems227_a()

=======
Suggestion 6

def main():
    #n,k,a = map(int, input().split())
    n,k,a = 3, 14, 2
    #n,k,a = 1, 100, 1
    #n,k,a = map(int, input().split())
    #print(n,k,a)
    nlist = [0]*n
    #print(nlist)
    for i in range(k):
        #print(i)
        nlist[a-1] += 1
        #print(nlist)
        a += 1
        if a > n:
            a = 1
    #print(nlist)
    for i in range(n):
        if nlist[i] == max(nlist):
            print(i+1)
            break

main()

=======
Suggestion 7

def main():
    # 读取输入
    inputs = input().split()
    N = int(inputs[0])
    K = int(inputs[1])
    A = int(inputs[2])

    # 循环K次，每次发牌
    for i in range(K):
        if A < N:
            A += 1
        else:
            A = 1

    # 输出结果
    print(A)

=======
Suggestion 8

def main():
    N, K, A = map(int, input().split())
    if K % N == 0:
        print(A)
    else:
        print(A + K % N - 1 if A + K % N <= N else A + K % N - N)

=======
Suggestion 9

def main():
    n,k,a = map(int,input().split())
    k = k%n
    if k+a-1 > n:
        print(k+a-n)
    else:
        print(k+a-1)
