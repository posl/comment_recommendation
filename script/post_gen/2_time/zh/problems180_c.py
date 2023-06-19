Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def solve(n):
    from math import sqrt
    ans = set()
    for i in range(1, int(sqrt(n)) + 1):
        if n % i == 0:
            ans.add(i)
            ans.add(n // i)
    return sorted(ans)

=======
Suggestion 2

def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if temp%i==0:
            cnt=0
            while temp%i==0:
                cnt+=1
                temp //= i
            arr.append(i)
    if temp!=1:
        arr.append(temp)
    if arr==[]:
        arr.append(n)
    return arr

n = int(input())
arr = factorization(n)
ans = set()
ans.add(1)
for i in range(1, len(arr)+1):
    for j in range(len(arr)):
        ans.add(arr[j]**i)
ans = sorted(list(ans))
for i in range(len(ans)):
    print(ans[i])

=======
Suggestion 3

def main():
    n = int(input())
    i = 1
    while i * i <= n:
        if n % i == 0:
            print(i)
            if i != n // i:
                print(n // i)
        i += 1

=======
Suggestion 4

def find_divisor(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n%i == 0:
            divisors.append(i)
            if i != n//i:
                divisors.append(n//i)
    return divisors

n = int(input())
divisors = find_divisor(n)
divisors.sort()
for i in divisors:
    print(i)

=======
Suggestion 5

def main():
    N = int(input())
    i = 1
    while i * i <= N:
        if N % i == 0:
            print(i)
            if i != N // i:
                print(N // i)
        i += 1

main()

=======
Suggestion 6

def main():
    n = int(input())
    #n = 1000000007
    #n = 720
    num = 1
    #num_list = []
    while num <= n:
        if n % num == 0:
            #num_list.append(num)
            print(num)
        num += 1
    #print(num_list)

=======
Suggestion 7

def get_divisors(n):
    divisors = set()
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            divisors.add(i)
            divisors.add(n // i)
    return divisors

N = int(input())
divisors = get_divisors(N)
for d in sorted(divisors):
    print(d)

=======
Suggestion 8

def main():
    N = int(input())
    i = 1
    while i * i <= N:
        if N % i == 0:
            print(i)
            if i * i != N:
                print(N // i)
        i += 1

=======
Suggestion 9

def get_divisor(n):
    divisor = []
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            divisor.append(i)
            divisor.append(n // i)
    return sorted(divisor)
