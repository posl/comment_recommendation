Synthesizing 9/10 solutions

=======
Suggestion 1

def main():
    A, B, K = map(int, input().split())
    cnt = 0
    for i in range(1, 101):
        if A % i == 0 and B % i == 0:
            cnt += 1
            if cnt == K:
                print(i)
                exit()

=======
Suggestion 2

def divisors(n):
    i = 1
    table = []
    while i*i <= n:
        if n%i == 0:
            table.append(i)
            if i != n//i:
                table.append(n//i)
        i += 1
    table.sort()
    return table

a, b, k = map(int, input().split())
table = divisors(a)
table.extend(divisors(b))
table = sorted(set(table), reverse=True)
print(table[k-1])

=======
Suggestion 3

def main():
    a, b, k = map(int, input().split())
    divisors = [i for i in range(1, 101) if a % i == 0 and b % i == 0]
    print(divisors[-k])

=======
Suggestion 4

def main():
    a,b,k = map(int, input().split())
    cnt = 0
    for i in range(1,101):
        if a % i == 0 and b % i == 0:
            cnt += 1
            if cnt == k:
                print(i)
                break

=======
Suggestion 5

def main():
    a,b,k = map(int, input().split())
    nums = []
    for i in range(1, 101):
        if a % i == 0 and b % i == 0:
            nums.append(i)
    print(nums[-k])

=======
Suggestion 6

def main():
    a, b, k = map(int, input().split())
    i = 0
    for j in range(100, 0, -1):
        if a % j == 0 and b % j == 0:
            i += 1
            if i == k:
                print(j)
                break

=======
Suggestion 7

def main():
    # 標準入力から A, B, K を取得する
    a, b, k = map(int, input().split())

    # A, B を割り切る正整数の集合を計算する
    divisors = set()
    for i in range(1, 101):
        if a % i == 0 and b % i == 0:
            divisors.add(i)

    # divisors を昇順にソートして、K 番目の要素を出力する
    divisors = sorted(divisors)
    print(divisors[k - 1])

=======
Suggestion 8

def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b,a%b)

=======
Suggestion 9

def main():
    a, b, k = map(int, input().split())
    #print(a, b, k)
    #print(type(a), type(b), type(k))
    #print(a, b, k)
    #print(type(a), type(b), type(k))
    i = 0
    c = 0
    while True:
        i += 1
        if a % i == 0 and b % i == 0:
            c += 1
        if c == k:
            print(i)
            break
