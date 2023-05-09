def main():
    T = int(input())
    for i in range(T):
        a, s = map(int, input().split())
        if a > s:
            print('No')
        else:
            if a == s:
                print('Yes')
            else:
                if a == 0:
                    print('No')
                else:
                    if s % 2 == 0:
                        print('No')
                    else:
                        if a % 2 == 0:
                            print('No')
                        else:
                            print('Yes')

if __name__ == '__main__':
    main()