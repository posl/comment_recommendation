Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    k = int(input())
    count = 0
    for i in range(1, k + 1):
        if i % 2 == 0:
            for j in range(1, k + 1):
                if j % 2 == 1:
                    count += 1
    print(count)

=======
Suggestion 2

def main():
    k = int(input())
    even = [i for i in range(1, k + 1) if i % 2 == 0]
    odd = [i for i in range(1, k + 1) if i % 2 == 1]
    print(len(even) * len(odd))

=======
Suggestion 3

def main():
    K = int(input())
    ans = 0
    for i in range(1, K + 1):
        if i % 2 == 0:
            ans += K // 2
        else:
            ans += (K + 1) // 2
    print(ans)

=======
Suggestion 4

def main():
    k = int(input())
    ans = 0
    for i in range(1,k+1):
        if i%2 == 0:
            ans += (k-i)//2 + 1
    print(ans)

=======
Suggestion 5

def main():
    # 入力
    K = int(input())

    # 処理
    ans = 0
    for i in range(1, K + 1):
        if i % 2 == 0:
            for j in range(1, K + 1):
                if j % 2 == 1:
                    ans += 1

    # 出力
    print(ans)

main()

=======
Suggestion 6

def main():
    k = int(input())
    if k % 2 == 0:
        print(int(k/2)**2)
    else:
        print(int(k/2)*int((k+1)/2))

=======
Suggestion 7

def main():
    K = int(input())
    print(K*(K-1)//2)

=======
Suggestion 8

def main():

    #入力
    K = int(input())

    #偶数の数
    even = K // 2
    #奇数の数
    odd = K // 2 + 1 if K % 2 == 1 else K // 2

    #出力
    print(even * odd)

=======
Suggestion 9

def main():
    k = int(input())
    print(int(k/2)*(k-int(k/2)))
