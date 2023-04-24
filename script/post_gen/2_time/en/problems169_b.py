Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 1
    for a in A:
        ans *= a
        if ans > 10**18:
            ans = -1
            break
    print(ans)

=======
Suggestion 2

def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 1
    for a in A:
        ans *= a
        if ans > 10**18:
            ans = -1
            break
    print(ans)

main()

=======
Suggestion 3

def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 1
    for i in range(N):
        ans *= A[i]
        if ans > 10**18:
            ans = -1
            break
    print(ans)

=======
Suggestion 4

def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 1
    for i in range(N):
        ans *= A[i]
        if ans > 10**18:
            print(-1)
            return
    print(ans)
    return

main()

=======
Suggestion 5

def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 1
    for i in range(n):
        if a[i] == 0:
            print(0)
            return
        ans *= a[i]
        if ans > 10**18:
            print(-1)
            return
    print(ans)

=======
Suggestion 6

def main():
    N = int(input())
    A = list(map(int, input().split()))
    if 0 in A:
        print(0)
    else:
        product = 1
        for i in range(N):
            product *= A[i]
            if product > 10**18:
                print(-1)
                return
        print(product)

=======
Suggestion 7

def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 1
    flag = 0
    for i in range(N):
        if A[i] == 0:
            flag = 1
            print(0)
            break
        if ans > 10 ** 18 // A[i]:
            flag = 1
            print(-1)
            break
        ans *= A[i]
    if flag == 0:
        print(ans)

=======
Suggestion 8

def main():
    n = int(input())
    a = list(map(int, input().split()))
    z = 1
    for i in range(n):
        z *= a[i]
    if z > 10**18:
        print(-1)
    else:
        print(z)

=======
Suggestion 9

def main():
    # Read the input
    n = int(input())
    a = list(map(int, input().split()))
    # Compute the product
    product = 1
    for i in range(n):
        product *= a[i]
    # Check if the product is > 10^18
    if product > 10**18:
        print(-1)
    else:
        print(product)
