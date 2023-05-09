def main():
    n = int(input())
    a_list = list(map(int, input().split()))
    x = int(input())
    sum_a = sum(a_list)
    sum_b = sum_a * (x // sum_a)
    i = n * (x // sum_a)
    while sum_b <= x:
        sum_b += a_list[i % n]
        i += 1
    print(i)
