Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

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
Suggestion 2

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
Suggestion 3

def main():
    # 读入数据
    n = int(input())
    a = list(map(int, input().split()))

    # 检查是否包含0
    if 0 in a:
        print(0)
        return

    # 计算答案
    ans = 1
    for i in range(n):
        ans *= a[i]
        if ans > 10 ** 18:
            print(-1)
            return

    print(ans)

=======
Suggestion 4

def solve(input):
    result = 1
    for i in input:
        if i == 0:
            return 0
        else:
            result *= i
            if result > 10 ** 18:
                return -1
    return result

=======
Suggestion 5

def main():
    n = int(input())
    a_list = list(map(int, input().split()))
    if 0 in a_list:
        print(0)
        return
    ans = 1
    for i in range(n):
        ans *= a_list[i]
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
    ans = 1
    for i in range(n):
        ans *= a[i]
        if ans > 1e18:
            print(-1)
            return
    print(ans)

=======
Suggestion 7

def main():
    N = int(input())
    A = list(map(int,input().split()))
    if 0 in A:
        print(0)
    else:
        ans = 1
        for i in range(N):
            ans *= A[i]
            if ans > 10**18:
                print(-1)
                break
        else:
            print(ans)
main()

=======
Suggestion 8

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
