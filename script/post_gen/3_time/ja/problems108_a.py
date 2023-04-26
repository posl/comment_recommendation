Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    K = int(input())
    count = 0
    for i in range(1, K+1):
        for j in range(1, K+1):
            if i % 2 == 0 and j % 2 != 0:
                count += 1
    print(count)

=======
Suggestion 2

def main():
    k = int(input())
    even = k // 2
    odd = (k + 1) // 2
    print(even * odd)

=======
Suggestion 3

def main():
    K = int(input())
    if K % 2 == 0:
        print((K//2)**2)
    else:
        print(((K-1)//2)*((K+1)//2))

=======
Suggestion 4

def main():
    K = int(input())
    result = 0
    for i in range(1,K+1):
        if i%2 == 0:
            result += (K//2)
        else:
            result += ((K+1)//2)
    print(result)

=======
Suggestion 5

def main():
    K = int(input())
    even = K // 2
    odd = K - even
    print(even * odd)

=======
Suggestion 6

def main():
    k = int(input())
    print(k*(k-1)//2)

=======
Suggestion 7

def main():
    K = int(input())
    # K = 3
    # K = 6
    # K = 11
    # K = 50
    # K = 100

    # 偶数と奇数の組み合わせを求める
    # 1. 偶数の個数と奇数の個数を求める
    # 2. それぞれの個数の組み合わせを求める
    # 3. 2の値をかける
    # 1.
    even = 0
    odd = 0
    for i in range(1,K+1):
        if i % 2 == 0:
            even += 1
        else:
            odd += 1
    # 2.
    even_combi = 0
    odd_combi = 0
    for i in range(1,even+1):
        even_combi += i
    for i in range(1,odd+1):
        odd_combi += i
    # 3.
    combi = even_combi * odd_combi
    print(combi)

=======
Suggestion 8

def main():
    K = int(input())
    print(K * (K // 2))

=======
Suggestion 9

def main():
    K = int(input())
    print(K//2*(K//2+(K%2)))
