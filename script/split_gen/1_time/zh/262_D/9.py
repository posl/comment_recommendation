def main():
    N = int(input())
    A = list(map(int, input().split()))
    cnt = 0
    for i in range(1, 2**N):
        sum = 0
        for j in range(N):
            if ((i >> j) & 1):
                sum += A[j]
        if (sum % (i.bit_length()) == 0):
            cnt += 1
    print(cnt)
