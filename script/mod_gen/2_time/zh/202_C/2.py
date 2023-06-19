def problem202_c():
    n = int(input())
    a = [int(x) for x in input().split()]
    b = [int(x) for x in input().split()]
    c = [int(x) for x in input().split()]
    a_dict = {}
    b_dict = {}
    c_dict = {}
    for i in range(n):
        a_dict[i] = a[i]
        b_dict[i] = b[i]
        c_dict[i] = c[i]
    a_dict = sorted(a_dict.items(), key=lambda x:x[1])
    b_dict = sorted(b_dict.items(), key=lambda x:x[1])
    c_dict = sorted(c_dict.items(), key=lambda x:x[1])
    count = 0
    for i in range(n):
        for j in range(n):
            if a_dict[i][1] == b_dict[c_dict[j][1]-1][1]:
                count += 1
    print(count)

if __name__ == '__main__':
    problem202_c()