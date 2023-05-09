def main():
    num = input().split()
    num.sort(reverse=True)
    print(num[0] + num[1] + num[2])

if __name__ == '__main__':
    main()