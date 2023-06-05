def main():
    num = int(input())
    list = input().split()
    max = 0
    for i in range(num):
        if int(list[i]) > max:
            max = int(list[i])
            max_index = i + 1
    print(max_index)

if __name__ == '__main__':
    main()