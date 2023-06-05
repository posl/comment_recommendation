def main():
    num = int(input())
    for i in range(num):
        n = int(input())
        a_list = list(map(int, input().split()))
        count = 0
        for j in range(n):
            if a_list[j] % 2 == 1:
                count += 1
        print(count)

if __name__ == '__main__':
    main()