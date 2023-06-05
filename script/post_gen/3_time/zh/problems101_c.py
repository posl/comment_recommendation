Synthesizing 9/10 solutions

=======
Suggestion 1

def solve(N, K, A):
    # Write your code here
    # To debug: print("Debug messages...", file=sys.stderr, flush=True)
    # Return the number of operations
    if K == 2:
        return N - 1
    else:
        return N - 2

=======
Suggestion 2

def get_min_element(start, end, a):
    min_element = 100000
    for i in range(start, end + 1):
        if a[i] < min_element:
            min_element = a[i]
    return min_element

=======
Suggestion 3

def main():
    n,k=map(int,input().split())
    a=list(map(int,input().split()))
    if k==1:
        print(0)
        return
    ans=0
    for i in range(n-k+1):
        if a[i+k-1]==min(a[i:i+k]):
            ans+=1
    print(ans)

=======
Suggestion 4

def problems101_c():
    print("problems101_c")

=======
Suggestion 5

def solve():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        if i == 0:
            ans += 1
        else:
            if (a[i] - a[i - 1]) % (k - 1) != 0:
                ans += 1
    print(ans)

=======
Suggestion 6

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        if i == 0:
            ans += 1
        else:
            ans += (K-1)
    print(ans)

=======
Suggestion 7

def problems101_c():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        if i % (k - 1) == 0:
            ans += 1
    print(ans)

problems101_c()

=======
Suggestion 8

def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        if i == 0:
            ans += 1
        elif a[i] > a[i-1]:
            ans += 1
    print(ans)

=======
Suggestion 9

def main():
    # 读入数据
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    # print(n, k, a)
    # 初始化
    ans = 0
    # 遍历，找到最小值
    for i in range(n):
        ans += 1
        # 如果最小值是在最后的k个数里，那么就不用再往后找了
        if i + k - 1 >= n:
            break
        # 找到最小值
        min_num = a[i]
        # 遍历，找到最小值
        for j in range(k):
            if a[i + j] < min_num:
                min_num = a[i + j]
        # 替换
        for j in range(k):
            a[i + j] = min_num
    # 输出
    print(ans)
