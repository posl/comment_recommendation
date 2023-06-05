def main():
    a, b = map(int, input().split())
    a_sum, b_sum = 0, 0
    while a > 0:
        a_sum += a % 10
        a //= 10
    while b > 0:
        b_sum += b % 10
        b //= 10
    print(a_sum if a_sum >= b_sum else b_sum)
