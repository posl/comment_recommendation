def main():
    num_list = input().split()
    num_list = [int(i) for i in num_list]
    num_list.sort()
    print(sum(num_list[-2:]))

if __name__ == '__main__':
    main()