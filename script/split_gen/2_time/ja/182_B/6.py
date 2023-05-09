def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort(reverse=True)
    max_gcd = 0
    max_num = 0
    for i in range(2, A[0] + 1):
        gcd_cnt = 0
        for j in range(N):
            if A[j] % i == 0:
                gcd_cnt += 1
        if gcd_cnt > max_gcd:
            max_gcd = gcd_cnt
            max_num = i
    print(max_num)
