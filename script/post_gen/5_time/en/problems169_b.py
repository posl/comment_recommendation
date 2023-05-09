Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    A = list(map(int, input().split()))
    if 0 in A:
        print(0)
        return
    ans = 1
    for a in A:
        ans *= a
        if ans > 10 ** 18:
            print(-1)
            return
    print(ans)

=======
Suggestion 2

def main():
    n = int(input())
    a = list(map(int, input().split()))
    if 0 in a:
        print(0)
    else:
        ans = 1
        for i in a:
            ans *= i
            if ans > 10 ** 18:
                print(-1)
                return
        print(ans)

=======
Suggestion 3

def main():
    n = int(input())
    a = list(map(int, input().split()))
    if 0 in a:
        print(0)
    else:
        ans = 1
        for i in a:
            ans *= i
            if ans > 10 ** 18:
                print(-1)
                exit()
        print(ans)

=======
Suggestion 4

def main():
    n = int(input())
    a = list(map(int, input().split()))
    if 0 in a:
        print(0)
        return
    ans = 1
    for i in a:
        ans *= i
        if ans > 10**18:
            print(-1)
            return
    print(ans)

=======
Suggestion 5

def main():
    N = int(input())
    A = list(map(int, input().split()))
    if 0 in A:
        print(0)
        return
    result = 1
    for a in A:
        result *= a
        if result > 10**18:
            print(-1)
            return
    print(result)

=======
Suggestion 6

def main():
    N = int(input())
    A = list(map(int, input().split()))
    if 0 in A:
        print(0)
        return
    res = 1
    for a in A:
        res *= a
        if res > 10**18:
            print(-1)
            return
    print(res)
    return

=======
Suggestion 7

def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 1
    for i in range(n):
        ans *= a[i]
        if ans > 10**18:
            ans = -1
            break
    print(ans)

=======
Suggestion 8

def main():
    n = int(input())
    a = list(map(int, input().split()))
    if 0 in a:
        print(0)
        return
    result = 1
    for i in range(n):
        result *= a[i]
        if result > 10**18:
            print(-1)
            return
    print(result)

=======
Suggestion 9

def main():
    N = int(input())
    A = list(map(int, input().split()))
    if 0 in A:
        print(0)
        exit()
    p = 1
    for i in A:
        p *= i
        if p > 10**18:
            print(-1)
            exit()
    print(p)
    exit()

=======
Suggestion 10

def compute_product_of_list(list):
    product = 1
    for item in list:
        product *= item
        if product > 10**18:
            return -1
    return product
