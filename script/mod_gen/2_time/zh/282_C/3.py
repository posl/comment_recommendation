def main():
    n = int(input())
    s = input()
    s_list = list(s)
    for i in range(0, n, 2):
        s_list[i] = '.'
    print(''.join(s_list))

if __name__ == '__main__':
    main()