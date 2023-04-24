Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    w = int(input())
    if w % 2 == 0 and w > 2:
        print(2)
        print(w//2, w//2)
    else:
        print(3)
        print(1, 2, w-3)

=======
Suggestion 2

def main():
    W = int(input())
    if W == 2:
        print(2)
        print(1, 1)
        return
    if W == 3:
        print(3)
        print(1, 1, 1)
        return
    if W % 2 == 0:
        print(W)
        for i in range(1, W + 1):
            print(i, end = " ")
        print()
        return
    else:
        print(W + 1)
        for i in range(1, W + 2):
            print(i, end = " ")
        print()
        return

=======
Suggestion 3

def main():
    W = int(input())
    if W % 2 == 0:
        ans = [W // 2, W // 2]
    else:
        ans = [W // 2, W // 2 + 1]
    print(len(ans))
    print(*ans)

=======
Suggestion 4

def main():
    W = int(input())
    N = W//2
    A = [2]*N
    if W%2 == 1:
        N += 1
        A.append(1)
    print(N)
    print(*A)

=======
Suggestion 5

def main():
    W = int(input())
    N = W // 2
    A = [2] * N
    A[0] = 1
    print(N)
    print(*A)

=======
Suggestion 6

def main():
    W = int(input())
    print(W)
    print(" ".join([str(i) for i in range(1, W + 1)]))

=======
Suggestion 7

def main():
    W = int(input())
    ans = []
    ans.append(1)
    ans.append(2)
    ans.append(3)
    ans.append(4)
    ans.append(5)
    ans.append(6)
    ans.append(7)
    ans.append(8)
    ans.append(9)
    ans.append(10)
    ans.append(11)
    ans.append(12)
    ans.append(13)
    ans.append(14)
    ans.append(15)
    ans.append(16)
    ans.append(17)
    ans.append(18)
    ans.append(19)
    ans.append(20)
    ans.append(21)
    ans.append(22)
    ans.append(23)
    ans.append(24)
    ans.append(25)
    ans.append(26)
    ans.append(27)
    ans.append(28)
    ans.append(29)
    ans.append(30)
    ans.append(31)
    ans.append(32)
    ans.append(33)
    ans.append(34)
    ans.append(35)
    ans.append(36)
    ans.append(37)
    ans.append(38)
    ans.append(39)
    ans.append(40)
    ans.append(41)
    ans.append(42)
    ans.append(43)
    ans.append(44)
    ans.append(45)
    ans.append(46)
    ans.append(47)
    ans.append(48)
    ans.append(49)
    ans.append(50)
    ans.append(51)
    ans.append(52)
    ans.append(53)
    ans.append(54)
    ans.append(55)
    ans.append(56)
    ans.append(57)
    ans.append(58)
    ans.append(59)
    ans.append(60)
    ans.append(61)
    ans.append(62)
    ans.append(63)
    ans.append(64)
    ans.append(65)
    ans.append(66)
    ans.append(67)
    ans.append(68)
    ans.append(69)
    ans.append(70)
    ans.append(71)
    ans.append(72)
    ans.append(73)
    ans.append(74)
    ans.append(75)
    ans.append(76)
    ans.append(77)
    ans.append(78)
    ans.append(79)
    ans.append(80)
    ans.append(81)
    ans

=======
Suggestion 8

def main():
    W = int(input())
    if W % 2 == 1:
        print(W+1)
        for i in range(W):
            print(1, end=' ')
        print()
    else:
        print(W)
        for i in range(W):
            print(1, end=' ')
        print()

=======
Suggestion 9

def main():
    W = int(input())
    # 重さの和が W になるようにおもりを用意する
    # 1 以上 W 以下のすべての正整数は 良い整数 である。
    # 1 以上 W 以下の整数のうち、おもりの重さの和になるものを 良い整数 と呼ぶ
    # 1 以上 W 以下の正整数は、おもりの重さの和になるので、
    # 1 以上 W 以下の正整数は 良い整数 である。
    # 1 以上 W 以下の正整数は、いくつかのおもりを用いて、
    # おもりの重さの和になるので、良い整数である。
    # 1 以上 W 以下の正整数は、いくつかのおもりを用いて、
    # おもりの重さの和になるので、良い整数である。
    # 1 以上 W 以下の正整数は、いくつかのおもりを用いて、
    # おもりの重さの和になるので、良い整数である。
    # 1 以上 W 以下の正整数は、いくつかのおもりを用いて、
    # おもりの重さの和になるので、良い整数である。
    # 1 以上 W 以下の正整数は、いくつかのおもりを用いて、
    # おもりの重さの和になるので、良い整数である。
    # 1 以上 W 以下の正整数は、いくつかのおもりを用いて、
    # おもりの重さの和になるので、良い整数である。
    # 1 以上 W 以下の

=======
Suggestion 10

def main():
    W = int(input())
    N = W
    A = [1] * W
    for i in range(1, W):
        if N % 2 == 0:
            N = N // 2
            A[i] = 2
        else:
            N = N // 2 + 1
            A[i] = 2
    print(W)
    print(*A)
main()
