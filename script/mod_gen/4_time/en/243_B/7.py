def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    a_dict = {}
    b_dict = {}
    for i in range(n):
        a_dict[a[i]] = i
        b_dict[b[i]] = i
    a_set = set(a)
    b_set = set(b)
    a_b_same = a_set & b_set
    a_b_diff = a_set ^ b_set
    same = 0
    diff = 0
    for i in a_b_same:
        if a_dict[i] == b_dict[i]:
            same += 1
        else:
            diff += 1
    print(same)
    print(diff)

if __name__ == '__main__':
    main()