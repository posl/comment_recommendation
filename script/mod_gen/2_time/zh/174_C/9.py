def problem174_c():
    k = int(input())
    if k % 2 == 0 or k % 5 == 0:
        print(-1)
    else:
        x = 7
        for i in range(1, k + 1):
            if x % k == 0:
                print(i)
                break
            else:
                x = x * 10 + 7
        else:
            print(-1)

if __name__ == '__main__':
    problem174_c()