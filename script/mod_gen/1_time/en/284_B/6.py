def main():
    num = int(input())
    for i in range(num):
        num1 = int(input())
        num2 = input().split()
        count = 0
        for j in range(num1):
            if int(num2[j]) % 2 != 0:
                count += 1
        print(count)
main()

if __name__ == '__main__':
    main()