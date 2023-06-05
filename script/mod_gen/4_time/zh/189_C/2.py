def main():
    n = int(input())
    a = list(map(int, input().split()))
    max_a = max(a)
    max_a_index = a.index(max_a)
    max_a_count = a.count(max_a)
    max_a_count_index = max_a_index + max_a_count - 1
    if max_a_index == 0:
        max_a_count_left = 0
    else:
        max_a_count_left = a[:max_a_index].count(max_a)
    if max_a_count_index == n - 1:
        max_a_count_right = 0
    else:
        max_a_count_right = a[max_a_count_index + 1:].count(max_a)
    if max_a_count_left + max_a_count_right == max_a_count:
        print(max_a * max_a_count)
        return
    ans = 0
    for i in range(n):
        for j in range(i, n):
            x = min(a[i:j + 1])
            ans = max(ans, x * (j + 1 - i))
    print(ans)

if __name__ == '__main__':
    main()