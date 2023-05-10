def main():
    n = int(input())
    a = []
    b = []
    for i in range(n):
        a_i, b_i = map(int, input().split())
        a.append(a_i)
        b.append(b_i)
    a_sum = sum(a)
    b_sum = sum(b)
    # print(a_sum, b_sum)
    if a_sum < b_sum:
        print(0)
        exit()
    diff = [a_i - b_i for a_i, b_i in zip(a, b)]
    # print(diff)
    diff.sort(reverse=True)
    # print(diff)
    count = 0
    for d in diff:
        count += 1
        a_sum -= d
        if a_sum < b_sum:
            break
    print(count)

if __name__ == '__main__':
    main()