Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

N = int(input())
A = list(map(int, input().split()))

=======
Suggestion 2

def gcd(a, b):
    if a < b:
        a, b = b, a
    while b != 0:
        a, b = b, a % b
    return a

=======
Suggestion 3

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

=======
Suggestion 4

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

=======
Suggestion 5

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

=======
Suggestion 6

def main():
    N = int(input())
    A = list(map(int, input().split()))
    if N == 2:
        print(gcd(A[0], A[1]))
        return
    A.sort()
    # print(A)
    # print(gcd(A[0], A[1]))
    # print(gcd(A[1], A[2]))
    # print(gcd(A[0], A[2]))
    print(max(gcd(A[0], A[1]), gcd(A[1], A[2]), gcd(A[0], A[2])))

=======
Suggestion 7

def main():
    N = int(input())
    A = list(map(int, input().split()))

    # Aの最大値を求める
    max_A = max(A)

    # Aの最大値の約数を求める
    max_A_divs = []
    for i in range(1, int(max_A**0.5)+1):
        if max_A % i == 0:
            max_A_divs.append(i)
            if i != max_A // i:
                max_A_divs.append(max_A // i)

    # Aの最大値の約数のうち、Aの約数になっているものを求める
    A_divs = []
    for div in max_A_divs:
        for a in A:
            if a % div != 0:
                break
        else:
            A_divs.append(div)

    # Aの最大値の約数のうち、Aの約数になっているもののうち、最大のものを求める
    print(max(A_divs))
