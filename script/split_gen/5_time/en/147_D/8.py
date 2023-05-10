def xor_sum(a):
    res = 0
    for i in range(60):
        cnt = 0
        for j in range(len(a)):
            if(a[j] >> i) & 1:
                cnt += 1
        res += (cnt*(len(a)-cnt)) * (1 << i)
        res %= 10**9+7
    return res
N = int(input())
A = list(map(int, input().split()))
print(xor_sum(A))
