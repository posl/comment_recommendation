Synthesizing 10/10 solutions

=======
Suggestion 1

def lunlun(n):
    if n%10 == 0:
        return n+1
    elif n%10 == 9:
        return n-1
    else:
        return [n-1,n+1]

=======
Suggestion 2

def main():
    K = int(input())
    lunlun = [1,2,3,4,5,6,7,8,9]
    for i in range(1, K):
        num = lunlun[i]
        last = num % 10
        if last == 0:
            lunlun.append(num * 10 + last)
            lunlun.append(num * 10 + last + 1)
        elif last == 9:
            lunlun.append(num * 10 + last - 1)
            lunlun.append(num * 10 + last)
        else:
            lunlun.append(num * 10 + last - 1)
            lunlun.append(num * 10 + last)
            lunlun.append(num * 10 + last + 1)
    print(lunlun[K-1])

=======
Suggestion 3

def main():
    K = int(input())
    lunlun = [1,2,3,4,5,6,7,8,9]
    for i in range(K):
        if i < 9:
            continue
        num = lunlun[i]
        if num % 10 == 0:
            lunlun.append(num*10 + num % 10)
        elif num % 10 == 9:
            lunlun.append(num*10 + num % 10 - 1)
        else:
            lunlun.append(num*10 + num % 10)
            lunlun.append(num*10 + num % 10 - 1)
    print(lunlun[K-1])

=======
Suggestion 4

def solve():
    K = int(input())
    q = [i for i in range(1, 10)]
    for _ in range(K):
        x = q.pop(0)
        for i in range(-1, 2):
            y = x % 10 + i
            if y >= 0 and y <= 9:
                q.append(x * 10 + y)
    print(x)

solve()

=======
Suggestion 5

def lunlun(n, k):
    if k == 1:
        return n
    else:
        if n % 10 == 9:
            return lunlun(n * 10 + n % 10 - 1, k - 1)
        elif n % 10 == 0:
            return lunlun(n * 10 + n % 10 + 1, k - 1)
        else:
            return min(lunlun(n * 10 + n % 10 - 1, k - 1), lunlun(n * 10 + n % 10 + 1, k - 1))

k = int(input())
print(lunlun(0, k))

=======
Suggestion 6

def solve():
    from collections import deque
    import sys
    input = sys.stdin.readline
    K = int(input())
    q = deque(range(1, 10))
    for i in range(K):
        x = q.popleft()
        if x % 10 > 0:
            q.append(10 * x + x % 10 - 1)
        q.append(10 * x + x % 10)
        if x % 10 < 9:
            q.append(10 * x + x % 10 + 1)
    print(x)

=======
Suggestion 7

def lunlun(n):
    if n < 10:
        return n
    elif n < 100:
        return (n % 10) + 10 * lunlun(n // 10)
    else:
        return (n % 10) + 10 * lunlun(n // 10) + 100 * lunlun(n // 100)

K = int(input())
print(lunlun(K))

=======
Suggestion 8

def  lunlun ( n ) :
     if  n  <=   9 :
         return  [ str ( i )   for  i  in   range ( 1 , n + 1 ) ]
     else :
         return  [ str ( i )   for  i  in   range ( 1 , 10 ) ]  +  [ i + j  for  i  in  lunlun ( n // 10 )  for  j  in   [ str ( int ( i [ - 1 ] ) + k )   for  k  in   [ - 1 , 0 , 1 ]   if  0  <=  int ( i [ - 1 ] ) + k  < =   9 ]   if  i [ - 1 ]  !=   '0' ]  +  [ i + j  for  i  in  lunlun ( n // 10 + 1 )  for  j  in   [ str ( int ( i [ - 1 ] ) + k )   for  k  in   [ - 1 , 0 , 1 ]   if  0  <=  int ( i [ - 1 ] ) + k  < =   9 ]   if  i [ - 1 ]  !=   '0' ]

=======
Suggestion 9

def lunlun(n):
    if n < 10:
        return n
    else:
        return lunlun(n // 10) + n % 10

=======
Suggestion 10

def lunlun(n):
    if n < 10:
        return n
    else:
        # 1桁目の取り出し
        a = n % 10
        # 1桁目以外の取り出し
        b = n // 10
        # 1桁目以外の最大値を取得
        c = max([int(i) for i in str(b)])
        # 1桁目以外の最小値を取得
        d = min([int(i) for i in str(b)])
        # 1桁目の値が最大値の場合
        if a == c:
            return 10 * lunlun(b) + a - 1
        # 1桁目の値が最小値の場合
        elif a == d:
            return 10 * lunlun(b) + a + 1
        # 1桁目の値が最大値と最小値の中間の場合
        else:
            return 10 * lunlun(b) + a

k = int(input())
n = 1
for i in range(k):
    n = lunlun(n)
print(n)
