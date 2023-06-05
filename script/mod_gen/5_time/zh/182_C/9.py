def main():
    N = int(input())
    digits = list(map(int, list(str(N))))
    sum_digits = sum(digits)
    if sum_digits % 3 == 0:
        print(0)
        return
    elif sum_digits % 3 == 1:
        if 1 in digits:
            print(1)
            return
        elif 2 in digits and len(digits) > 1:
            print(2)
            return
        else:
            print(-1)
            return
    else:
        if 2 in digits:
            print(1)
            return
        elif 1 in digits and len(digits) > 1:
            print(2)
            return
        else:
            print(-1)
            return

if __name__ == '__main__':
    main()