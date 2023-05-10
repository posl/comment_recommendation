Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

p = int(input())
ans = 0
for i in range(10, 0, -1):
    if p >= factorial(i):
        ans += p // factorial(i)
        p %= factorial(i)
print(ans)

=======
Suggestion 2

def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)

p = int(input())

coins = []
for i in range(1,11):
    coins.append(factorial(i))

coins.reverse()

count = 0
for coin in coins:
    while p >= coin:
        p -= coin
        count += 1

print(count)

=======
Suggestion 3

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

=======
Suggestion 4

def main():
    n = int(input())
    #n!のリストを作成
    n_list = [1]
    for i in range(1,11):
        n_list.append(n_list[i-1]*i)
    #print(n_list)

    #n!のリストから引いていく
    ans = 0
    for i in range(10,0,-1):
        #print(n_list[i])
        while n >= n_list[i]:
            n -= n_list[i]
            ans += 1
    print(ans)

=======
Suggestion 5

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)

p = int(input())
ans = 0
for i in range(10, 0, -1):
    if p >= factorial(i):
        ans += p // factorial(i)
        p %= factorial(i)
print(ans)

=======
Suggestion 6

def main():
    P = int(input())
    ans = 0
    for i in range(10, 0, -1):
        ans += P // i
        P %= i
    print(ans)

=======
Suggestion 7

def calc(n):
    if n == 0:
        return 0
    else:
        for i in range(10, 0, -1):
            if n >= i * factorial(i):
                return i + calc(n - i * factorial(i))
        return 0

=======
Suggestion 8

def factorial(n):
    return n * factorial(n - 1) if n > 1 else 1

p = int(input())
coins = [factorial(i) for i in range(1, 11)][::-1]
i = 0
count = 0
while p > 0:
    count += p // coins[i]
    p %= coins[i]
    i += 1
print(count)

=======
Suggestion 9

def main():
    p = int(input())
    k = 0
    for i in range(10,0,-1):
        k += p//math.factorial(i)
        p %= math.factorial(i)
    print(k)
