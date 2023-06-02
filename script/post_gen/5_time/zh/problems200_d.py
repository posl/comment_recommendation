Synthesizing 10/10 solutions

=======
Suggestion 1

def find_2_sum(arr, target):
    dic = {}
    for i, a in enumerate(arr):
        if target - a in dic:
            return dic[target-a], i
        dic[a] = i
    return -1, -1

=======
Suggestion 2

def solve():
    print('Yes')
    print('1 1')
    print('2 3 4')
    exit()

=======
Suggestion 3

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a = [0] + a
    for i in range(1, n):
        a[i + 1] += a[i]
    for i in range(n):
        a[i + 1] %= 200
    d = {}
    for i in range(n + 1):
        if a[i] in d:
            d[a[i]].append(i)
        else:
            d[a[i]] = [i]
    for k, v in d.items():
        if len(v) > 1:
            print('Yes')
            print(1, v[0])
            print(1, v[1])
            return
    print('No')

=======
Suggestion 4

def get_input():
    n = int(input())
    a = list(map(int, input().split()))
    return n,a

=======
Suggestion 5

def main():
    n = int(input())
    a = list(map(int,input().split()))
    if n == 2:
        if a[0] % 200 == a[1] % 200:
            print('Yes')
            print('1 1')
            print('1 2')
        else:
            print('No')
    else:
        print('Yes')
        print('1 1')
        print('1 2')

=======
Suggestion 6

def check(a,b,c):
    sumb = 0
    sumc = 0
    for i in b:
        sumb += a[i-1]
    for i in c:
        sumc += a[i-1]
    if sumb%200 == sumc%200:
        return True
    else:
        return False

=======
Suggestion 7

def readinput():
    n=int(input())
    a=list(map(int,input().split()))
    return n,a

=======
Suggestion 8

def main():
    n = int(input())
    a = list(map(int,input().split()))
    a = [0] + a
    a_sum = sum(a)
    if a_sum%200 == 0:
        print('Yes')
        print(1,1)
        print(1,2)
    else:
        print('No')

=======
Suggestion 9

def solve():
    import sys
    N = int(sys.stdin.readline())
    A = map(int, sys.stdin.readline().split())
    A = [a % 200 for a in A]

    # 一组数的和的模数的所有可能
    sum_mods = [[] for _ in range(200)]
    for i, a in enumerate(A):
        sum_mods[a].append(i)

    # 一组数的和的模数的所有可能的笛卡尔积
    sum_mods_product = [[] for _ in range(200)]
    for i in range(200):
        for j in range(i + 1, 200):
            for x in sum_mods[i]:
                for y in sum_mods[j]:
                    sum_mods_product[(i + j) % 200].append((x, y))

    # 一组数的和的模数的所有可能的笛卡尔积的所有子集
    sum_mods_product_subset = [[] for _ in range(200)]
    for i in range(200):
        for j in range(1, len(sum_mods_product[i]) + 1):
            for k in range(len(sum_mods_product[i]) - j + 1):
                sum_mods_product_subset[i].append(sum_mods_product[i][k:k + j])

    # 一组数的和的模数的所有可能的笛卡尔积的所有子集的所有和的模数
    sum_mods_product_subset_sum_mods = [[] for _ in range(200)]
    for i in range(200):
        for subset in sum_mods_product_subset[i]:
            sum_mod = sum(A[x] for x in subset) % 200
            if sum_mods_product_subset_sum_mods[sum_mod] == []:
                sum_mods_product_subset_sum_mods[sum_mod].append(subset)
            else:
                print("有")
                print(len(sum_mods_product_subset_sum_mods[sum_mod][0]), *sum_mods_product_subset_sum_mods[sum_mod][0])
                print(len(subset), *subset)
                return

    print("No")

solve()

=======
Suggestion 10

def solve():
    pass
