def main():
    n, m, k = map(int, input().split())
    a_list = list(map(int, input().split()))
    b_list = list(map(int, input().split()))
    a_sum_list = [0]
    for a in a_list:
        a_sum_list.append(a_sum_list[-1] + a)
    b_sum_list = [0]
    for b in b_list:
        b_sum_list.append(b_sum_list[-1] + b)
    max_count = 0
    a_count = 0
    b_count = 0
    while a_count <= n:
        if a_sum_list[a_count] > k:
            break
        while b_sum_list[b_count] <= k - a_sum_list[a_count]:
            b_count += 1
        max_count = max(max_count, a_count + b_count - 1)
        a_count += 1
    print(max_count)

if __name__ == '__main__':
    main()