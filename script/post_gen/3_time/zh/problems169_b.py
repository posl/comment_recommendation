Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def mul_list(list):
    """
    :param list: list of integer
    :return: multiplication of the list
    """
    result = 1
    for i in range(len(list)):
        result = result * list[i]
    return result

=======
Suggestion 2

def main():
    n = int(input())
    a = list(map(int, input().split()))
    if 0 in a:
        print(0)
        exit()
    ans = 1
    for i in a:
        ans *= i
        if ans > 10**18:
            print(-1)
            exit()
    print(ans)

=======
Suggestion 3

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
Suggestion 4

def mul(a):
    m = 1
    for i in range(len(a)):
        m *= a[i]
    return m

n = int(input())
a = list(map(int, input().split()))

=======
Suggestion 5

def main():
    n = int(input())
    a = list(map(int, input().split()))
    if 0 in a:
        print(0)
        return
    ans = 1
    for i in range(n):
        ans *= a[i]
        if ans > 10**18:
            print(-1)
            return
    print(ans)

=======
Suggestion 6

def main():
    n = int(input())
    a = list(map(int, input().split()))
    if 0 in a:
        print(0)
        return
    p = 1
    for i in a:
        p *= i
        if p > 10**18:
            print(-1)
            return
    print(p)
    return
