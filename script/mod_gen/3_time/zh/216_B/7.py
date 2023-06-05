def main():
    N = int(input())
    name_list = []
    for i in range(N):
        name_list.append(input())
    if len(name_list) == len(set(name_list)):
        print('No')
    else:
        print('Yes')

if __name__ == '__main__':
    main()