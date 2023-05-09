def main():
    a, b = map(int, input().split())
    sum_a = sum(map(int, str(a)))
    sum_b = sum(map(int, str(b)))
    print(max(sum_a, sum_b))
