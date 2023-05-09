def main():
    n = int(input())
    a_list = [int(i) for i in input().split()]
    x = int(input())
    loop = 0
    sum_a = sum(a_list)
    if x < sum_a:
        for i in range(n):
            if sum_a <= x:
                loop += 1
                sum_a += a_list[i]
            else:
                break
    else:
        loop = n * (x // sum_a)
        sum_a = sum_a * (x // sum_a)
        for i in range(n):
            if sum_a <= x:
                loop += 1
                sum_a += a_list[i]
            else:
                break
    print(loop)
