Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

=======
Suggestion 2

def sum():
    N, a, b = map(int, input().split())
    sum = 0
    for i in range(1, N+1):
        if i%a!=0 and i%b!=0:
            sum+=i
    return sum

print(sum())

=======
Suggestion 3

def f(n,a,b):
    c=n//a
    d=n//b
    e=n//(a*b)
    return n*(n+1)//2 - (a+c)*c//2 - (b+d)*d//2 + (a*b+e)*e//2

n,a,b=map(int,input().split())
print(f(n,a,b))

=======
Suggestion 4

def main():
    N, a, b = map(int, input().split())
    sum = 0
    for i in range(1,N+1):
        if i%a != 0 and i%b != 0:
            sum += i
    print(sum)

=======
Suggestion 5

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

=======
Suggestion 6

def main():
    #读取数据
    input_str = input()
    input_list = input_str.split()
    N = int(input_list[0])
    a = int(input_list[1])
    b = int(input_list[2])
    #计算答案
    #先计算A的倍数之和
    sum_a = 0
    if a <= N:
        sum_a = a*(N//a)*(N//a+1)//2
    #再计算B的倍数之和
    sum_b = 0
    if b <= N:
        sum_b = b*(N//b)*(N//b+1)//2
    #再计算A和B的最小公倍数的倍数之和
    sum_ab = 0
    if a*b <= N:
        sum_ab = a*b*(N//(a*b))*(N//(a*b)+1)//2
    #最后减去A和B的最小公倍数的倍数之和
    sum_ans = sum_a + sum_b - sum_ab
    #输出答案
    print(sum_ans)

=======
Suggestion 7

def gcd(x,y):
    if x < y:
        x,y = y,x
    while y > 0:
        r = x % y
        x = y
        y = r
    return x
