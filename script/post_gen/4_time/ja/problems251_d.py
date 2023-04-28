Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    w = int(input())
    if w == 3:
        print(2)
        print(1, 2)
    elif w == 2:
        print(2)
        print(1, 2)
    elif w == 1:
        print(1)
        print(1)
    elif w == 4:
        print(3)
        print(1, 2, 4)
    elif w == 5:
        print(3)
        print(1, 2, 4)
    elif w == 6:
        print(3)
        print(1, 2, 3)
    elif w == 7:
        print(3)
        print(1, 2, 4)
    elif w == 8:
        print(3)
        print(1, 2, 4)
    elif w == 9:
        print(3)
        print(1, 2, 6)
    elif w == 10:
        print(3)
        print(1, 2, 6)
    elif w == 11:
        print(3)
        print(1, 2, 6)
    elif w == 12:
        print(3)
        print(1, 2, 3)
    elif w == 13:
        print(3)
        print(1, 2, 6)
    elif w == 14:
        print(3)
        print(1, 2, 6)
    elif w == 15:
        print(3)
        print(1, 2, 6)
    elif w == 16:
        print(3)
        print(1, 2, 6)
    elif w == 17:
        print(3)
        print(1, 2, 6)
    elif w == 18:
        print(3)
        print(1, 2, 3)
    elif w == 19:
        print(3)
        print(1, 2, 6)
    elif w == 20:
        print(3)
        print(1, 2, 6)
    elif w == 21:
        print(3)
        print(1, 2, 6)
    elif w == 22:
        print(3)
        print(1, 2,

=======
Suggestion 2

def main():
    w = int(input())
    if w <= 2:
        print("NO")
    elif w % 2 == 0:
        print("YES")
    else:
        print("NO")

=======
Suggestion 3

def get_divisors(num):
    divisors = []
    for i in range(1, int(num**0.5)+1):
        if num % i == 0:
            divisors.append(i)
            if i != num // i:
                divisors.append(num//i)
    return divisors

W = int(input())

=======
Suggestion 4

def main():
    W = int(input())
    if W == 3:
        print(2)
        print("1 2")
    elif W == 2:
        print(1)
        print("2")
    elif W == 1:
        print(1)
        print("1")
    elif W == 4:
        print(2)
        print("1 3")
    elif W == 5:
        print(2)
        print("2 3")
    elif W == 6:
        print(3)
        print("1 2 3")
    else:
        print(6)
        print("1 2 3 4 5 6")

=======
Suggestion 5

def main():
    W = int(input())
    if W <= 2:
        print(1)
        print(W)
    elif W <= 4:
        print(2)
        print(1, W-1)
    elif W <= 300:
        print(3)
        print(1, 2, 3)
    else:
        print(4)
        print(1, 2, 3, W-6)

=======
Suggestion 6

def solve():
    W = int(input())
    if W == 1:
        print(1)
        print(1)
    elif W == 2:
        print(2)
        print('1 2')
    elif W == 3:
        print(2)
        print('1 2')
    elif W == 4:
        print(3)
        print('1 2 4')
    elif W == 5:
        print(3)
        print('1 2 4')
    elif W == 6:
        print(3)
        print('1 2 4')
    elif W == 7:
        print(3)
        print('1 2 6')
    elif W == 8:
        print(4)
        print('1 2 6 8')
    elif W == 9:
        print(4)
        print('1 2 6 8')
    elif W == 10:
        print(4)
        print('1 2 6 8')
    elif W == 11:
        print(4)
        print('1 2 6 8')
    elif W == 12:
        print(4)
        print('1 2 6 8')
    elif W == 13:
        print(4)
        print('1 2 6 8')
    elif W == 14:
        print(4)
        print('1 2 6 8')
    elif W == 15:
        print(4)
        print('1 2 6 8')
    elif W == 16:
        print(5)
        print('1 2 6 8 16')
    elif W == 17:
        print(5)
        print('1 2 6 8 16')
    elif W == 18:
        print(5)
        print('1 2 6 8 16')
    elif W == 19:
        print(5)
        print('1 2 6 8 16')
    elif W == 20:
        print(5)
        print('1 2 6 8 16')
    elif W == 21:
        print(5)
        print('1 2 6 8 16')
    elif W == 22:
        print(5)
        print('1 2

=======
Suggestion 7

def main():
    w = int(input())
    if w == 3:
        print(2)
        print(1,2)
    else:
        print(3)
        if w % 2 == 0:
            print(w//2,w//2,1)
        else:
            print(w//2,w//2+1,1)

=======
Suggestion 8

def get_weight(n):
    if n == 1:
        return [1]
    if n == 2:
        return [1, 2]
    if n == 3:
        return [1, 2, 3]
    if n % 2 == 0:
        return get_weight(n-1) + [n]
    else:
        return get_weight(n-2) + [n]

=======
Suggestion 9

def main():
    w = int(input())
    print(2)
    print(w//2, w//2 + w%2)
