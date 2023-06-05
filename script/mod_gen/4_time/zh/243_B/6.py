def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    a_set = set(a)
    b_set = set(b)
    a_b_same = a_set & b_set
    a_b_diff = a_set ^ b_set
    a_b_same_num = 0
    a_b_diff_num = 0
    for i in range(n):
        if a[i] in a_b_same and b[i] in a_b_same:
            a_b_same_num += 1
        if a[i] in a_b_diff or b[i] in a_b_diff:
            a_b_diff_num += 1
    print(a_b_same_num)
    print(a_b_diff_num)

if __name__ == '__main__':
    main()