def main():
    N = int(input())
    name_list = []
    for i in range(N):
        name_list.append(input().split())
    name_set = set()
    for name in name_list:
        if tuple(name) in name_set:
            print('Yes')
            return
        else:
            name_set.add(tuple(name))
    print('No')

if __name__ == '__main__':
    main()