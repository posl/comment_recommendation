def convert(n, k):
    if n < k:
        return str(n)
    else:
        return convert(n//k, k) + str(n%k)
N, K = map(int, input().split())
print(len(convert(N, K)))
