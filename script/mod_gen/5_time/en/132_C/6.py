def count_difficulty(d, K):
    count = 0
    for i in range(len(d)):
        if d[i] >= K:
            count += 1
    return count
N = int(input())
d = list(map(int, input().split()))
d.sort()
K = d[N//2]
print(K)
print(count_difficulty(d, K))
print(count_difficulty(d, K+1))
print(count_difficulty(d, K-1))
print(count_difficulty(d, K+2))
print(count_difficulty(d, K-2))
print(count_difficulty(d, K+3))
print(count_difficulty(d, K-3))
print(count_difficulty(d, K+4))
print(count_difficulty(d, K-4))
print(count_difficulty(d, K+5))
print(count_difficulty(d, K-5))
print(count_difficulty(d, K+6))
print(count_difficulty(d, K-6))
print(count_difficulty(d, K+7))
print(count_difficulty(d, K-7))
print(count_difficulty(d, K+8))
print(count_difficulty(d, K-8))
print(count_difficulty(d, K+9))
print(count_difficulty(d, K-9))
print(count_difficulty(d, K+10))
print(count_difficulty(d, K-10))
print(count_difficulty(d, K+11))
print(count_difficulty(d, K-11))
print(count_difficulty(d, K+12))
print(count_difficulty(d, K-12))
print(count_difficulty(d, K+13))
print(count_difficulty(d, K-13))
print(count_difficulty(d, K+14))
print(count_difficulty(d, K-14))
print(count_difficulty(d, K+15))
print(count_difficulty(d, K-15))
print(count_difficulty(d, K+16))
print(count_difficulty(d, K-16))
print(count_difficulty(d, K+17))
print(count_difficulty(d, K-17))
print(count_difficulty(d, K+18))
print(count_difficulty(d, K-18))
print(count_difficulty(d, K+19))
print(count_difficulty(d, K-19))
print(count_difficulty(d, K+20))
print(count_difficulty(d, K-20))
print(count_difficulty(d, K+21))
print(count_difficulty(d, K-21))
print(count_difficulty(d
