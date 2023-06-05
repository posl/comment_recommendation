def main():
    k = int(input())
    if k % 2 == 0:
        print("-1")
    else:
        a = 7
        for i in range(1, k + 1):
            if a % k == 0:
                print(i)
                break
            else:
                a = a * 10 + 7
        else:
            print("-1")

if __name__ == '__main__':
    main()