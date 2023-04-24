Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    A = list(map(int, input().split()))
    c2 = 0
    c3 = 0
    for a in A:
        while a % 2 == 0:
            c2 += 1
            a //= 2
        while a % 3 == 0:
            c3 += 1
            a //= 3
        if a != 1:
            print(-1)
            return
    print(c2 + c3)

=======
Suggestion 2

def main():
    N = int(input())
    A = list(map(int, input().split()))
    count = 0
    while True:
        for i in range(N):
            if A[i] % 2 == 0:
                A[i] //= 2
            elif A[i] % 3 == 0:
                A[i] //= 3
            else:
                print(-1)
                return
        if len(set(A)) == 1:
            break
        count += 1
    print(count)

=======
Suggestion 3

def main():
    N = int(input())
    A = list(map(int, input().split()))
    two = 0
    three = 0
    for i in A:
        while i % 2 == 0:
            two += 1
            i //= 2
        while i % 3 == 0:
            three += 1
            i //= 3
    if len(set(A)) == 1:
        print(abs(two - three))
    else:
        print(-1)

=======
Suggestion 4

def main():
    n = int(input())
    a = list(map(int, input().split()))
    count = 0
    while True:
        if all(x == a[0] for x in a):
            break
        for i in range(n):
            if a[i] % 3 == 0:
                a[i] = a[i] // 3
                count += 1
                break
            elif a[i] % 2 == 0:
                a[i] = a[i] // 2
                count += 1
                break
        else:
            count = -1
            break
    print(count)

=======
Suggestion 5

def main():
    N = int(input())
    A = list(map(int, input().split()))
    cnt = 0
    while True:
        if len(set(A)) == 1:
            print(cnt)
            break
        for i in range(N):
            if A[i] % 3 == 0:
                A[i] = A[i] // 3
                cnt += 1
                break
            elif A[i] % 2 == 0:
                A[i] = A[i] // 2
                cnt += 1
                break
        else:
            print(-1)
            break

=======
Suggestion 6

def main():
    N = int(input())
    A = list(map(int, input().split()))
    count = 0

    while True:
        if all([a % 2 == 0 for a in A]):
            A = [a // 2 for a in A]
            count += 1
        elif all([a % 3 == 0 for a in A]):
            A = [a // 3 for a in A]
            count += 1
        else:
            break

    if all([a == A[0] for a in A]):
        print(count)
    else:
        print(-1)

=======
Suggestion 7

def main():
    n = int(input())
    a = list(map(int, input().split()))
    count = 0
    while True:
        if len(set(a)) == 1:
            print(count)
            break
        if all([i % 2 == 0 for i in a]):
            a = [i / 2 for i in a]
            count += 1
        elif all([i % 3 == 0 for i in a]):
            a = [i / 3 for i in a]
            count += 1
        else:
            print(-1)
            break

=======
Suggestion 8

def main():
    N = int(input())
    As = list(map(int, input().split()))
    min_A = min(As)

    # N=1の時は0を出力
    if N == 1:
        print(0)
        return

    # min_Aが2の倍数でない時は-1を出力
    if min_A % 2 != 0:
        print(-1)
        return

    # Asの要素を2で割り続ける回数を数える
    count = 0
    while True:
        for i in range(N):
            if As[i] % 2 != 0:
                print(-1)
                return
            As[i] //= 2
        if min(As) == min_A:
            break
        count += 1

    print(count)

=======
Suggestion 9

def main():
    N = int(input())
    A = list(map(int, input().split()))
    print("N =", N)
    print("A =", A)
    print("")

    # convert A to a list of 2s and 3s
    B = []
    for i in range(N):
        while A[i] % 2 == 0:
            A[i] = A[i] // 2
            B.append(2)
        while A[i] % 3 == 0:
            A[i] = A[i] // 3
            B.append(3)
    print("B =", B)
    print("")

    # check if all elements of A are equal
    for i in range(N-1):
        if A[i] != A[i+1]:
            print(-1)
            return

    # count the number of 2s and 3s in B
    count2 = 0
    count3 = 0
    for i in range(len(B)):
        if B[i] == 2:
            count2 += 1
        if B[i] == 3:
            count3 += 1
    print("count2 =", count2)
    print("count3 =", count3)
    print("")

    # find the minimum number of operations
    print(min(count2, count3) + abs(count2 - count3))

=======
Suggestion 10

def count_operations(a_list):
    # your code here
    return 0
