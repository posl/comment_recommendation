Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    a, b = map(int, input().split())
    if a <= b <= a * 6:
        print("Yes")
    else:
        print("No")

=======
Suggestion 2

def main():
    A, B = map(int, input().split())
    if A <= B <= 6*A:
        print("Yes")
    else:
        print("No")

=======
Suggestion 3

def main():
    a,b = map(int, input().split())
    if a*1 <= b <= a*6:
        print('Yes')
    else:
        print('No')

=======
Suggestion 4

def main():
    a, b = map(int, input().split())
    if a <= b and b <= 6*a:
        print("Yes")
    else:
        print("No")

=======
Suggestion 5

def dice():
    a, b = map(int, input().split())
    if a <= 100 and b <= 1000:
        for i in range(1, a+1):
            for j in range(1, 7):
                if i * j == b:
                    print('Yes')
                    exit()
        print('No')
    else:
        print('No')

dice()

=======
Suggestion 6

def main():
    a,b = map(int,input().split())
    if 6*a >= b and a <= b:
        print('Yes')
    else:
        print('No')

main()

=======
Suggestion 7

def main():
    a, b = map(int, input().split())
    print("Yes" if a <= b <= a * 6 else "No")

=======
Suggestion 8

def dice(n):
    sum = 0
    for i in range(1,7):
        sum += i
        if sum == n:
            return True
    return False

a, b = map(int, input().split())

=======
Suggestion 9

def main():
    # 入力
    a, b = map(int, input().split())
    # 出力
    if a <= b and b <= a*6:
        print("Yes")
    else:
        print("No")
