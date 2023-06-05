def main():
    n = int(input())
    a_list = list(map(int, input().split()))
    b_list = list(map(int, input().split()))
    sum = 0
    for i in range(n):
        if a_list[i] > b_list[i]:
            sum += b_list[i]
            a_list[i] -= b_list[i]
            b_list[i] = 0
        else:
            sum += a_list[i]
            b_list[i] -= a_list[i]
            a_list[i] = 0
        if a_list[i + 1] > b_list[i]:
            sum += b_list[i]
            a_list[i + 1] -= b_list[i]
            b_list[i] = 0
        else:
            sum += a_list[i + 1]
            b_list[i] -= a_list[i + 1]
            a_list[i + 1] = 0
    print(sum)
