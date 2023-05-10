def main():
    n = int(input())
    a_list = [int(x) for x in input().split()]
    a_list.sort()
    prev = a_list[0]
    prev_count = 1
    prev_index = 0
    result_list = [0] * n
    for i in range(1, n):
        if a_list[i] == prev:
            prev_count += 1
        else:
            for j in range(prev_index, i):
                result_list[j] = i - prev_index - prev_count
            prev = a_list[i]
            prev_count = 1
            prev_index = i
    for j in range(prev_index, n):
        result_list[j] = n - prev_index - prev_count
    for i in range(n):
        print(result_list[i])

if __name__ == '__main__':
    main()