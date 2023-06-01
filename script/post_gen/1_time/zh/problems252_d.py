Synthesizing 10/10 solutions

=======
Suggestion 1

def solve(N, A):

=======
Suggestion 2

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a = sorted(a)
    ans = 0
    for i in range(n-2):
        for j in range(i+1,n-1):
            for k in range(j+1,n):
                if a[i] != a[j] and a[j] != a[k]:
                    ans += 1
    print(ans)

=======
Suggestion 3

def find_unique_triple(n, a):
    # 1. 首先将a中的元素进行排序
    a.sort()
    print("a = ", a)
    # 2. 从a中找出不同的元素，以及每个元素出现的次数
    unique_a = []
    count_a = []
    for i in range(0, n):
        if a[i] not in unique_a:
            unique_a.append(a[i])
            count_a.append(1)
        else:
            count_a[-1] += 1
    print("unique_a = ", unique_a)
    print("count_a = ", count_a)
    # 3. 计算满足条件的三联体的数量
    unique_count = len(unique_a)
    sum_count = sum(count_a)
    # 3.1 计算满足条件的三联体的数量
    triple_count = 0
    for i in range(0, unique_count-2):
        for j in range(i+1, unique_count-1):
            for k in range(j+1, unique_count):
                triple_count += count_a[i]*count_a[j]*count_a[k]
    # 3.2 计算满足条件的三联体的数量
    for i in range(0, unique_count-1):
        for j in range(i+1, unique_count):
            triple_count += count_a[i]*(count_a[i]-1)*count_a[j]//2
    # 3.3 计算满足条件的三联体的数量
    for i in range(0, unique_count):
        triple_count += count_a[i]*(count_a[i]-1)*(count_a[i]-2)//6
    # 4. 返回满足条件的三联体的数量
    return triple_count

=======
Suggestion 4

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    count = 0
    for i in range(N):
        for j in range(i+1, N):
            for k in range(j+1, N):
                if A[i] != A[j] and A[j] != A[k]:
                    count += 1
    print(count)

=======
Suggestion 5

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    a.append(0)
    ans = 0
    l = 0
    for i in range(n):
        if a[i] == a[i+1]:
            l += 1
        else:
            ans += l * (l-1) // 2
            l = 0
    print(ans)

=======
Suggestion 6

def main():
    n = int(input())
    a = list(map(int, input().split()))
    cnt = [0] * (max(a)+1)
    for v in a:
        cnt[v] += 1
    ans = 0
    for i in range(len(cnt)):
        if cnt[i] >= 3:
            ans += cnt[i] * (cnt[i]-1) * (cnt[i]-2) // 6
        if cnt[i] >= 2:
            for j in range(i+1, len(cnt)):
                if cnt[j] >= 2:
                    ans += cnt[i] * (cnt[i]-1) // 2 * cnt[j] * (cnt[j]-1) // 2
                if cnt[j] >= 1:
                    for k in range(j+1, len(cnt)):
                        if cnt[k] >= 1:
                            ans += cnt[i] * cnt[j] * cnt[k]
    print(ans)

=======
Suggestion 7

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    # print(A)
    # print(len(A))
    # print(A[len(A)-1])
    # print(A[len(A)-2])
    # print(A[len(A)-3])
    # print(A[len(A)-4])
    # print(A[len(A)-5])
    # print(A[len(A)-6])
    # print(A[len(A)-7])
    # print(A[len(A)-8])
    # print(A[len(A)-9])
    # print(A[len(A)-10])
    # print(A[len(A)-11])
    # print(A[len(A)-12])
    # print(A[len(A)-13])
    # print(A[len(A)-14])
    # print(A[len(A)-15])
    # print(A[len(A)-16])
    # print(A[len(A)-17])
    # print(A[len(A)-18])
    # print(A[len(A)-19])
    # print(A[len(A)-20])
    # print(A[len(A)-21])
    # print(A[len(A)-22])
    # print(A[len(A)-23])
    # print(A[len(A)-24])
    # print(A[len(A)-25])
    # print(A[len(A)-26])
    # print(A[len(A)-27])
    # print(A[len(A)-28])
    # print(A[len(A)-29])
    # print(A[len(A)-30])
    # print(A[len(A)-31])
    # print(A[len(A)-32])
    # print(A[len(A)-33])
    # print(A[len(A)-34])
    # print(A[len(A)-35])
    # print(A[len(A)-36])
    # print(A[len(A)-37])
    # print(A[len(A)-38])
    # print(A[len(A)-39])
    # print(A[len(A)-40])
    # print(A[len(A)-41])
    # print(A[len(A)-42])
    # print(A[len(A)-43])
    # print(A[len(A)-44])
    # print(A[len(A)-45])
    # print(A[len(A)-46])
    # print(A[len(A)-47])
    # print(A[len(A)-48])
    # print(A[len(A)-49])
    # print(A[len(A)-50])
    # print(A[len(A)-51])
    # print(A[len(A)-

=======
Suggestion 8

def main():
    N = int(input())
    A = list(map(int, input().split()))
    count = 0
    for i in range(N-2):
        for j in range(i+1,N-1):
            for k in range(j+1,N):
                if A[i] != A[j] and A[j] != A[k] and A[i] != A[k]:
                    if A[i] + A[j] > A[k] and A[i] + A[k] > A[j] and A[j] + A[k] > A[i]:
                        count += 1
    print(count)

=======
Suggestion 9

def get_input():
    n = int(input())
    a = list(map(int, input().split()))
    return n, a

=======
Suggestion 10

def main():
    n = int(input())
    a = list(map(int, input().split()))
    c = [0] * 200005
    for i in range(n):
        c[a[i]] += 1
    s = 0
    for i in range(200005):
        s += c[i] * (c[i] - 1) * (c[i] - 2) // 6
    for i in range(200005):
        s -= c[i] * (c[i] - 1) // 2 * (n - c[i])
    for i in range(200005):
        for j in range(i + 1, 200005):
            s -= c[i] * c[j] * (c[j] - 1) // 2
    print(s)
