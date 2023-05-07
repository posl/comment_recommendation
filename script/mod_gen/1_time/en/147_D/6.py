def xor_sum(A):
    total = 0
    for i in range(len(A)):
        for j in range(i+1, len(A)):
            total += A[i] ^ A[j]
    return total % (10**9+7)
N = int(input())
A = list(map(int, input().split()))
print(xor_sum(A))

if __name__ == '__main__':
    xor_sum()