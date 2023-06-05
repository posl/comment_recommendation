Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N = int(input())
    print((N//2)*((N+1)//2))

=======
Suggestion 2

def solve(K):
    # 1. 2~K之间的偶数个数
    # 2. 1~K之间的奇数个数
    # 3. 1.2的组合
    # 4. 3的和
    # 5. 4的平方
    return (K//2) * ((K+1)//2)

print(solve(3))
print(solve(6))
print(solve(11))
print(solve(50))

=======
Suggestion 3

def main():
    k = int(input())
    print(int(k/2*(k-k/2)))

=======
Suggestion 4

def main():
    K = int(input())
    print(int(K/2*(K-K/2)))

=======
Suggestion 5

def main():
    k = int(input())
    print(int(k/2)*int((k+1)/2))

main()

=======
Suggestion 6

def main():
    k = int(input())
    print((k//2)*((k+1)//2))

=======
Suggestion 7

def main():
    K = int(input())
    print(int(K/2)*int(K/2+K%2))

=======
Suggestion 8

def main():
    k = int(input())
    if k % 2 == 0:
        print(int((k/2)**2))
    else:
        print(int((k//2)*(k//2+1)))

=======
Suggestion 9

def main():
    k = int(input())
    sum = 0
    for i in range(1,k+1):
        if i % 2 == 0:
            for j in range(1,k+1):
                if j % 2 == 1:
                    sum += 1
        else:
            for j in range(1,k+1):
                if j % 2 == 0:
                    sum += 1
    print(sum)
