def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = list(map(int, input().split()))
    b_dict = {}
    for i in range(n):
        b_dict[b[i]] = b_dict.get(b[i], 0) + 1
    c_dict = {}
    for i in range(n):
        c_dict[c[i]] = c_dict.get(c[i], 0) + 1
    b_c = {}
    for i in range(n):
        b_c[b[i]] = b_c.get(b[i], []) + [c[i]]
    c_a = {}
    for i in range(n):
        c_a[c[i]] = c_a.get(c[i], []) + [a[i]]
    c_a_count = {}
    for k, v in c_a.items():
        c_a_count[k] = {}
        for i in v:
            c_a_count[k][i] = c_a_count[k].get(i, 0) + 1
    count = 0
    for k, v in b_dict.items():
        if k in b_c:
            for i in b_c[k]:
                if i in c_dict:
                    count += b_dict[k] * c_dict[i]
                    if i in c_a_count:
                        count -= b_dict[k] * c_a_count[i][k]
    print(count)

if __name__ == '__main__':
    main()