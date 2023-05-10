def main():
    input_list = list(map(int, input().split()))
    alpha_list = list('abcdefghijklmnopqrstuvwxyz')
    for i in range(26):
        print(alpha_list[input_list[i]-1], end='')

if __name__ == '__main__':
    main()