def main():
    N = int(input())
    item_list = []
    for i in range(N):
        item_list.append(input())
    print(len(set(item_list)))

if __name__ == '__main__':
    main()