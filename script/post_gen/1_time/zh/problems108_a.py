Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    k = int(input())
    count = 0
    for i in range(1,k+1):
        if i%2==0:
            for j in range(1,k+1):
                if j%2==1:
                    count += 1
    print(count)
main()

=======
Suggestion 2

def problem108_a():
    k = int(input())
    print(int(k/2 * (k - k/2)))

problem108_a()

=======
Suggestion 3

def main():
    n = int(input())
    print((n//2)*(n-n//2))

=======
Suggestion 4

def problems108_a():
    k = int(input())
    if k < 2 or k > 100:
        print("输入的k不符合要求")
        return
    count = 0
    for i in range(1, k + 1):
        for j in range(i+1, k + 1):
            if i % 2 == 0 and j % 2 == 1:
                count += 1
    print(count * 2)

=======
Suggestion 5

def solution():
    k = int(input())
    even = k // 2
    odd = k - even
    print(even * odd)

solution()

=======
Suggestion 6

def main():
    k = int(input())
    print(int(k/2)*int(k/2+1))

=======
Suggestion 7

def main():
    k = int(input())
    print(int(k/2*(k-k/2)))

=======
Suggestion 8

def main():
    k = int(input())
    print(int(k / 2) * int(k / 2 + k % 2))

=======
Suggestion 9

def main():
    k = int(input())
    count = 0
    for i in range(1,k+1):
        if i % 2 == 0:
            count += (k//2)
        else:
            count += (k//2 + 1)
    print(count)

=======
Suggestion 10

def get_even_odd_method(k):
    # 偶数的个数
    even_num = k // 2
    # 奇数的个数
    odd_num = k - even_num
    # 选择偶数的方法
    even_method = even_num * odd_num
    return even_method
