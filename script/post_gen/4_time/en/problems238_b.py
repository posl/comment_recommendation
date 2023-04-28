Synthesizing 9/10 solutions

=======
Suggestion 1

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

=======
Suggestion 2

def main():
    N = int(input())
    A = list(map(int, input().split()))
    print(360 - sum(A))

=======
Suggestion 3

def main():
    n = int(input())
    a = list(map(int,input().split()))

    ans = 360
    for i in range(n):
        ans = min(ans, abs(360 - 2*sum(a[:i+1])))
    print(ans)

=======
Suggestion 4

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A = A[::-1]
    ans = 360
    for i in range(N):
        ans = ans - A[i]
    print(ans)

=======
Suggestion 5

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.reverse()
    sumA = sum(A)
    if sumA >= 360:
        print(sumA - 360)
    else:
        print(sumA)

=======
Suggestion 6

def main():
    n = int(input())
    a = list(map(int,input().split()))
    s = 180*(n+1)
    for i in range(n):
        s -= a[i]
    print(s)

=======
Suggestion 7

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A = [0] + A
    A = [a%360 for a in A]
    A = [a if a <= 180 else 360-a for a in A]
    A = [a if a <= 90 else 180-a for a in A]
    A = [a if a <= 45 else 90-a for a in A]
    A = [a if a <= 22.5 else 45-a for a in A]
    A = [a if a <= 11.25 else 22.5-a for a in A]
    A = [a if a <= 5.625 else 11.25-a for a in A]
    A = [a if a <= 2.8125 else 5.625-a for a in A]
    A = [a if a <= 1.40625 else 2.8125-a for a in A]
    A = [a if a <= 0.703125 else 1.40625-a for a in A]
    A = [a if a <= 0.3515625 else 0.703125-a for a in A]
    A = [a if a <= 0.17578125 else 0.3515625-a for a in A]
    A = [a if a <= 0.087890625 else 0.17578125-a for a in A]
    A = [a if a <= 0.0439453125 else 0.087890625-a for a in A]
    A = [a if a <= 0.02197265625 else 0.0439453125-a for a in A]
    A = [a if a <= 0.010986328125 else 0.02197265625-a for a in A]
    A = [a if a <= 0.0054931640625 else 0.010986328125-a for a in A]
    A = [a if a <= 0.00274658203125 else 0.0054931640625-a for a in A]
    A = [a if a <= 0.001373291015625 else 0.00274658203125-a for a in A]
    A = [

=======
Suggestion 8

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A = [360 - i for i in A]
    A = A[::-1]
    A.append(0)
    A = [A[i] - A[i+1] for i in range(N)]
    A = [i if i > 0 else i + 360 for i in A]
    print(360 - max(A))

=======
Suggestion 9

def main():
    N = int(input())
    A = list(map(int, input().split()))
    #print(N)
    #print(A)

    # 1. 360度をNで割った余りが答え
    # 2. 360度をNで割った余りが0の場合は、答えは360度
    # 3. 360度をNで割った余りが0以外の場合は、答えは360度から余りを引いたもの
    ans = 360 % N
    if ans == 0:
        ans = 360
    else:
        ans = 360 - ans
    print(ans)
