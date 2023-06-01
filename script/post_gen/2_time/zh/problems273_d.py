Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    A = list(map(int, input().split()))
    # print(N, A)

    # print(N, A)
    # print(A)
    # print(N, A)

    # N = 6
    # A = [2, 7, 1, 8, 2, 8]

    # N = 10
    # A = [979861204, 57882493, 979861204, 447672230, 644706927, 710511029, 763027379, 710511029, 447672230, 136397527]

    # N = 1
    # A = [1]

    # N = 2
    # A = [1, 1]

    # N = 3
    # A = [1, 1, 1]

    # N = 4
    # A = [1, 1, 1, 1]

    # N = 5
    # A = [1, 1, 1, 1, 1]

    # N = 6
    # A = [1, 1, 1, 1, 1, 1]

    # N = 7
    # A = [1, 1, 1, 1, 1, 1, 1]

    # N = 8
    # A = [1, 1, 1, 1, 1, 1, 1, 1]

    # N = 9
    # A = [1, 1, 1, 1, 1, 1, 1, 1, 1]

    # N = 10
    # A = [1, 1, 1, 1, 1, 1, 1, 1, 1,

=======
Suggestion 2

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a = sorted(a)
    ans = [0] * n
    for i in range(n):
        if i == 0:
            ans[0] = 0
        elif a[i] == a[i-1]:
            ans[i] = ans[i-1]
        else:
            ans[i] = ans[i-1] + 1
    for i in range(n):
        print(ans[i])

=======
Suggestion 3

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a = [0] + a
    a.sort()
    print(a)
    ans = [0] * (n + 1)
    ans[0] = 0
    for i in range(1, n + 1):
        if a[i] != a[i - 1]:
            ans[i] = ans[i - 1] + 1
        else:
            ans[i] = ans[i - 1]
    print(ans)
    for i in range(1, n + 1):
        print(ans[i])

=======
Suggestion 4

def main():
    n = int(input())
    a = list(map(int, input().split()))
    d = {}
    for i in range(n):
        if a[i] in d:
            d[a[i]] += 1
        else:
            d[a[i]] = 1
    d = sorted(d.items(), key=lambda x: x[0])
    #print(d)
    ans = 0
    for i in range(len(d)):
        ans += d[i][1]
        d[i] = (d[i][0], ans)
    #print(d)
    for i in range(n):
        for j in range(len(d)):
            if a[i] == d[j][0]:
                print(d[j][1] - 1)
                break

=======
Suggestion 5

def problems273_c():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    A.append(10**9+1)
    ans = [0] * N
    cnt = 0
    for i in range(N):
        if A[i] != A[i+1]:
            for j in range(cnt, i+1):
                ans[j] = i - cnt + 1
            cnt = i + 1
    print('\n'.join(map(str, ans)))
    return 0

=======
Suggestion 6

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a = sorted(a)
    a.append(0)
    k = 0
    for i in range(n):
        if a[i] != a[i+1]:
            print(k)
            k = 0
        else:
            k += 1

=======
Suggestion 7

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    ans = [0] * n
    for i in range(n):
        if i == 0:
            ans[i] = 1
        elif a[i] == a[i-1]:
            ans[i] = ans[i-1]
        else:
            ans[i] = ans[i-1] + 1
    for i in range(n):
        print(ans[i])

=======
Suggestion 8

def solve():
    # 读入数据
    N = int(input())
    A = list(map(int, input().split()))

    # 用于存储答案
    ans = [0] * N

    # 用于存储之前的出现过的数字
    used = set()

    # 用于存储之前的出现过的数字的个数
    used_count = 0

    # 从后往前遍历
    for i in range(N - 1, -1, -1):

        # 如果A[i]之前没有出现过
        if A[i] not in used:
            # 之前出现过的数字的个数+1
            used_count += 1
            # 将A[i]加入到已经出现过的数字中
            used.add(A[i])

        # 之前出现过的数字的个数就是答案
        ans[i] = used_count

    # 输出答案
    for i in range(N):
        print(ans[i])

=======
Suggestion 9

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    k = 0
    for i in range(n):
        if i != 0 and a[i] != a[i-1]:
            k += 1
        print(k)

=======
Suggestion 10

def get_count(a):
    count = 0
    for i in range(len(a)):
        for j in range(i+1,len(a)):
            if a[i] < a[j]:
                count += 1
    return count
