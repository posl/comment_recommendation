Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def divisor(n):
    res = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            res.append(i)
            if i != n // i:
                res.append(n//i)
    return res

N = int(input())
count = 0
for i in range(1, N+1, 2):
    if len(divisor(i)) == 8:
        count += 1
print(count)

=======
Suggestion 2

def main():
    N = int(input())
    count = 0
    for i in range(1, N + 1, 2):
        if count_divisor(i) == 8:
            count += 1
    print(count)

=======
Suggestion 3

def main():
    N = int(input())
    count = 0
    for i in range(1,N+1,2):
        if len([j for j in range(1,i+1) if i%j==0]) == 8:
            count += 1
    print(count)

=======
Suggestion 4

def main():
    N = int(input())
    ans = 0

    for i in range(1,N+1,2):
        cnt = 0
        for j in range(1,i+1):
            if i % j == 0:
                cnt += 1
        if cnt == 8:
            ans += 1

    print(ans)

=======
Suggestion 5

def main():
    N = int(input())
    count = 0
    for i in range(1, N+1, 2):
        if len(divisor(i)) == 8:
            count += 1
    print(count)

=======
Suggestion 6

def main():
    N = int(input())
    ans = 0
    for i in range(1, N + 1, 2):
        if i % 2 == 0:
            continue
        cnt = 0
        for j in range(1, i + 1):
            if i % j == 0:
                cnt += 1
        if cnt == 8:
            ans += 1
    print(ans)

=======
Suggestion 7

def main():
    N = int(input())
    ans = 0
    for i in range(1,N+1,2):
        if i % 2 == 1:
            if count(i) == 8:
                ans += 1
    print(ans)

=======
Suggestion 8

def main():
    N = int(input())
    #N = 105
    #N = 7
    #N = 200
    #N = 100
    #N = 50
    #N = 25
    #N = 10
    #N = 5
    #N = 2
    #N = 1
    #N = 0

    # 奇数のリストを作成
    list = [i for i in range(1, N+1) if i % 2 != 0]

    # 約数を求める
    # 約数の個数が8個のリストを作成
    list2 = [i for i in list if len([j for j in range(1, i+1) if i % j == 0]) == 8]

    print(len(list2))

=======
Suggestion 9

def main():
    N = int(input())
    print(N // 2)
