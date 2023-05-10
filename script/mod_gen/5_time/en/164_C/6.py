def main():
    num = int(input())
    list = []
    for i in range(num):
        list.append(input())
    print(len(set(list)))

if __name__ == '__main__':
    main()