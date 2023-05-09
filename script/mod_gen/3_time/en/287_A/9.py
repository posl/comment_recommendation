def main():
    n = int(input())
    s_list = [input() for _ in range(n)]
    s_list.sort()
    if s_list[n//2] == s_list[n//2-1]:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()