def main():
    a, b = map(int, input().split())
    a_100 = a // 100
    a_10 = (a - a_100 * 100) // 10
    a_1 = a - a_100 * 100 - a_10 * 10
    b_100 = b // 100
    b_10 = (b - b_100 * 100) // 10
    b_1 = b - b_100 * 100 - b_10 * 10
    a_sum = a_100 + a_10 + a_1
    b_sum = b_100 + b_10 + b_1
    print(max(a_sum, b_sum))
