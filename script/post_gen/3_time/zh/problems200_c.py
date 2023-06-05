Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    a = [int(i) for i in input().split()]
    ans = 0
    cnt = [0] * 200
    for i in range(n):
        ans += cnt[a[i] % 200]
        cnt[a[i] % 200] += 1
    print(ans)

=======
Suggestion 2

def get_ans(N,A):
    ans = 0
    for i in range(N):
        for j in range(i+1,N):
            if (A[i]-A[j])%200 == 0:
                ans += 1
    return ans

=======
Suggestion 3

def get_input():
    N = int(input())
    A = [int(x) for x in input().split()]
    return N, A

=======
Suggestion 4

def problems200_c():
    N = int(input())
    A = list(map(int, input().split()))
    #print(N, A)
    D = {}
    for i in range(N):
        r = A[i] % 200
        if r in D:
            D[r] += 1
        else:
            D[r] = 1
    #print(D)
    ans = 0
    for k in D:
        if D[k] > 1:
            ans += D[k] * (D[k]-1) // 2
    print(ans)

=======
Suggestion 5

def count_pairs(A):
    count = 0
    for i in range(len(A)):
        for j in range(i+1, len(A)):
            if (A[i] - A[j]) % 200 == 0:
                count += 1
    return count

=======
Suggestion 6

def solve():
    # 读取输入
    N = int(input())
    A = list(map(int, input().split()))
    # 用于计数的数组
    B = [0] * 200
    # 遍历输入，计数
    for a in A:
        B[a % 200] += 1
    # 计算答案
    ans = 0
    for b in B:
        ans += b * (b - 1) // 2
    # 输出答案
    print(ans)

=======
Suggestion 7

def main():
    # 读取输入
    N = int(input())
    A = list(map(int, input().split()))
    # 保存余数的计数器
    r = [0] * 200
    # 计算余数
    for a in A:
        r[a % 200] += 1
    # 计算配对数
    ans = 0
    for i in range(200):
        ans += r[i] * (r[i] - 1) // 2
    # 输出答案
    print(ans)

=======
Suggestion 8

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = [0]*200
    for a in A:
        B[a%200] += 1
    count = 0
    for b in B:
        count += b*(b-1)//2
    print(count)
main()

=======
Suggestion 9

def problems200_c():
    N = int(input())
    A = list(map(int,input().split()))
    cnt = [0]*200
    for i in range(N):
        cnt[A[i]%200] += 1
    ans = 0
    for i in range(200):
        ans += cnt[i]*(cnt[i]-1)//2
    print(ans)

=======
Suggestion 10

def solve():
    answer = 0
    # 问题解决方案:
    # 1. 如果有200的倍数, 则必然存在两个数的差是200的倍数
    # 2. 如果两个数的差是200的倍数, 则这两个数对200取余数必然是相同的
    # 3. 因此, 可以遍历取余数, 然后统计每个余数的数目, 然后(1+2+...n-1)即为所求
    # 4. 注意, 如果余数是0, 则需要特殊处理, 因为0是所有数的倍数, 所以需要单独统计
    # 5. 注意, 如果余数是100, 则需要特殊处理, 因为100是所有数的倍数, 所以需要单独统计
    remainder_dict = {}
    for num in num_list:
        remainder = num % 200
        if remainder == 0:
            answer += remainder_dict.get(0, 0)
            remainder_dict[0] = remainder_dict.get(0, 0) + 1
        elif remainder == 100:
            answer += remainder_dict.get(100, 0)
            remainder_dict[100] = remainder_dict.get(100, 0) + 1
        else:
            answer += remainder_dict.get(remainder, 0)
            remainder_dict[remainder] = remainder_dict.get(remainder, 0) + 1
    return answer
