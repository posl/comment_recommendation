def main():
    n = int(input())
    s = input()
    flag = False
    for i in range(n):
        if s[i] == '"':
            flag = not flag
        else:
            if flag:
                print(s[i],end='')
            else:
                print('.',end='')
    print('')

if __name__ == '__main__':
    main()