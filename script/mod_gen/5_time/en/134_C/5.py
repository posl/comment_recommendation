def main():
    n = int(input())
    a = [int(input()) for i in range(n)]
    a_max = max(a)
    a_max2 = sorted(a)[-2]
    for i in a:
        if i == a_max:
            print(a_max2)
        else:
            print(a_max)

if __name__ == '__main__':
    main()