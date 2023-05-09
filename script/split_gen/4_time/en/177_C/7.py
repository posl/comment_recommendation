def main():
    N = int(input())
    A = list(map(int, input().split()))
    MOD = 10**9 + 7
    sum_a = sum(A)
    sum_a_square = sum([a**2 for a in A])
    print(((sum_a**2 - sum_a_square)//2)%MOD)
