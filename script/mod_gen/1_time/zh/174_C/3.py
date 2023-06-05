def problem174_c():
    k = int(input())
    if k % 2 == 0:
        print(-1)
    else:
        num = 7
        count = 1
        while True:
            if num % k == 0:
                print(count)
                break
            else:
                num = num * 10 + 7
                count += 1

if __name__ == '__main__':
    problem174_c()