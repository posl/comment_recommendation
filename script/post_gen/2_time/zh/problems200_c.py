Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def find_pairs(a):
    pairs = 0
    for i in range(len(a)):
        for j in range(i+1, len(a)):
            if (a[i] - a[j]) % 200 == 0:
                pairs += 1
    return pairs

=======
Suggestion 2

def main():
    N = int(input())
    A = list(map(int, input().split()))
    cnt = [0]*200
    for i in range(N):
        cnt[A[i]%200] += 1
    ans = 0
    for i in range(200):
        ans += cnt[i]*(cnt[i]-1)//2
    print(ans)

=======
Suggestion 3

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = [a % 200 for a in A]
    C = [0] * 200
    for b in B:
        C[b] += 1
    ans = 0
    for c in C:
        ans += c * (c - 1) // 2
    print(ans)

=======
Suggestion 4

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = [0] * 200
    for i in range(N):
        B[A[i] % 200] += 1
    ans = 0
    for i in range(200):
        ans += B[i] * (B[i] - 1) // 2
    print(ans)

main()

=======
Suggestion 5

def get200(n, a):
    a.sort()
    a_dic = {}
    for i in a:
        if i % 200 in a_dic:
            a_dic[i % 200] += 1
        else:
            a_dic[i % 200] = 1
    res = 0
    for i in a_dic:
        res += a_dic[i] * (a_dic[i] - 1) / 2
    return res

=======
Suggestion 6

def main():
    n = int(input())
    a = list(map(int, input().split()))
    d = {}
    for i in range(n):
        if a[i] % 200 in d:
            d[a[i] % 200] += 1
        else:
            d[a[i] % 200] = 1
    ans = 0
    for i in d:
        ans += d[i] * (d[i] - 1) // 2
    print(ans)

=======
Suggestion 7

def solve():
    N = int(input())
    A = list(map(int, input().split()))
    B = [0] * 200
    for a in A:
        B[a % 200] += 1
    ans = 0
    for b in B:
        ans += b * (b - 1) // 2
    print(ans)

=======
Suggestion 8

def main():
    N = int(input())
    A = list(map(int, input().split()))
    # print(N)
    # print(A)

    # count = 0
    # for i in range(N):
    #     for j in range(i+1, N):
    #         if (A[i]-A[j])%200 == 0:
    #             count += 1
    # print(count)

    # 200的倍数，只有两种情况，一种是末尾两个数字相等，一种是末尾两个数字相加等于200
    # 1. 末尾两个数字相等
    # 2. 末尾两个数字相加等于200
    # 3. 末尾两个数字相加等于400
    # 4. 末尾两个数字相加等于600
    # 5. 末尾两个数字相加等于800
    # ...
    # 100个
    # 1. 末尾两个数字相等
    # 2. 末尾两个数字相加等于200
    # 3. 末尾两个数字相加等于400
    # 4. 末尾两个数字相加等于600
    # 5. 末尾两个数字相加等于800
    # ...
    # 100个
    # 1. 末尾两个数字相等
    # 2. 末尾两个数字相加等于200
    # 3. 末尾两个数字相加等于400
    # 4. 末尾两个数字相加等于600
    # 5. 末尾两个数字相加等于800
    # ...
    # 100个
    # 1. 末尾两个数字相等
    # 2. 末尾两个数字相加等于200
    # 3. 末尾两个数字相加等于400
    # 4. 末尾两

=======
Suggestion 9

def problems200_c():
    n = int(input())
    a = list(map(int, input().split()))
    b = [0] * 200
    for i in range(n):
        b[a[i] % 200] += 1
    ans = 0
    for i in range(200):
        ans += b[i] * (b[i] - 1) // 2
    print(ans)
problems200_c()
