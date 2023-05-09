def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    max_gcd = 0
    max_gcd_num = 0
    for i in range(2, A[-1]+1):
        gcd_num = 0
        for j in range(N):
            if A[j] % i == 0:
                gcd_num += 1
        if gcd_num >= max_gcd:
            max_gcd = gcd_num
            max_gcd_num = i
    print(max_gcd_num)
