def main():
    n = int(input())
    a = list(map(int, input().split()))
    sum_a = sum(a)
    sum_a_square = sum([i**2 for i in a])
    ans = (sum_a**2 - sum_a_square) // 2 % (10**9 + 7)
    print(ans)
