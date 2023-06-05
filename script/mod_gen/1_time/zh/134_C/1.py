def find_max_except_i(n, a):
    a.sort()
    for i in range(n):
        if i == 0:
            print(a[-1])
        elif i == n - 1:
            print(a[-2])
        else:
            if a[-1] == a[-2]:
                print(a[-1])
            else:
                if a[i] == a[-1]:
                    print(a[-2])
                else:
                    print(a[-1])

if __name__ == '__main__':
    find_max_except_i()