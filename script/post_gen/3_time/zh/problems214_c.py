Synthesizing 10/10 solutions

=======
Suggestion 1

def find_first_time(N, S, T):
    # Snuke i（1 ≦ i ≦ N）在时间t收到一颗宝石，S_i单位的时间后，它将在时间t+S_i将该宝石交给Snuke i+1
    # 高桥将在时间T_i递给Snuke i一颗宝石。
    # 对于每个i（1 ≦ i ≦ N），找出Snuke i第一次收到宝石的时间
    # 按照时间顺序列出Snuke三人和Takahashi到时间13为止的行动。
    # 时间3：高桥将一颗宝石交给Snuke 1。
    # 时间7：斯诺克1把宝石交给斯诺克2。
    # 时间8：Snuke 2将一颗宝石交给Snuke 3。
    # 时间10：高桥将一颗宝石交给Snuke 2。
    # 时间11：Snuke 2递给Snuke 3一颗宝石。
    # 时间13：Snuke 3将一颗宝石交给Snuke 1。
    # 此后，他们将继续递送宝石，尽管这与答案无关。
    # 请注意，S_i和T_i的值可能不是不同的。
    # 请注意，一个Snuke可以同时进行多个交易。特别是，一个Snuke可以同时从高桥和另一个Snuke那里接收宝石。
    # 请注意，Snuke i（1 ≦ i ≦ N）在时间t收到一颗宝石，S_i单位的时间后，它将在时间t+S_i将该宝石交给Snuke i+1。
    # 此外，高桥将在时间T_i递给Snuke i一颗

=======
Suggestion 2

def main():
    N = int(input())
    S = list(map(int, input().split()))
    T = list(map(int, input().split()))
    for i in range(N):
        if i == 0:
            time = T[i]
            continue
        else:
            if time > T[i]:
                time = T[i]
            else:
                pass
        time += S[i]
        print(time)

=======
Suggestion 3

def main():
    pass

=======
Suggestion 4

def main():
    n = int(input())
    s = list(map(int, input().split()))
    t = list(map(int, input().split()))
    ans = [0] * n
    for i in range(n):
        ans[i] = t[i]
    for i in range(n):
        if ans[i] > ans[(i-1)%n] + s[(i-1)%n]:
            ans[i] = ans[(i-1)%n] + s[(i-1)%n]
    for i in range(n):
        print(ans[i])

=======
Suggestion 5

def main():
    N = int(input())
    S = list(map(int, input().split()))
    T = list(map(int, input().split()))

    # print(N, S, T)

    # 1. 找到最小的T对应的S
    # 2. 从最小的T对应的S开始，逐个找到S对应的T
    # 3. 找到S对应的T后，从该T开始，逐个找到S对应的T

    minT = min(T)
    minT_index = T.index(minT)
    # print(minT, minT_index)
    # print(S[minT_index])

    for i in range(N):
        if i == minT_index:
            print(minT)
        else:
            print(min(minT + S[minT_index], T[i]))

=======
Suggestion 6

def main():
    n = int(input())
    s = list(map(int, input().split()))
    t = list(map(int, input().split()))
    ans = [0] * n
    for i in range(n):
        ans[i] = t[i]
        if i > 0 and ans[i] <= ans[i - 1]:
            ans[i] = ans[i - 1] + 1
        if i < n - 1 and s[i] + ans[i] <= ans[i + 1]:
            ans[i] = ans[i + 1] - s[i]
    for i in range(n):
        print(ans[i])

=======
Suggestion 7

def problem214_c():
    n = int(input())
    s = list(map(int, input().split()))
    t = list(map(int, input().split()))

    # print(n)
    # print(s)
    # print(t)

    res = [0] * n

    for i in range(n):
        res[i] = t[i]

    for i in range(n):
        if i == 0:
            if s[i] < t[i]:
                res[i] = s[i]
        else:
            if s[i] < t[i]:
                res[i] = s[i]
            else:
                if res[i-1] + s[i-1] < t[i]:
                    res[i] = res[i-1] + s[i-1]
                else:
                    res[i] = t[i]


    for i in range(n):
        print(res[i])

=======
Suggestion 8

def problems214_c():
    pass

=======
Suggestion 9

def main():
    n = int(input())
    s = list(map(int, input().split()))
    t = list(map(int, input().split()))
    t.sort()
    t = t[:n]
    for i in range(n):
        if t[i] < s[i]:
            t[i] = s[i]
    print(min(t))

=======
Suggestion 10

def main():
    n = int(input())
    s = list(map(int, input().split()))
    t = list(map(int, input().split()))
    ans = [0] * n
    for i in range(n):
        if i == 0:
            ans[0] = t[0]
        else:
            ans[i] = min(ans[i-1]+s[i-1], t[i])
    for i in range(n):
        print(ans[i])
