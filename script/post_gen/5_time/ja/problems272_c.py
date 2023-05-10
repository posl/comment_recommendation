Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    A = list(map(int,input().split()))

    if len(A) == len(set(A)):
        print(-1)
    else:
        print(max(A) * 2)

=======
Suggestion 2

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort(reverse=True)
    max_even = -1
    for i in range(N - 1):
        for j in range(i + 1, N):
            if (A[i] + A[j]) % 2 == 0:
                max_even = max(max_even, A[i] + A[j])
    print(max_even)

=======
Suggestion 3

def main():
    N = int(input())
    A = list(map(int, input().split()))
    #print(N,A)
    #print(A[0])
    #print(A[1])
    #print(A[2])
    #print(A[0]+A[1])
    #print(A[0]+A[2])
    #print(A[1]+A[2])
    #print(A[0]+A[1]+A[2])
    #print(A[0]+A[1]+A[2]+A[3])
    #print(A[0]+A[1]+A[2]+A[3]+A[4])
    #print(A[0]+A[1]+A[2]+A[3]+A[4]+A[5])
    #print(A[0]+A[1]+A[2]+A[3]+A[4]+A[5]+A[6])
    #print(A[0]+A[1]+A[2]+A[3]+A[4]+A[5]+A[6]+A[7])
    #print(A[0]+A[1]+A[2]+A[3]+A[4]+A[5]+A[6]+A[7]+A[8])
    #print(A[0]+A[1]+A[2]+A[3]+A[4]+A[5]+A[6]+A[7]+A[8]+A[9])
    #print(A[0]+A[1]+A[2]+A[3]+A[4]+A[5]+A[6]+A[7]+A[8]+A[9]+A[10])
    #print(A[0]+A[1]+A[2]+A[3]+A[4]+A[5]+A[6]+A[7]+A[8]+A[9]+A[10]+A[11])
    #print(A[0]+A[1]+A[2]+A[3]+A[4]+A[5]+A[6]+A[7]+A[8]+A[9]+A[10]+A[11]+A[12])
    #print(A[0]+A[1]+A[2]+A[3]+A[4]+A[5]+A[6]+A[7]+A

=======
Suggestion 4

def main():
    N = int(input())
    A = list(map(int, input().split()))
    max_a = max(A)
    min_a = min(A)
    if max_a == min_a:
        print(-1)
        return
    if min_a == 0:
        print(max_a)
        return
    print(max_a * 2)

=======
Suggestion 5

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    if a[-1] % 2 == 0:
        print(a[-1])
    else:
        if a[-1] == 1:
            print(-1)
        else:
            print(a[-1] + a[-2])

=======
Suggestion 6

def main():
    n = int(input())
    a = list(map(int, input().split()))
    # 2つの数の和の偶奇は、2つの数の偶奇に依存する
    # 2つの数の偶奇が同じなら、その和は偶数
    # 2つの数の偶奇が異なれば、その和は奇数
    # なので、偶数を作るには、
    # 2つの数の偶奇が異なる組み合わせを探せば良い
    # 2つの数の偶奇が異なる組み合わせの中で最大のものを探せば良い
    # ということは、
    # 偶数の数と奇数の数を数えれば良い
    # 偶数の数が1つ以上あれば、偶数の数の中の最大値を出力すれば良い
    # 偶数の数がなければ、-1を出力すれば良い
    even_count = 0
    odd_count = 0
    for i in range(n):
        if a[i] % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    if even_count > 0:
        print(max(a))
    else:
        print(-1)

=======
Suggestion 7

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    if A[0] == 0 and A[-1] == 0:
        print(0)
        exit()
    if A[0] == 0 or A[-1] == 0:
        print(-1)
        exit()
    if N == 2:
        if (A[0] + A[1]) % 2 == 0:
            print(A[0] + A[1])
            exit()
        else:
            print(-1)
            exit()
    if N == 3:
        if (A[0] + A[1]) % 2 == 0:
            print(A[0] + A[1])
            exit()
        if (A[0] + A[2]) % 2 == 0:
            print(A[0] + A[2])
            exit()
        if (A[1] + A[2]) % 2 == 0:
            print(A[1] + A[2])
            exit()
        if (A[0] + A[1] + A[2]) % 2 == 0:
            print(A[0] + A[1] + A[2])
            exit()
        else:
            print(-1)
            exit()
    if N >= 4:
        if (A[0] + A[-1]) % 2 == 0:
            print(A[0] + A[-1])
            exit()
        if (A[0] + A[-2]) % 2 == 0:
            print(A[0] + A[-2])
            exit()
        if (A[1] + A[-1]) % 2 == 0:
            print(A[1] + A[-1])
            exit()
        if (A[1] + A[-2]) % 2 == 0:
            print(A[1] + A[-2])
            exit()
        if (A[0] + A[-3]) % 2 == 0:
            print(A[0] + A[-3])
            exit()
        if (A[1] + A[-3]) % 2 == 0:
            print(A[1] + A[-3])
            exit()
        if (A[2] + A

=======
Suggestion 8

def main():
    N = int(input())
    A = list(map(int, input().split()))
    odd = []
    even = []
    for i in A:
        if i % 2 == 0:
            even.append(i)
        else:
            odd.append(i)
    if len(odd) == 0:
        print(-1)
    else:
        print(sum(even) + max(odd))

=======
Suggestion 9

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    if a[0] % 2 == 0:
        print(a[0] + a[1])
    elif a[1] % 2 == 0:
        print(a[1] + a[2])
    elif a[0] % 2 != 0 and a[1] % 2 != 0 and a[2] % 2 != 0:
        print(-1)

=======
Suggestion 10

def main():
    N = int(input())
    A = list(map(int,input().split()))
    A.sort()
    if A[0] % 2 == 0 or A[-1] % 2 == 0:
        print(A[-1])
    else:
        print(-1)
