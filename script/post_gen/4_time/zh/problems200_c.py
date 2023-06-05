Synthesizing 10/10 solutions

=======
Suggestion 1

def solve():
    N = int(input())
    A = list(map(int, input().split()))
    #A = [int(i) for i in input().split()]
    cnt = [0] * 200
    for a in A:
        cnt[a % 200] += 1
    ans = 0
    for i in range(200):
        ans += cnt[i] * (cnt[i] - 1) // 2
    print(ans)

=======
Suggestion 2

def main():
    n = int(input())
    a = list(map(int, input().split()))
    cnt = [0] * 200
    for x in a:
        cnt[x % 200] += 1
    ans = 0
    for i in range(200):
        ans += cnt[i] * (cnt[i] - 1) // 2
    print(ans)

main()

=======
Suggestion 3

def get_input():
    n = int(input())
    a = list(map(int, input().split()))
    return n, a

=======
Suggestion 4

def count_pairs(nums):
    count = 0
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if (nums[i] - nums[j]) % 200 == 0:
                count += 1
    return count

=======
Suggestion 5

def main():
    # 读取输入
    n = int(input())
    a = list(map(int, input().split()))
    # 用字典存储余数
    dic = {}
    for i in range(n):
        a[i] = a[i] % 200
        if a[i] in dic:
            dic[a[i]] += 1
        else:
            dic[a[i]] = 1
    # 计算结果
    ans = 0
    for i in dic:
        ans += dic[i]*(dic[i]-1)//2
    # 输出结果
    print(ans)

=======
Suggestion 6

def solve():
    N = int(input())
    A = [int(x) for x in input().split()]
    ans = 0
    cnt = [0] * 200
    for a in A:
        r = a % 200
        cnt[r] += 1
    for i in range(200):
        ans += cnt[i] * (cnt[i] - 1) // 2
    print(ans)

=======
Suggestion 7

def solve():
    n = int(input())
    a = list(map(int, input().split()))
    cnt = [0]*200
    for i in range(n):
        cnt[a[i]%200] += 1
    ans = 0
    for i in range(200):
        ans += cnt[i]*(cnt[i]-1)//2
    print(ans)

solve()

=======
Suggestion 8

def f(n, a):
    #从a中找出所有200的倍数，然后两两组合
    #找出所有200的倍数
    b = []
    for i in range(n):
        if a[i] % 200 == 0:
            b.append(i)
    #print(b)
    #两两组合
    count = 0
    for i in range(len(b)-1):
        for j in range(i+1, len(b)):
            count += 1
    return count

=======
Suggestion 9

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = [0] * 200
    for i in range(n):
        b[a[i] % 200] += 1
    ans = 0
    for i in range(200):
        ans += b[i] * (b[i] - 1) // 2
    print(ans)

=======
Suggestion 10

def main():
    n = int(input())
    a = [int(i) for i in input().split()]
    b = [0]*200
    for i in a:
        b[i%200] += 1
    ans = 0
    for i in b:
        ans += i*(i-1)//2
    print(ans)
