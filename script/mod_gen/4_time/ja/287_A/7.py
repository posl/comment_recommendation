def main():
    n = int(input())
    s_list = []
    for i in range(n):
        s = input()
        s_list.append(s)
    if s_list.count('For') > n//2:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()