def main():
    N = int(input())
    A = list(map(int, input().split()))
    A = [a % 200 for a in A]
    #print(A)
    memo = {}
    for i in range(2 ** N):
        b = []
        c = []
        for j in range(N):
            if (i >> j) & 1:
                b.append(j + 1)
            else:
                c.append(j + 1)
        #print(b, c)
        if len(b) == 0 or len(c) == 0:
            continue
        sum_b = sum([A[i] for i in b])
        sum_c = sum([A[i] for i in c])
        if sum_b % 200 == sum_c % 200:
            print("Yes")
            print(len(b), *b)
            print(len(c), *c)
            return
        if sum_b % 200 in memo:
            print("Yes")
            print(len(b), *b)
            print(len(memo[sum_b % 200]), *memo[sum_b % 200])
            return
        memo[sum_b % 200] = b
    print("No")
