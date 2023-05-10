def main():
    n = int(input())
    a = list(map(int, input().split()))
    sum_inv_a = 0
    for i in range(n):
        sum_inv_a += 1/a[i]
    print(1/sum_inv_a)
