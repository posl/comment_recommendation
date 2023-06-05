def main():
    n = int(input())
    a = []
    b = []
    for i in range(n):
        a_i, b_i = map(int, input().split())
        a.append(a_i)
        b.append(b_i)
    sum_a = sum(a)
    sum_b = sum([a_i / b_i for a_i, b_i in zip(a, b)])
    #print(sum_a, sum_b)
    sum_a_b = sum_a / sum_b
    sum_a_b_i = 0
    for i in range(n):
        sum_a_b_i += a[i] / b[i]
        if sum_a_b_i >= sum_a_b:
            print(sum_a_b_i)
            break
